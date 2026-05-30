---
name: scrape-url
description: Scrape a URL to a clean Markdown file (full text, no summaries, no nav/menus), then discover same-domain links and let the user select which ones to also scrape. Handles paywalled sites via cookie injection.
---

# scrape-url

Scrape a URL into a clean Markdown file, discover same-domain links, and let you choose which to scrape next. Handles JavaScript-rendered pages, Cloudflare-protected sites, and login-walled content.

## Usage

```
/scrape-url <url>
/scrape-url <url> --output <path>
/scrape-url <url> --cookies <name=value,name=value,...>
```

- `<url>` — the page to scrape (required)
- `--output <path>` — folder to write MD files into (optional, default: `_raw/`)
  - Paths are relative to the vault root
  - Examples: `_raw/`, `Workspaces/Work/Projects/knowledge-scraping/sources/`
- `--cookies <cookie-string>` — inject session cookies for paywalled/login-protected sites (optional)
  - Format: `name1=value1;name2=value2` (semicolon-separated)
  - Typically: a WordPress `wordpress_logged_in_*` cookie + any Cloudflare `cf_clearance` cookie
- `--force` — overwrite even if URL exists in registry (use to refresh stale content)

---

## Steps

### Phase 0 — Detect site protection

Before scraping, assess the URL:

- **JavaScript-heavy / SPA** (URL has `#fragment`, or site is known to be a React/Next.js app):
  add `waitFor: 5000` to the scrape call to allow JS to render.
- **Cloudflare-protected** (domains using Cloudflare WAF):
  use `proxy: "stealth"` instead of the default proxy.
- **Login-walled** (`--cookies` provided OR previous scrape returned paywall markers):
  use the **Authenticated Session Workflow** (Phase 1b) instead of Phase 1.

Paywall markers to detect in scraped content:
- `"Log in to continue reading"`
- `"Access the full article"`
- `"Login"` appearing as a heading mid-article
- Content that abruptly ends after 1-2 sections followed by a cookie banner
- **Silent truncation**: page metadata says "X min read" but scraped content is far too short (e.g. "10 min read" → fewer than 400 words = truncated)
- **Key Takeaways trap**: content ends with a "Key Takeaways" section immediately after a short summary with no detailed body sections in between — this is the SAFe-style free preview pattern

---

### Phase 0b — Duplicate check (registry)

Before scraping any URL, check `_meta/scrape-registry.json`:

1. Read `_meta/scrape-registry.json`. If the file doesn't exist yet, create it as `{}`.
2. If the URL is already in the registry AND `--force` was NOT passed:
   - Report: `⏭ Already scraped: <url> (slug: <slug>, date: <scraped>, words: ~<words>)`
   - Ask the user: **skip** (default), **re-scrape** (refresh), or **show existing entry**?
   - If skip → do not scrape; move on.
   - If re-scrape → proceed but overwrite both the file and registry entry.
3. If the URL is NOT in the registry → proceed to Phase 1.

**Registry format** (`_meta/scrape-registry.json`):
```json
{
  "https://example.com/article": {
    "slug": "example_com_article.md",
    "scraped": "YYYY-MM-DD",
    "words": 1200,
    "authenticated": false,
    "ingested": false
  }
}
```

**After every successful save**, update the registry:
- Add or update the entry for the URL
- Set `scraped` to today's date
- Set `words` to actual word count
- Set `authenticated: true` if cookies were used
- `ingested` stays `false` until the wiki ingestion pipeline updates it

**Note:** `registry.json` must NEVER be deleted when clearing `_raw/` — it is the permanent duplicate-prevention record.

---

### Phase 1 — Scrape the target URL (unauthenticated)

1. Parse `--output` from args. If not provided, use `_raw/`.
2. Derive the slug for the file name from the URL:
   - Remove the protocol (`https://`, `http://`)
   - Replace every `/`, `.`, `?`, `=`, `&`, `#` with `_`
   - Collapse consecutive underscores into one
   - Strip leading/trailing underscores
   - Lowercase the result
   - Append `.md`
   - Examples:
     - `https://docs.anthropic.com/en/overview` → `docs_anthropic_com_en_overview.md`
     - `https://framework.scaledagile.com/#big-picture` → `framework_scaledagile_com_big-picture.md`
3. Check for duplicates (two-step):
   a. **Registry check** (Phase 0b) — already done above.
   b. **File check** — if the output file already exists on disk AND `--force` was not passed, ask: overwrite, skip, or rename?
4. Call `firecrawl_scrape` with:
   - `url`: the target URL
   - `formats`: `["markdown"]`
   - `onlyMainContent`: `true` ← strips nav, menus, headers, footers
   - `proxy`: `"stealth"` if site is Cloudflare-protected; otherwise omit
   - `waitFor`: `5000` if site is JavaScript-rendered; otherwise omit
