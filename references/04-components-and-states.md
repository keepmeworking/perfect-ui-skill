# Components and States

Every shared component needs a written contract covering purpose, anatomy, variants, props, states, keyboard behavior, accessibility, responsive behavior, themes, motion behavior, and content limits.

Consider: default, hover, focus-visible, active/pressed, selected, disabled, loading, success, warning, error, read-only, offline/stale, and permission-limited.

## Universal component rules

- One interaction concept should map to one canonical component or pattern.
- Native semantics come first; custom controls must reproduce keyboard, focus, name, value, and state behavior.
- State changes must remain understandable without color or motion alone.
- Loading must not change control width or cause layout shift.
- Pointer feedback begins immediately when safe, but the committed action follows the platform/control contract.
- Hover behavior is enhancement, never the only way to reveal essential information.
- Motion must define purpose, frequency, properties, duration/easing or spring behavior, interruption, and reduced-motion fallback.
- Component APIs expose intent/variant, not arbitrary styling escape hatches that fragment the system.

## Buttons and pressables

- Keep stable width while loading and prevent duplicate actions.
- Preserve an accessible name while showing a spinner.
- Use a subtle pointer-down response where appropriate, such as surface change or `scale(0.97)`; do not distort precision controls or cause layout movement.
- Disabled buttons do not fire actions and should explain unavailable conditions nearby when the reason is not obvious.
- Destructive actions require proportionate confirmation, undo, or recovery. Do not use confirmation dialogs for harmless reversible actions.
- Keyboard activation must remain immediate; do not force a decorative entrance/exit delay onto repeated keyboard actions.

## Inputs and forms

- Use persistent labels; placeholders are examples, not labels.
- Errors explain the problem and recovery, remain associated with the field, and preserve entered data.
- Validate at a useful moment. Do not show hostile errors for untouched fields or wait until the end when earlier feedback prevents wasted work.
- Preserve focus and scroll position after validation.
- Announce meaningful asynchronous validation without repeatedly interrupting screen-reader users.
- Mobile inputs should avoid font sizes that trigger unwanted browser zoom.

## Dialogs, sheets, and drawers

- Provide a clear title and purpose.
- Choose deliberate initial focus, contain focus where required, support Escape/back behavior, and restore focus to the trigger.
- Do not lock out input solely because an animation is running.
- Dialogs may remain center-origin; trigger-anchored popovers should use the trigger origin.
- Sheets/drawers that support dragging must track 1:1, capture the pointer, use velocity-aware settling, permit interruption, and respect reduced motion.
- Compact layouts may turn a dialog into a full-screen sheet when the task needs space.

## Menus, popovers, tooltips, tabs, and comboboxes

- Follow established keyboard patterns and focus behavior.
- Menus/popovers/tooltips should preserve the spatial connection to their trigger.
- Tooltips should not contain essential interactive content. Delay the first tooltip enough to avoid accidental activation; adjacent tooltips may appear immediately once the group is active.
- Tabs preserve a predictable active state and focus model; animated indicators must not delay selection.
- Comboboxes clearly distinguish input value, highlighted option, selected value, loading, no results, and error states.

## Lists, tables, and collection components

- Empty data and no search results are different states.
- Preserve item identity with stable keys.
- Added/removed/reordered items must not cause users to lose track of selection or focus.
- Animate collection changes only when frequency and function justify it; sorting/filtering dense operational data usually prioritizes stability.
- Virtualized collections retain accessible position/count information where feasible.

## Loading and skeletons

- Skeletons reflect the final structure and reserve dimensions to avoid layout shift.
- Do not use a skeleton for a tiny local action where an inline progress state is clearer.
- Use determinate progress when measurable.
- Long operations explain what is happening, whether users can leave, and how to recover.

## Component contract checklist

For every new shared component document:

1. Purpose and non-goals.
2. Anatomy and content limits.
3. Variants and sizes.
4. Complete state matrix.
5. Keyboard/focus behavior.
6. Accessible name/description/status behavior.
7. Responsive adaptation.
8. Motion/gesture contract and reduced-motion alternative.
9. Theme/high-contrast behavior.
10. Performance constraints.
11. Test and verification examples.

Do not create a new component when an existing component can satisfy the same interaction concept.
