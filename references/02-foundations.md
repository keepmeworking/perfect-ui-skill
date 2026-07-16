# Foundations

## Tokens

Use primitive tokens only to define semantic tokens. Components consume names such as `surface-default`, `text-primary`, `border-muted`, `action-primary`, `status-danger`, never raw hex values.

Keep token layers explicit:

`primitive values → semantic roles → component aliases → component usage`

Include motion, opacity, layering, and focus-ring tokens alongside color, spacing, and typography. A design system is incomplete when animation timings or z-index values remain scattered literals.

## Spacing

Use a 4px base scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96. Related items stay closer than unrelated groups. Mobile page gutters default to 16px, tablet 24px, desktop 24–32px.

Spacing communicates relationship. Label-to-control spacing should be smaller than field-to-field spacing; component-to-component spacing should be smaller than section-to-section spacing.

Use `rem`/`em` where spacing should scale with text. Fixed pixel spacing must not cause layouts to collapse when users enlarge type.

## Typography

Use one primary UI family and at most one supporting family. Prefer a platform/system UI font unless the brand has a reason for a custom face. Body text should normally be 14–16px, mobile inputs 16px, readable line height 1.4–1.6, and clear role-based hierarchy. Use `rem` on web and tabular numerals for data.

Typography is a coordinated system of size, weight, line height, tracking, and width—not size alone.

- Large display text generally needs tighter line height and slightly negative tracking.
- Small text may need more open tracking and generous line height.
- Do not use one `letter-spacing` value across all sizes.
- Enable optical sizing when the font supports it: `font-optical-sizing: auto`.
- Use `clamp()` carefully for fluid display type; verify long headings and localization.
- Respect user text scaling and Dynamic Type; the layout must grow with text.
- Avoid ultra-light weights on small text and translucent surfaces.

Example:

```css
:root {
  font: 100%/1.5 system-ui, sans-serif;
}

.display {
  font-size: clamp(2rem, 5vw, 4rem);
  line-height: 1.05;
  letter-spacing: -0.02em;
  font-optical-sizing: auto;
}
```

## Color

Target WCAG 2.2 AA contrast. Do not communicate status by color alone. Define light, dark, high-contrast, selected, hover, active, and disabled behavior through semantic tokens.

Do not make disabled text so faint that users cannot understand what is unavailable. A disabled state may be exempt from some contrast requirements, but it still needs legible purpose and context.

## Shape and elevation

Keep radius and shadow scales small. Prefer spacing, borders and surfaces before heavy shadows. Define a controlled layering scale for sticky UI, popovers, toasts and modals.

Elevation must represent behavior and hierarchy, not decorative variety. A floating surface should have a consistent relationship to the layer beneath it across the product.

## Translucent materials

Use blur/translucency only when it communicates a floating layer and content actually passes beneath it.

- Avoid stacking multiple light translucent surfaces.
- Provide solid alternatives for `prefers-reduced-transparency`.
- Provide stronger borders/backgrounds for `prefers-contrast: more`.
- Ensure text remains legible over every realistic background.
- Test blur performance on mobile/Safari-class devices.
- A blocking dialog normally uses a scrim; a parallel non-blocking panel may use separation without a scrim.

## Icons

Use one icon family, consistent size and stroke. Icon-only actions require accessible names and sufficiently large hit targets.

Align icons optically, not only mathematically. Similar-looking actions must use the same symbol and behavior across the product. Do not invent ambiguous icons where a text label is clearer.
