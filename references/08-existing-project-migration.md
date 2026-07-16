# Existing Project Migration

Avoid a big-bang redesign.

1. Capture the current routes, states, screenshots and critical flows.
2. Inventory raw values, tokens, component libraries and duplicate components.
3. Classify defects: critical accessibility/data-loss, high usability/responsive, system inconsistency and optional visual polish.
4. Introduce semantic aliases around existing values before changing the brand.
5. Create canonical components and compatibility adapters.
6. Migrate flow by flow, beginning with high-frequency or high-risk areas.
7. Add tests and visual evidence before removing legacy code.
8. Remove old tokens/components only after all consumers migrate.

Preserve API behavior, analytics, focus behavior, URLs, content and user data. Track legacy-to-target mappings and deprecations explicitly.