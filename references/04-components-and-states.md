# Components and States

Every shared component needs a written contract covering purpose, anatomy, variants, props, states, keyboard behavior, accessibility, responsive behavior, themes and content limits.

Consider: default, hover, focus-visible, active, selected, disabled, loading, success, warning, error and read-only.

Core requirements:
- Buttons keep stable width while loading and prevent duplicate actions.
- Inputs use persistent labels; placeholders are examples, not labels.
- Errors explain the problem and recovery, remain associated with the field and preserve entered data.
- Dialogs have a clear title, deliberate initial focus, focus containment, Escape behavior and focus restoration.
- Menus, tabs, comboboxes and grids follow established keyboard patterns.
- Empty data and no search results are different states.
- Skeletons should reflect the final structure and avoid layout shift.
- Destructive actions require proportionate confirmation, undo or recovery.

Do not create a new component when an existing component can satisfy the same interaction concept.