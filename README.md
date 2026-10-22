# Service Quality Review documentation

Customer documentation for **Service Quality Review for Jira Service Management**, by Magnascale.

**Portal:** https://magnascale.github.io/sqrjsm-public-docs/

The portal covers setup, review programs, criteria, sampling, human assessments, optional AI, calibration, results, coaching, administration, and support. Product availability is described on the portal; the documentation's publication does not announce a Marketplace launch.

## Local preview

Use Python 3.12. Create a virtual environment, activate it, and install the hash-locked dependencies:

```sh
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install --require-hashes -r requirements.txt
python -m mkdocs serve
```

## Validate

```sh
python -m mkdocs build --strict
python scripts/check_site.py
```

The validation checks generated local links, anchors, assets, search-index presence, and common publication-boundary mistakes. Review prose and screenshots manually for accuracy and confidential material; an automated check cannot prove these are safe.

## Publishing

Changes go through a `codex/` branch and pull request. The Documentation workflow builds and validates pull requests. After an approved merge to `main`, it builds the same source and deploys the artifact through GitHub Pages. Configure the repository's Pages source as **GitHub Actions**. No personal access token is stored in the workflow.

To update dependencies, edit `requirements.in`, regenerate `requirements.txt` with `uv pip compile requirements.in --generate-hashes --output-file requirements.txt`, then validate locally and in CI.

## Editorial guidance

- Lead with customer tasks and use the product's visible labels.
- Describe implemented behavior, evidence limits, permissions, and uncertainty accurately.
- Keep availability and Marketplace links current; never fabricate an installation URL.
- Keep unpublished contractual drafts and internal engineering evidence out of this public repository.
- Use synthetic, reviewed screenshots. Confirm that no customer data or credentials are visible.
- Keep the five navigation sections small and cross-link related tasks.
- Retain the bundled font's licence when redistributing site assets.

Public issues are for documentation feedback only. Send product, account, security, and privacy information through the private channels listed on the portal.
