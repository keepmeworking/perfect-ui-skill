---
name: perfect-ui-skill
description: Enforces and implements a production-grade UI design system for any new or existing web, mobile, desktop, dashboard, SaaS, or cross-device product. Use whenever creating, changing, reviewing, refactoring, or auditing UI/UX, components, layouts, pages, design tokens, styling, responsive behavior, accessibility, forms, tables, navigation, states, animation, theming, or frontend visual code. Do not use for backend-only work with no user-interface impact.
---

# Perfect UI Skill

## Mission

Create interfaces that are coherent, accessible, responsive, performant, predictable, and maintainable. “Perfect” means the UI follows a deliberate system and passes objective quality gates; it does not mean adding decoration or forcing every product to look the same.

This skill applies to:

- New products and new design systems.
- Existing products that need gradual UI cleanup or redesign.
- Individual pages, flows, components, dashboards, mobile screens, and desktop interfaces.
- Visual implementation, interaction behavior, accessibility, responsive behavior, loading/error states, and UI performance.

## Non-negotiable operating rules

1. **Inspect before designing.** Never replace an existing brand, component library, token system, or interaction pattern without first mapping it.
2. **System before screens.** Establish or reuse foundations, semantic tokens, components, and patterns before producing one-off page styling.
3. **No arbitrary styling.** Avoid unexplained colors, spacing, font sizes, radii, shadows, breakpoints, z-index values, and animation timings.
4. **Every interactive element has complete states.** At minimum consider default, hover where applicable, focus-visible, active/pressed, selected, disabled, loading, success, error, and read-only where applicable.
5. **Accessibility is a release requirement.** Target WCAG 2.2 AA, native semantics, keyboard operation, visible focus, readable contrast, zoom/reflow, reduced motion, and accessible names.
6. **Responsive means adaptation, not shrinking.** Re-prioritize, reflow, collapse, scroll, disclose, or change navigation patterns according to available space and input method.
7. **Preserve user intent and data.** Loading, errors, retries, optimistic updates, autosave, destructive actions, and navigation must not surprise users or discard work.
8. **Performance is part of UX.** Prevent layout shift, unnecessary blocking, oversized payloads, unoptimized assets, repeated requests, and heavy animation.
9. **Verify the rendered interface.** A build passing is not enough. Test representative viewports, keyboard flow, states, content extremes, and reduced-motion behavior.
10. **Do not claim perfection without evidence.** Report what was verified, what remains, and any constraints.

## Source-of-truth order

When rules conflict, follow this order:

1. Explicit user/product requirements.
2. Existing approved brand guidelines and product design system.
3. Existing reusable components and established product patterns.
4. Platform conventions and accessibility requirements.
5. This skill’s defaults.

Do not impose this skill’s visual defaults over a valid product identity. Use the skill to improve consistency and behavior while preserving the brand.

## Select the operating mode

### Mode A — Bootstrap a new project

Use when no reliable UI system exists.

1. Inspect the product brief, users, platforms, content density, brand assets, and technical stack.
2. Define foundations and semantic tokens.
3. Establish layout primitives and responsive strategy.
4. Build core components with complete state contracts.
5. Create representative templates before expanding the component catalog.
6. Add project documentation and quality gates.

Read:
- `references/02-foundations.md`
- `references/03-responsive-layout.md`
- `references/04-components-and-states.md`
- `references/05-accessibility.md`
- `references/09-quality-gates.md`

### Mode B — Retrofit an existing project

Use when a live UI already exists.

1. Inventory tokens, styles, component libraries, routes/screens, patterns, and duplicated UI.
2. Capture current behavior before changing it.
3. Identify critical usability/accessibility defects separately from visual inconsistency.
4. Create a mapping from legacy values/components to target tokens/components.
5. Migrate incrementally, keeping compatibility adapters where necessary.
6. Verify regressions at every phase; avoid a blind big-bang rewrite.

Read:
- `references/01-operating-protocol.md`
- `references/08-existing-project-migration.md`
- `references/09-quality-gates.md`

### Mode C — Build or change a feature/component

Use for normal product work.

1. Read the project’s design-system documentation and inspect nearby components.
2. Reuse an existing component/pattern when it satisfies the need.
3. If a new component is necessary, define its API, variants, states, responsive behavior, accessibility, and content limits before implementation.
4. Use semantic tokens, not raw visual values.
5. Test all relevant states and representative viewport/input combinations.
6. Update the component documentation or state matrix.

Read only the references relevant to the task.

### Mode D — Audit only

Use when the user wants findings rather than code changes.

1. Run the static audit script when applicable:
   `python scripts/audit_ui.py <project-root> --format markdown --output perfect-ui-audit.md`
2. Manually inspect architecture, rendered screens, keyboard behavior, content extremes, states, and responsive behavior.
3. Classify findings as critical, high, medium, or low.
4. Separate objective defects from subjective visual suggestions.
5. Provide a prioritized remediation plan with evidence and affected files/components.

