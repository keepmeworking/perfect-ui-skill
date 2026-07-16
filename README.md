# perfect-ui-skill

A portable, production-grade **single primary UI skill** for Codex, Claude Code, Cursor, and Google Antigravity.

It covers the complete UI lifecycle without requiring separate skills for animation, review, accessibility, dashboards, migration, or planning:

- New-project design-system bootstrap.
- Existing-project retrofit and phased migration.
- Feature/component implementation.
- Focused UI review with an explicit verdict.
- Codebase-wide audit with `quick`, `standard`, and `deep` effort levels.
- Self-contained implementation plans that another agent can execute.
- Motion/gesture review and high-restraint opportunity discovery.
- Accessibility, responsive behavior, states, async UX, dashboards, performance, and verification.
- A heuristic static scanner, bootstrap script, installer, templates, and CI validation.

The core workflow is:

`discover → define contract → implement through system primitives → verify rendered UI → report evidence`

## Why one skill

The repository keeps all specialist knowledge as references and operating modes behind one `SKILL.md`. You maintain and install only `perfect-ui-skill`; the agent loads the relevant reference based on the task.

Examples:

```text
Use perfect-ui-skill audit quick on the checkout flow.
```

```text
Use perfect-ui-skill motion review on this drawer and block any non-interruptible gesture behavior.
```

```text
Use perfect-ui-skill opportunities on this dashboard. Be strict and include rejected ideas.
```

```text
Use perfect-ui-skill plan the top three findings, then execute plan 001.
```

## Package highlights

- Strict source-of-truth and inspect-before-design rules.
- Semantic design tokens for color, typography, spacing, motion, focus, and layering.
- Complete component state and motion contracts.
- WCAG 2.2 AA target and native-platform equivalents.
- Adaptive mobile/tablet/desktop behavior rather than scaled desktop layouts.
- Purpose/frequency-based motion decisions.
- Origin-aware surfaces, immediate press feedback, interruptible motion, velocity handoff, momentum projection, and rubber-banding guidance.
- Required review tables, severity, evidence, and approve/block verdicts.
- Audit-to-plan workflow with self-contained execution plans.
- 100-point quality score and release stop conditions.

## Global install

Clone or download the repository, then run from its root:

```bash
python scripts/install_global.py --platform all
```

This installs to:

| Tool | Global location |
|---|---|
| Codex | `~/.agents/skills/perfect-ui-skill/` |
| Claude Code | `~/.claude/skills/perfect-ui-skill/` |
| Cursor | `~/.cursor/skills/perfect-ui-skill/` |
| Antigravity | `~/.gemini/config/skills/perfect-ui-skill/` |
| Antigravity CLI compatibility | `~/.gemini/antigravity-cli/skills/perfect-ui-skill/` |

Use `--force` to replace an older installed copy. During development, `--mode symlink` keeps installed copies linked to this repository; Windows users should normally use copy mode unless symlink support is enabled.

Install for one tool:

```bash
python scripts/install_global.py --platform cursor
python scripts/install_global.py --platform claude
python scripts/install_global.py --platform codex
python scripts/install_global.py --platform antigravity
```

## Project-local install

```bash
python scripts/install_global.py \
  --scope project \
  --project-root /path/to/project \
  --platform all
```

Project locations:

- Codex / Antigravity: `.agents/skills/perfect-ui-skill/`
- Claude Code: `.claude/skills/perfect-ui-skill/`
- Cursor: `.cursor/skills/perfect-ui-skill/`

## Make it mandatory for UI work

Copy the relevant instruction from `integration/`:

- Codex/project agents: `integration/AGENTS.md.snippet`
- Claude Code: `integration/CLAUDE.md.snippet`
- Cursor: copy `integration/cursor-perfect-ui.mdc` to `.cursor/rules/perfect-ui.mdc`
- Antigravity: paste `integration/antigravity-rule.md` into global or project rules

The installer deliberately does not edit instruction files automatically.

## Main invocation modes

| Invocation | Result |
|---|---|
| `bootstrap` | Create/adapt a new design-system foundation |
| `retrofit` | Map and migrate an existing UI incrementally |
| `build` | Implement a feature/component with complete states |
| `review` | Focused UI review with evidence and verdict |
| `audit quick` | High-traffic, high-severity review |
| `audit standard` | Full interactive-product audit |
| `audit deep` | Whole-product audit including lower-priority polish |
| `plan <finding>` | Write one self-contained execution plan |
| `opportunities` | Find only high-conviction polish/motion opportunities |
| `motion review` | Strict motion/gesture review |
| `execute <plan>` | Implement and verify a selected plan |
| `reconcile plans` | Refresh status and stale references |

Codex can be explicitly invoked with `$perfect-ui-skill`. Claude Code exposes it as `/perfect-ui-skill`. Cursor and Antigravity can select it automatically or when named.

## Bootstrap a project baseline

Preview:

```bash
python scripts/bootstrap_project.py --root /path/to/project
```

Apply:

```bash
python scripts/bootstrap_project.py --root /path/to/project --apply
```

The scaffold is non-destructive by default and creates/adapts:

```text
perfect-ui.config.yaml
docs/design-system/
  README.md
  component-state-matrix.md
  motion.md
  ui-audit-report.md
  tokens.example.json
plans/ui/
  README.md
src/styles/ or equivalent/
  perfect-ui.tokens.css
```

Neutral defaults are not approved branding. The agent must adapt them to the actual product and verify contrast, text scaling, and states.

## Static audit

```bash
python scripts/audit_ui.py /path/to/project \
  --format markdown \
  --output perfect-ui-audit.md
```

Motion-only sweep:

```bash
python scripts/audit_ui.py . --category motion
```

CI threshold:

```bash
python scripts/audit_ui.py . --fail-on high
```

The scanner flags heuristics such as hidden focus, clickable non-semantic elements, missing image alt, positive tabindex, tiny text, raw colors, fixed widths, `transition: all`, `ease-in`, `scale(0)`, long/infinite motion, layout-property transitions, missing reduced-motion handling, and ungated hover motion.

Static findings may be false positives and never replace rendered, keyboard, screen-reader, real-device, or performance verification.

## Validate the package

```bash
python scripts/verify_package.py
python -m unittest discover -s tests -v
```

## Recommended new-project workflow

1. Install the skill globally or in the repository.
2. Add the mandatory-use rule.
3. Ask the agent to inspect the product, users, stack, and brand before scaffolding.
4. Run the bootstrap only when no stronger project system exists.
5. Build representative components/templates with complete state and motion contracts.
6. Verify compact/medium/expanded layouts, keyboard, focus, text scaling, content extremes, network states, reduced motion, and input methods.
7. Keep tokens, component matrix, motion rules, plans, and audit evidence in version control.

## Recommended existing-project workflow

1. Start with `audit quick` or `audit standard` in read-only mode.
2. Inventory tokens, components, states, motion conventions, and critical flows.
3. Fix blockers before visual polish.
4. Create semantic aliases and canonical components.
5. Generate self-contained plans for selected findings.
6. Migrate flow by flow and verify every phase.
7. Remove compatibility layers only after consumers and tests migrate.

## License and attribution

This project is MIT licensed. Motion-craft and audit-workflow ideas adapted from Emil Kowalski’s MIT-licensed `emilkowalski/skills` repository are credited in `THIRD_PARTY_NOTICES.md`.

## Important limitation

No prompt or static scanner can guarantee a universally perfect UI. Product research, brand decisions, real-device testing, assistive-technology testing, performance profiling, and human judgment remain necessary. This skill makes those expectations explicit, repeatable, and difficult for an agent to skip.
