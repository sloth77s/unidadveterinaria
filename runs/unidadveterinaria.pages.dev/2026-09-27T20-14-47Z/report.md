# SEO + AI-search audit — unidadveterinaria.pages.dev

- **Target:** https://unidadveterinaria.pages.dev/ (5 pages analyzed)
- **Generated:** 2026-09-27T20:15:01.616Z · run `2026-09-27T20-14-47Z` · plugin 0.2.0
- **Coverage:** Deterministic subset — model-judged modules not evaluated · data tier 0
- **Platform:** unknown · hosting cloudflare-pages · environment production
- **Findings:** 47

## Scores

| Axis | Score | Band | Coverage | Interpretation |
|---|---:|---|---:|---|
| Search SEO | 44.2 | F | 60% | Foundational SEO issues to fix first. |
| AI Visibility | 78.1 | C \* | 34% | Citable by AI, but weak classic ranking limits reach. |

- **AI Visibility:** \* provisional — below the coverage floor, treat the band as indicative (34/100)

### Search SEO — categories

| Category | Weight | Value | Active | Scored | needs_api | manual_review |
|---|---:|---:|---|---:|---:|---:|
| Indexability & Crawl | 22 | — | no findings | 0 | 0 | 0 |
| Core Web Vitals / Performance | 16 | 50 | yes | 1 | 1 | 0 |
| On-Page & Meta | 12 | 44.7 | yes | 6 | 2 | 0 |
| Structured Data | 12 | 0 | yes | 1 | 0 | 0 |
| Rendering | 8 | — | active, no scored findings | 0 | 1 | 0 |
| Internal Linking & Semantics | 8 | 50 | yes | 4 | 1 | 0 |
| E-E-A-T | 7 | — | no findings | 0 | 0 | 0 |
| Images / Media | 5 | 50 | yes | 1 | 0 | 0 |
| Sitemaps & Discovery | 5 | 50 | yes | 1 | 0 | 0 |
| Freshness | 3 | — | no findings | 0 | 0 | 0 |
| Social Cards | 2 | 25 | yes | 10 | 0 | 0 |
| E-commerce | 15 | — | inactive | 0 | 0 | 0 |
| Local | 10 | — | inactive | 0 | 0 | 0 |
| International | 8 | — | inactive | 0 | 0 | 0 |

### AI Visibility — categories

| Category | Weight | Value | Active | Scored | needs_api | manual_review |
|---|---:|---:|---|---:|---:|---:|
| Answer Extractability | 18 | — | no findings | 0 | 0 | 0 |
| AI Crawler Access | 14 | 100 | yes | 6 | 0 | 0 |
| Fact Density / Original Data | 14 | — | no findings | 0 | 0 | 0 |
| Structured Data | 12 | 0 | yes | 1 | 0 | 0 |
| Rendering (non-JS) | 10 | — | active, no scored findings | 0 | 1 | 0 |
| Entity / Knowledge-Graph | 9 | — | no findings | 0 | 0 | 0 |
| E-E-A-T / Authority | 9 | — | no findings | 0 | 0 | 0 |
| Freshness | 6 | — | no findings | 0 | 0 | 0 |
| Agent-readiness | 4 | 50 | yes | 6 | 1 | 0 |
| Images / Multimodal | 4 | 50 | yes | 1 | 0 | 0 |
| AI discovery & agent endpoints | 0 | 75 | yes | 2 | 0 | 0 |
| Agentic commerce readiness | 6 | — | inactive | 0 | 0 | 0 |
| Local / place data | 5 | — | inactive | 0 | 0 | 0 |

## Site rollup

- role_weights · 5 pages analyzed
- **Weakest pages (Search SEO):** / 37.5 · /preguntas-frecuentes 43.6 · /servicios/citopatologia-veterinaria 48.4
- **Weakest pages (AI Visibility):** / 52.9 · /contacto-y-ubicacion 88.9 · /servicios/citopatologia-veterinaria 88.9

## Sampling