5. If the scrape fails, report the error and stop.
6. **Check for paywall markers** in the returned content. If detected → switch to Phase 1b.
7. Prepend a metadata header to the scraped content:
   ```
   ---
   source_url: <url>
   scraped: <YYYY-MM-DD>
   ---
   ```
8. Write the file to `<output>/<slug>.md`.
9. Confirm: `Saved: <output>/<slug>.md (~<word count> words)`

---

### Phase 1a — Validate scraped content (mandatory)

After every scrape — unauthenticated or authenticated — run all validation checks before saving. **Never save a file that fails validation without flagging it.**

**Check 1 — Hard paywall markers** (fail immediately):
- Content contains `"Log in to continue reading"` or `"Access the full article"` or `"Login"` as a heading → FAIL

**Check 2 — Silent truncation (Key Takeaways trap)**:
- Content contains `"Key Takeaways"` AND the total word count is fewer than 300 words → FAIL
- Rationale: legitimate articles with Key Takeaways sections have substantial body content before them; a preview-only article jumps straight from a short summary to Key Takeaways

**Check 3 — Reading time mismatch**:
- If the page metadata includes `twitter:data1` or similar "Est. reading time" field showing "X minutes":
  - "3 min" → expect at least 450 words
  - "5 min" → expect at least 750 words
  - "10 min" → expect at least 1500 words
  - "15 min" → expect at least 2250 words
- If actual word count is less than 50% of the expected minimum → FAIL

**Check 4 — Bare minimum length**:
- Any article shorter than 100 words (excluding frontmatter) is suspicious → WARN and ask user to verify

**On validation FAIL:**
1. Do NOT save the file (or if overwriting, do not overwrite the existing file)
2. Report: `⚠️ Truncated: <url> — <reason>`
3. If `--cookies` was provided → automatically switch to Phase 1b (authenticated scrape) and re-validate
4. If no cookies provided → add to a "needs-auth" list and report at the end:
   ```
   Auth needed (re-run with --cookies):
     - https://example.com/article-1
     - https://example.com/article-2
   ```

**On validation WARN (bare minimum):**
- Save the file but add `note: content may be incomplete — verify manually` to frontmatter.

---

### Phase 1b — Authenticated scrape (paywalled content)

Use this when Phase 1 detects a paywall OR when `--cookies` was provided.

**Step 1 — Open a live browser session:**

Call `firecrawl_scrape` on the target URL (with stealth proxy) to get a `scrapeId` from the metadata. This opens a live Playwright browser session.

**Step 2 — Inject cookies:**

Call `firecrawl_interact` with the scrapeId, `language: "node"`, and this code pattern:

```javascript
await page.context().addCookies([
  {
    name: '<cookie-name>',
    value: '<cookie-value>',
    domain: '<domain>',      // e.g. 'framework.scaledagile.com' or '.scaledagile.com'
    path: '/',
    httpOnly: true,
    secure: true,
    sameSite: 'Lax'          // or 'None' for cross-site cookies
  },
  // add more cookies as needed
]);
await page.reload({ waitUntil: 'networkidle', timeout: 30000 });
const bodyLen = await page.evaluate(() => document.body.innerText.length);
const isAuth = await page.evaluate(() => document.body.innerText.includes('<username or auth indicator>'));
process.stdout.write('len:' + bodyLen + ' auth:' + isAuth);
```

Important REPL notes:
- `await` at top level works in this REPL environment **after at least one prior code call** has been made in the session.
- If you get `SyntaxError: await is only valid in async functions`, make a dummy first call (e.g., `process.stdout.write('prime');`), then retry.
- Do NOT use `.then()` chains for multi-step flows — they return `[object Promise]` before completing. Use `await` instead.
- Each `firecrawl_interact` call on the same scrapeId shares REPL state — variables declared persist across calls.

**Step 3 — Extract content:**

After injection is confirmed (auth:true in stdout), call `firecrawl_interact` again:

```javascript
await page.goto('<url>', { waitUntil: 'networkidle', timeout: 30000 });
const content = await page.evaluate(() => {
  const el = document.querySelector('.entry-content')   // WordPress
           || document.querySelector('article')          // generic
           || document.querySelector('main')
           || document.body;
  return el.innerText;
});
process.stdout.write(content);
```

**Step 4 — For multiple articles in the same session:**

Re-use the same scrapeId — cookies persist within a session. Navigate sequentially (not in parallel — parallel calls on the same scrapeId conflict):

```javascript
await page.goto('<next-url>', { waitUntil: 'networkidle', timeout: 30000 });
const art = await page.evaluate(() => (document.querySelector('.entry-content') || document.body).innerText);
process.stdout.write(art);
```

