"""Validate generated local URLs, anchors, and customer-publication boundaries."""

import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
BASE = "https://magnascale.github.io/sqrjsm-public-docs/"
BASE_PATH = urlsplit(BASE).path


class Document(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for attr in ("href", "src"):
            if attr in attrs:
                self.links.append(attrs[attr])


def public_url(path):
    relative = path.relative_to(SITE).as_posix()
    return BASE + (relative[:-10] if relative.endswith("index.html") else relative)


def main():
    if not SITE.is_dir():
        raise SystemExit("Build the site before running this check.")
    documents = {path.resolve(): Document(path) for path in SITE.rglob("*.html")}
    errors = []
    count = 0
    for path, document in documents.items():
        for link in document.links:
            parsed = urlsplit(urljoin(public_url(path), link))
            if parsed.scheme not in ("https", "http") or parsed.netloc != urlsplit(BASE).netloc:
                continue
            if not parsed.path.startswith(BASE_PATH):
                errors.append(f"{path.relative_to(SITE)}: link escapes the project base: {link}")
                continue
            local = SITE / unquote(parsed.path[len(BASE_PATH):])
            if local.is_dir():
                local = local / "index.html"
            if not local.is_file():
                errors.append(f"{path.relative_to(SITE)}: missing target {link}")
            elif parsed.fragment and local.resolve() in documents:
                if unquote(parsed.fragment) not in documents[local.resolve()].ids:
                    errors.append(f"{path.relative_to(SITE)}: missing anchor {link}")
            count += 1

    forbidden = re.compile(
        r"one-atlas-iczv|magnascaletest|Internal notes \(do not publish\)|"
        r"[A-Z]:[\\/](?:Users|Program Files)[\\/]|"
        r"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})|"
        r"BEGIN (?:RSA |OPENSSH )?PRIVATE KEY",
        re.IGNORECASE,
    )
    for path in (ROOT / "docs").rglob("*"):
        if path.suffix in (".md", ".css", ".svg", ".js") and forbidden.search(path.read_text(encoding="utf-8")):
            errors.append(f"Publication boundary check failed: {path.relative_to(ROOT)}")

    search_path = SITE / "search/search_index.json"
    if not search_path.is_file():
        errors.append("Missing search index")
    else:
        index = json.loads(search_path.read_text(encoding="utf-8"))
        if not index.get("docs"):
            errors.append("Search index has no documents")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Validated {len(documents)} HTML pages and {count} local URLs/anchors; publication and search-index checks passed.")


if __name__ == "__main__":
    main()
