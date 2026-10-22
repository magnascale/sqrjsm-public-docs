---
name: Service Quality Review documentation
description: Magnascale's reading-focused MkDocs Material documentation system.
colors:
  forest: "#153f34"
  forest-light: "#285a48"
  forest-dark: "#103127"
  link: "#245e47"
  focus: "#467047"
  lime: "#d7ef90"
  off-white: "#fffefa"
  cream: "#f6f5ee"
  ink: "#253c34"
  muted-ink: "#496156"
  subdued-ink: "#65796e"
  pale-green: "#e9eedb"
  border: "#dce3d7"
  notice-border: "#b3c5af"
  table-header: "#f0f2e8"
  code-background: "#f0f1e9"
typography:
  headline:
    fontFamily: "Manrope, sans-serif"
    fontSize: "2.1rem"
    fontWeight: 750
    lineHeight: 1.18
    letterSpacing: "-.035em"
  body:
    fontFamily: "Manrope, sans-serif"
    fontSize: ".82rem"
    lineHeight: 1.8
  lead:
    fontFamily: "Manrope, sans-serif"
    fontSize: "1.04rem"
    lineHeight: 1.7
  table:
    fontSize: ".73rem"
    lineHeight: 1.65
  caption:
    fontSize: ".68rem"
rounded:
  screenshot: "8px"
components:
  notice:
    backgroundColor: "{colors.cream}"
  notice-title:
    backgroundColor: "{colors.pale-green}"
  table-heading:
    backgroundColor: "{colors.table-header}"
    textColor: "{colors.forest}"
---

# Design System: Service Quality Review documentation

## Overview

The portal extends Magnascale's established forest, cream, and lime identity through a reading-focused MkDocs Material layout. It preserves the familiar documentation shell rather than introducing a new visual world. The character is practical, calm, and factual: strong headings, readable guides, and restrained product imagery.

**Key Characteristics:**

- Locally served Manrope and an off-white reading surface.
- Forest navigation and headings, with lime reserved for selection and navigation emphasis.
- Standard documentation wayfinding and clear, sequential guide content.
- Real product screenshots with synthetic data and descriptive captions.

## Colors

Forest anchors the navigation, footer, and headings; off-white carries the reading surface. Cream and pale green distinguish notices, while thin neutral borders organize tables and screenshots. Dark ink and muted ink support the text hierarchy. Link green identifies content links; lime highlights selected text and active or hovered top-level navigation.

**The Readable Link Rule.** Content links remain underlined at rest and on hover. Heading permalink symbols are exempt; navigation uses its native active-state treatment.

## Typography

Manrope is served from the repository's font asset with a sans-serif fallback, a variable weight range of 200–800, and `font-display: swap`. Body text enables the font's `ss01` feature. The frontmatter records the authored type values; other documentation chrome and heading sizes inherit MkDocs Material's hierarchy.

Headings use forest and balanced wrapping. Second-level headings have a weight of 730, a line height of 1.35, and slightly tightened tracking; third-level headings use weight 700. Strong text uses weight 750. Body paragraphs and lists stop at 73 characters; leads stop at 58, and captions at 70. Tables use tabular numerals. Captions are left aligned and upright.

## Layout

Retain the standard MkDocs Material shell: top-level tabs, section navigation, a reading column, on-page contents, search, previous/next links, and return-to-top behavior. At wide sizes the grid has a maximum width of 65rem from 76.25em. Mobile uses the native navigation drawer instead of the desktop sidebars.

Below 44.99em, the main heading becomes 1.65rem and the lead .94rem. The availability banner becomes left aligned. Table cells have a minimum width of 7rem and retain Material's horizontal scrolling behavior. Figures occupy the reading column and keep explanatory captions adjacent.

Heading spacing separates tasks without introducing decorative panels. Second-level headings have 2.1em of space above; list items have .5em below; figures have 1.6rem vertical margins. Anchor scrolling reserves 8rem for the header.

## Elevation & Depth

Content is flat: background tints and thin borders distinguish notices, tables, and screenshots. Notices explicitly have no shadow. The header alone uses a soft `0 3px 16px #1031271f` shadow to separate persistent navigation from the page. Preserve native Material interaction surfaces rather than introducing a new elevation scale.

## Shapes

Use Material's existing component shapes. Product screenshots have gently rounded corners using the screenshot token and a single-pixel neutral border. Notices and tables use a single-pixel border; no custom card or button system is introduced.

## Components

**Navigation.** Forest header and tabs carry the product logo, title, search, and task sections. Top-level tabs use subdued opacity at rest and lime at full opacity when active or hovered. Active section links use weight 750. The footer continues the forest tones and native previous/next navigation.

**Content links and focus.** Keep content and availability-banner links visibly underlined with an offset of .18em. Keyboard focus uses a three-pixel focus-colored outline offset by three pixels. Inputs use a forest caret. Text selection pairs lime with forest text.

**Notices.** Cream bodies and pale-green titles use a muted green border, no shadow, and .75rem text. The title icon uses the lighter forest tone. Notices communicate contextual guidance without competing with the page heading.

**Tables.** Use standard Markdown tables, pale header rows, bold forest heading text, neutral borders, and the compact table typography. Keep the standard responsive overflow behavior.

**Screenshots.** Use real product views containing synthetic data, with useful alternative text and a visible factual caption. Keep the product interface intact rather than recoloring it to match the documentation shell.

**Availability banner.** A compact pale-green announcement above the header identifies the upcoming release and links to availability policy. Its type is .65rem; the linked policy is bold and underlined.

## Do's and Don'ts

- **Do** inherit the established Magnascale assets, palette, and local Manrope font.
- **Do** preserve Material's navigation, search, contents, keyboard access, and responsive behavior.
- **Do** keep content links persistently underlined and focus clearly visible.
- **Do** use readable measures, descriptive headings, and restrained synthetic product screenshots.
- **Don't** introduce a replacement brand, ornamental card system, or custom navigation grammar for a local extension.
- **Don't** add third-party font requests or analytics as part of the visual system.
