# Version 1.0.1 — global navigation and page completion

The current live theme was audited read-only on 27 October 2026. Its product gallery and native 275 SAR HONTON price rendered correctly, but both global section tags failed because the delivered `settings_data.json` lacked saved header/footer registrations. The homepage is independently overridden by an older Page Builder page. The source ZIP is corrected; no live dashboard changes were possible because the tagged YouCan connector exposed no callable tools.

## Corrected in the source

- Registered both global sections with native `type/settings/blocks/order` configuration; supplied a minimal additive registry patch and a local merge helper that preserves unrelated settings and app embeds.
- Added consistent branded/sticky desktop and mobile navigation, eight primary category links and five nested subcategories, native search and cart links, logo, and a footer with all eight real information destinations and the verified contact email.
- Preserved all existing information/legal page slugs and page.content; added Contact labels without changing native form POST/session/captcha mechanisms.
- Added per-page metadata/title fallbacks and safe structured-data quoting.
- Corrected native selected-variant defaults, zero-stock/quantity checks, safe query rendering, unknown sort values and pagination bounds.
- Extended local previews to all 13 actual category routes using each category's actual observed products. There are 213 first-page rows with overlap across categories; this is not a count of unique products or the complete admin catalog.
- Added global-registry regressions and strict preview behavior, so missing platform-required saved data is detected before delivery.

## Still requires store access

Apply/merge the corrected global configuration to the unpublished installed theme, resolve the Page Builder homepage assignment, run the authenticated YouCan check and isolated checkout tests, then preview all pages before publication. Existing category-product assignments are used directly; no duplicate category or policy pages should be created. See APPLY_HEADER_FOOTER_FIX.md.

No product prices, SKUs, variants, inventory, suppliers, fulfillment, checkout configuration, legal text or pixel configuration was written. No order was placed. GitHub delivery of the corrected artifact does not constitute a storefront deployment.
