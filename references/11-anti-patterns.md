# UI Anti-patterns

Flag these during implementation and review:

- Raw hex colors and arbitrary spacing repeated across components.
- Placeholder-only form labels.
- Clickable `div`/`span` instead of native controls.
- Hidden focus outlines.
- Disabled controls without explanation.
- Full-page blocking for a local async action.
- Spinners with no context or timeout.
- Error messages such as “Something went wrong” without recovery.
- Every card using a different radius or shadow.
- Desktop layouts simply scaled down for mobile.
- Tables squeezed until unreadable.
- Color-only status and inaccessible charts.
- `transition: all`, unnecessary parallax and ignored reduced-motion preferences.
- Huge z-index values instead of a layer system.
- One-off components that duplicate an existing interaction.
- Optimistic updates for irreversible or high-risk actions.
- Third-party requests blocking unrelated UI.
- Claims of accessibility based only on a static scanner.