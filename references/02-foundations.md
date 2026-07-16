# Foundations

## Tokens
Use primitive tokens only to define semantic tokens. Components consume names such as `surface-default`, `text-primary`, `border-muted`, `action-primary`, `status-danger`, never raw hex values.

## Spacing
Use a 4px base scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96. Related items stay closer than unrelated groups. Mobile page gutters default to 16px, tablet 24px, desktop 24–32px.

## Typography
Use one primary UI family and at most one supporting family. Body text should normally be 14–16px, mobile inputs 16px, readable line height 1.4–1.6, and clear role-based hierarchy. Use `rem` on web and tabular numerals for data.

## Color
Target WCAG 2.2 AA contrast. Do not communicate status by color alone. Define light, dark, high-contrast and disabled behavior through semantic tokens.

## Shape and elevation
Keep radius and shadow scales small. Prefer spacing, borders and surfaces before heavy shadows. Define a controlled layering scale for sticky UI, popovers, toasts and modals.

## Icons
Use one icon family, consistent size and stroke. Icon-only actions require accessible names and sufficiently large hit targets.