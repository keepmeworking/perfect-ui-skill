# Operating Protocol

Use this sequence for every UI task.

## 1. Discover
Inspect the product goal, users, framework, styling stack, tokens, shared components, routes, supported themes, breakpoints, accessibility utilities, tests, and nearby patterns. Do not start by replacing the current UI.

## 2. Inventory
Record the existing foundations, reusable components, duplicate implementations, interaction states, responsive behavior, and known defects. Separate objective issues from subjective preferences.

## 3. Define the UI contract
Document the user goal, hierarchy, primary action, reuse plan, states, responsive adaptation, accessibility behavior, performance risks, and acceptance checks.

## 4. Implement through the system
Work in this order: foundations → semantic tokens → primitives → components → patterns → templates → screens. Reuse before creating. Avoid one-off visual values.

## 5. Verify
Run format, lint, type, tests, and build. Inspect compact, medium, and expanded layouts; keyboard flow; visible focus; 200% zoom; reduced motion; long content; loading, empty, error, success, stale and permission states.

## 6. Report
State what changed, what was reused or added, what was verified, and what remains. Never claim complete accessibility or perfection without evidence.