| Template | Type | Discovered | Sampled |
|---|---|---:|---:|
| /servicios/* | — | 11 | 2 |
| /* | MedicalBusiness | 4 | 1 |
| /* | — | 1 | 1 |
| / | MedicalBusiness | 1 | 1 |
| /servicios | — | 1 | 0 |

- **Pages by role:** homepage 1 · sample 4
- **Skipped URLs:** budget 13
- **Discovered:** 18 · **Sampled:** 5

## Top actions (13)

| # | Priority | Finding | Status | Sev | Scope | Where | Fix | Recommendation |
|---:|---:|---|---|---:|---|---|---|---|
| 1 | 12 | `M5.article.missing` | fail | 4 | page | / | auto | Add Article JSON-LD to the template using schema/jsonld-templates/article.json. |
| 2 | 6 | `M9.img.no_dimensions` | warn | 3 | page | / | auto | Add width and height attributes (or an aspect-ratio in CSS) matching the file's intrinsic size. |
| 3 | 4 | `M15.cls.unsized_image` | warn | 4 | site | / | advisory | Add intrinsic width and height to the images listed above, then confirm the effect with a real CLS measurement. |
| 4 | 3 | `M10.contextual.too_few_inbody_links` | warn | 3 | page | /contacto-y-ubicacion, /servicios/citopatol… (+1) | proposed | Link from the body copy to the pages this one references, using anchor text that names the destination. |
| 5 | 3 | `M7.title.length_out_of_band` | warn | 3 | page | /, /contacto-y-ubicacion, /preguntas-frecue… | proposed | Shorten the title to about 50-60 characters so the SERP does not truncate it. |
| 6 | 3 | `M7c.outline.skipped_level` | fail | 3 | page | /preguntas-frecuentes | proposed | Renumber the headings so each nested section is exactly one level below its parent. |
| 7 | 2 | `M8.og.missing_image` | fail | 2 | page | /, /contacto-y-ubicacion, /servicios/citopa… (+2) | auto | Add <meta property="og:image" content="<absolute image URL>"> (at least 200×200 px) to the template. |
| 8 | 2 | `M8.twitter.no_card` | warn | 2 | page | /, /contacto-y-ubicacion, /servicios/citopa… (+2) | auto | Add <meta name="twitter:card" content="summary_large_image"> to the template. |
| 9 | 1 | `M22.controls.button_without_name` | warn | 2 | page | /, /contacto-y-ubicacion, /servicios/citopa… (+2) | proposed | Add visible text or an aria-label naming the action the button performs. |
| 10 | 1 | `M7.description.length_out_of_band` | warn | 2 | page | /contacto-y-ubicacion, /preguntas-frecuentes | proposed | Rewrite the description to land inside the band. |
| 11 | 1 | `M21.llmstxt.malformed` | warn | 1 | site | /llms.txt | auto | Fix the structure so a parser can read the sections and links. |
| 12 | 0.67 | `M17.sitemap.lastmod_identical` | warn | 2 | site | /sitemap.xml | advisory | Emit the real per-URL modification date, or omit lastmod entirely — a build timestamp on every URL is worse than none. |
| 13 | 0.67 | `M22.content.iframe_primary` | warn | 2 | page | /contacto-y-ubicacion | advisory | Render the content in the page itself and keep iframes for genuinely embedded third-party widgets. |

Ranked by severity x impact magnitude / effort proxy. Effort proxy: auto 1, proposed 2, advisory 3.

## Coverage and data

- **needs_api:** 5 (Search SEO) · 2 (AI Visibility)
- **manual_review:** 0 (Search SEO) · 0 (AI Visibility)
- **Modules covered:** M4, M5, M7, M8, M9, M10, M14, M15, M17, M20, M21, M22
- **Modules not evaluated (model-judged):** M3, M6, M11, M12, M16, M19
- **Data sources:** render none (static) · PSI needs_api · GSC none

## Warnings

- AI Visibility: coverage 34%: only 34 of 100 always-on weight on the ai axis carried a scored finding, so the band is provisional — unmeasured: Answer Extractability, Fact Density / Original Data, Rendering (non-JS), Entity / Knowledge-Graph and 2 more

## Files

- `C:\Users\SOPORTES JPVM\Documents\web uci vet con seo\runs\unidadveterinaria.pages.dev\2026-09-27T20-14-47Z\report.json`
- `C:\Users\SOPORTES JPVM\Documents\web uci vet con seo\runs\unidadveterinaria.pages.dev\2026-09-27T20-14-47Z\report.md`
- `C:\Users\SOPORTES JPVM\Documents\web uci vet con seo\runs\unidadveterinaria.pages.dev\2026-09-27T20-14-47Z\findings.json`