## Required workflow for every UI task

### 1. Discover

Inspect, as relevant:

- Framework, rendering model, styling approach, component library, icon set, form library, charting library, and test setup.
- Existing token/theme files and global styles.
- Shared layout and component directories.
- Existing accessibility utilities.
- Relevant routes/screens and their states.
- Product brand assets and content requirements.
- Existing responsive breakpoints and supported devices.

Do not begin by generating a generic replacement UI.

### 2. Define the contract

Before implementation, state or infer:

- User goal and primary action.
- Information hierarchy.
- Component/pattern reuse plan.
- Responsive behavior.
- State behavior: loading, empty, error, success, offline/stale, disabled, permission-limited.
- Accessibility behavior: semantics, keyboard, focus, labels, announcements.
- Performance risks.
- Acceptance checks.

For a small change, this can be concise. For a large feature, persist it in project documentation.

### 3. Implement through system primitives

Use this hierarchy:

`foundations → semantic tokens → primitives → components → patterns → templates → screens`

Rules:

- Prefer semantic token names such as `text-primary`, `surface-raised`, and `border-danger` over color names inside components.
- Keep visual values centralized and themeable.
- Reuse one component for one interaction concept; do not create near-duplicates merely to match one mockup.
- Separate component behavior from product content.
- Use native controls and semantics unless a custom implementation is necessary.
- Keep DOM/view hierarchy simple and predictable.
- Preserve platform conventions for navigation, gestures, focus, back behavior, and safe areas.

### 4. Verify

Run all relevant checks available in the repository:

- Format, lint, type-check, unit/component tests, and production build.
- Visual or screenshot tests when configured.
- Browser/device verification at compact, medium, and expanded widths appropriate to the product.
- Keyboard-only path.
- Focus order and focus visibility.
- 200% zoom and narrow-width reflow for web interfaces.
- Reduced-motion mode.
- Light/dark/high-contrast themes when supported.
- Long labels, validation messages, empty data, large data, slow responses, and failure states.
- Touch/pointer target size and spacing.
- Layout stability and obvious performance regressions.

Do not silently skip a failed check. Fix it or report the exact limitation.

### 5. Report

Conclude with:

- What changed.
- Which system rules/components/tokens were added or reused.
- What was verified and how.
- Remaining risks or follow-up work.

Avoid claiming that a UI is “fully accessible” based only on static analysis.

## Mandatory design-system artifacts

For a project with ongoing UI development, maintain equivalents of:

- Design-system overview and ownership.
- Token source of truth.
- Typography and spacing rules.
- Responsive layout rules.
- Component catalog and state matrix.
- Accessibility requirements.
- Motion and feedback rules.
- Content and validation patterns.
- Quality gate/audit record.

Adapt paths to the repository. Suggested starting structure:

```text
docs/design-system/
  README.md
  component-state-matrix.md
  accessibility.md
  responsive.md
src/styles/ or app/theme/
  tokens.*
  themes.*
```

Use `scripts/bootstrap_project.py` as an optional non-destructive scaffold.

## UI quality stop conditions

Do not mark UI work complete while any applicable condition remains:

- A primary flow cannot be completed with keyboard or assistive semantics.
- Focus is hidden, trapped incorrectly, or lost after an action.
- Text/UI contrast fails required levels.
- The layout requires unintended horizontal scrolling at supported narrow widths.
- A destructive action is ambiguous or loses data without warning/recovery.
- A network-dependent action has no loading/failure/retry behavior.
- A component lacks required states.
- Raw visual values are repeatedly duplicated instead of tokenized.
- A new component duplicates an existing interaction pattern without justification.
- The interface breaks with realistic long content, empty content, or validation errors.
- Motion ignores reduced-motion preferences.
- A slow dependency blocks unrelated UI without necessity.
- Verification was not performed on the rendered UI when tools permit it.

## Reference loading map

Read only what is needed to control context size:

- End-to-end procedure: `references/01-operating-protocol.md`
- Tokens, color, spacing, type, radius, elevation: `references/02-foundations.md`
- Responsive/adaptive layout: `references/03-responsive-layout.md`
- Components, variants, and states: `references/04-components-and-states.md`
- Accessibility: `references/05-accessibility.md`
- Motion, feedback, loading, and performance: `references/06-motion-feedback-performance.md`
- Dashboard/data-heavy UX: `references/07-dashboard-data-ux.md`
- Existing-project migration: `references/08-existing-project-migration.md`
- Audit scorecard and release gates: `references/09-quality-gates.md`
- Stack-specific implementation guidance: `references/10-stack-adapters.md`
- Anti-patterns and review heuristics: `references/11-anti-patterns.md`

## Final principle

The goal is not to produce a fashionable screenshot. The goal is to leave the project with a UI system that future contributors and agents can understand, extend, test, and consistently follow.
