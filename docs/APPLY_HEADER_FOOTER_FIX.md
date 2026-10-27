# Apply the global navigation and page fix

The current public store was inspected on 27 October 2026. The installed modular layout shows `global section data not found` in both global positions on product, category and information pages. The homepage is still the separate `dj26-home` Page Builder composition. No dashboard edits or publication were performed from this chat: the tagged YouCan connector exposed no callable store tools.

## Correct the installed theme without resetting its settings

The corrected source is version **1.0.1**. It registers `dj-header` and `dj-footer` in the native global-section registry and includes editable navigation for eight primary categories, five existing subcategories and all eight current information pages.

1. Export/duplicate the currently installed theme and Page Builder settings to preserve a rollback. Work on an unpublished copy or the supported preview of that theme.
2. Update the theme source files from the corrected ZIP through the supported theme editor/import workflow for this store. Retain its products, variants, prices, checkout, supplier integrations, pixels, app embeds and policy data.
3. In the installed theme's `config/settings_data.json`, merge the two entries in `global-sections-patch.json` into the **active** `current.sections` object. If `current` is a preset name, use that named preset's `sections`. Register by `type`: `dj-header` and `dj-footer`. Do not replace the full settings file with a shortened example, discard other sections, or remove existing `blocks` app embeds.
4. For a locally exported installed configuration, prepare a separate merged file:

```sh
python tools/merge-global-sections.py exported-settings_data.json corrected-settings_data.json
```

The helper preserves unrelated settings/app embeds and existing header/footer customizations. Review the separate output, especially navigation blocks, before saving it to the unpublished theme. `docs/global-sections-patch.json` contains `sections_to_merge` as a patch wrapper; merge its contents, not the wrapper key, into the actual theme file.

5. Preview product, collection directory, all category routes, search, cart and information pages. The visible Liquid errors must disappear and a real `<header>` and `<footer>` must render. Confirm the mobile menu, nested category links, search, cart and footer policy links.

## Give the homepage the same header and footer

A theme ZIP update alone does not remove the current Page Builder homepage override. In a safe unpublished preview, use the supported homepage assignment control to select the theme's native homepage/index. Confirm the original family image is first below the header and the circular photographic category navigation immediately follows. The product selectors must resolve to real YouCan products, with prices read natively.

If the existing store must keep Page Builder, use `classic/dist/00-header.html`, `99-footer.html` and `header-footer.css` only in **supported global header/footer slots** so they appear across the relevant pages. Inserting them in one page body is not a site-wide fix. Keep native product and collection widgets for titles, availability, media, variants and prices. If no supported global slots exist, use the native modular-theme homepage rather than a DOM-injection script.

## Category and information pages

No duplicate categories or policy pages are needed. The eight main categories and five subcategories already exist and have native products assigned. `templates/collection.json` renders the current route's `collection.products`, with native sorting/pagination and subcategories. Product membership and catalog prices are not changed by the theme. `store-pages-manifest.json` records every existing route.

All eight information routes keep their original slugs and content. The FAQ receives accessible disclosure presentation; the native Contact form gains field labels without changing its POST endpoint, session/captcha, or validation. Existing returns, privacy and terms text stays authoritative. Do not create new `/shipping` or `/how-to-order` duplicates in the live store.

## Validate and release

Run local tests and the authenticated YouCan check on the unpublished theme. Verify actual products and prices, zero-stock behavior, variant preselection, safe search text, sorting, pagination limits, information-page links, contact validation, mobile focus and image loading. Use an isolated store with production fulfillment disabled for order/checkout tests. Never send a test order to Taager production.

Publish only after the real preview passes and the owner approves it. If there is a regression, restore the previous theme/homepage assignment and its exported configuration; do not restore catalog prices or change supplier/checkout/pixel settings.