**Step 5 — Save:** Apply the same slug derivation, metadata header, and file write as Phase 1 Steps 7–9. Add `authenticated: true` to the frontmatter.

---

### Phase 2 — Discover same-domain links

10. Extract the base domain from the URL (e.g., `https://docs.anthropic.com/en/overview` → `docs.anthropic.com`).
11. Call `firecrawl_map` with:
    - `url`: `https://<base-domain>`
    - No filters — get all URLs
12. Filter the results:
    - Keep only same-domain links
    - Exclude: external domains, `mailto:`, bare anchors (`#only`)
    - Exclude the URL already scraped in Phase 1
    - **Apply smart filtering** if results > 200: remove obvious non-article paths such as `/blog/glossary_term/`, `/blog/category/`, `/blog/author/`, `/blog/media_category/`, `/blog/tag/`, `/contact`, `/thank-you`, `/ways-to-signup`
13. If no links found after filtering, report and stop.
14. **Organize links by category** when possible (group by URL path pattern):
    - Show main reference articles first
    - Blog posts / extended guidance separately
    - Utility pages last (or omit entirely)
15. If more than 50 links remain, show the first 50 and note how many were omitted. Offer to show more (`m`) or show next category.
16. Display a numbered list:
    ```
    Found <N> links on <domain>. Select which to scrape:

     CORE ARTICLES
      1. https://example.com/overview
      2. https://example.com/quickstart

     EXTENDED GUIDANCE
      3. https://example.com/advanced-topic-x

    Enter numbers or ranges (e.g. 1,3,5-8), or:
      a  — scrape all
      n  — done, skip remaining
      m  — show more links (if list was truncated)
    ```

---

### Phase 3 — Scrape selected links

17. Parse the user's input:
    - Single numbers: `3` → index 3
    - Ranges: `5-8` → indices 5, 6, 7, 8
    - Comma-separated: `1,3,5-8` → indices 1, 3, 5, 6, 7, 8
    - `a` → all links
    - `n` → stop
18. For each selected URL, repeat Phase 1 (or Phase 1b if authenticated):
    - Derive slug → check exists → scrape → check for paywall → save
    - Process them **sequentially** (not in parallel) when using authenticated sessions; parallel is fine for unauthenticated scrapes.
    - Report each save immediately so progress is visible.
    - If a scrape fails, log the failure and continue with the next URL.
19. When all selected links are done, print a summary:
    ```
    Done.
      Saved:        <N> files to <output>/
      Skipped:      <N> (already existed)
      Failed:       <N>
      Auth-needed:  <N> (truncated — re-run with --cookies)
      Warnings:     <N> (saved but flagged for manual review)

    Files written:
      - example_com_overview.md  (~1200 words) ✅
      - example_com_quickstart.md  (~800 words) ✅
      ...

    Needs auth (truncated, not saved):
      - https://example.com/gated-article
    ```

---

## Rules

- **Registry is permanent** — always read `_meta/scrape-registry.json` before scraping and always write to it after saving. Never delete `registry.json` when clearing `_raw/` files — it is the long-term duplicate prevention record.
- **`--force` overrides registry** — use only when intentionally refreshing stale content.
- **Never summarize** — write the full scraped text. `onlyMainContent: true` handles stripping nav/menus; do not truncate or condense further.
- **Always validate before saving** — run all Phase 1a checks on every scrape result, unauthenticated or authenticated. A file must pass validation before it is written.
- **Never save silently truncated content** — if validation fails and no cookies are available, report it rather than saving a partial file.
- **Never overwrite silently** — always ask the user before overwriting an existing file.
- **Slug uniqueness** — if two URLs produce the same slug, append `_2`, `_3`, etc.
- **Collapse underscores** — consecutive underscores in slugs (from `/#anchor`) should be collapsed to one.
- **Output path** — if the output folder does not exist, create it before writing.
- **Relative paths** — resolve all `--output` paths from the vault root, not from the current working directory.
- **Same-domain only** — never follow or list links that go to external domains.
- **Metadata header** — always prepend the `source_url` + `scraped` frontmatter block. Add `authenticated: true` when cookies were used. Add `note:` if content was image-only or otherwise incomplete.
- **Stealth proxy** — use for any site that shows Cloudflare protection or bot detection.
- **waitFor** — use 5000ms for any JavaScript-rendered single-page app or hash-fragment URL.
- **Content selector priority** — always try `.entry-content` → `article` → `main` → `body`; this avoids capturing nav and footer text.
- **Sequential auth sessions** — never fire parallel `firecrawl_interact` calls on the same scrapeId; they conflict. Process one article at a time within a session.
- **Session reuse** — within one auth session (same scrapeId), cookies persist. Re-inject only when starting a new session.
