# Quality Gates

Score production UI out of 100:

- Task clarity and hierarchy: 10
- Design-system consistency: 15
- Responsive/adaptive behavior: 15
- Accessibility: 20
- States and feedback: 10
- Forms and interaction safety: 10
- Performance and stability: 10
- Verification and maintainability: 10

Recommended production threshold: 90/100 with no critical blocker.

Block release when a primary flow cannot be completed, focus is lost or hidden, contrast fails, data can be lost unexpectedly, responsive layout breaks, required network states are absent, reduced motion is ignored, or rendered verification was skipped.

Evidence should include commands run, viewports checked, keyboard/focus results, state coverage, known limitations and affected components. A passing build alone is not sufficient.