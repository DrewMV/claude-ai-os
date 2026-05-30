---
type: meta
updated: 2026-05-30
---

# Scrape Registry

`_meta/scrape-registry.json` is the **permanent record of every URL ever scraped** into this vault.

## Purpose

It exists to prevent duplicate scraping — even after `_raw/` files are deleted or after wiki ingestion.
Unlike the MD files in `_raw/`, this file must **never be deleted**.

## Structure

```json
{
  "https://example.com/article": {
    "slug":          "example_com_article.md",
    "scraped":       "YYYY-MM-DD",
    "words":         1200,
    "authenticated": false,
    "ingested":      false
  }
}
```

| Field | Meaning |
|---|---|
| `slug` | Filename used in `_raw/` |
| `scraped` | Date the URL was last scraped |
| `words` | Word count of saved content |
| `authenticated` | `true` if scraped with session cookies (bypassed paywall) |
| `ingested` | `true` once the file has been processed into a wiki page via `/wiki-ingest` |

## How it gets updated

- **Written by** `/scrape-url` — adds an entry after every successful scrape
- **Updated by** `/wiki-ingest` — sets `ingested: true` when the source file is processed into a wiki page
- **Read by** `/scrape-url` — checked before every scrape to prevent duplicates

## Safe cleanup workflow

1. Run `/wiki-ingest` on `_raw/` to process all pending files
2. Registry entries with `ingested: true` are safe to delete from `_raw/`
3. Delete `_raw/*.md` freely — registry entries remain and prevent future re-scraping
4. **Never delete `scrape-registry.json` itself**

## Current coverage

Run this to check status:
```
/wiki-status
```

Or inspect the registry directly:
- Total entries: the number of keys in `scrape-registry.json`
- Ingested: count of entries where `ingested: true`
- Pending ingest: count where `ingested: false`
