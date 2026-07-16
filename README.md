# perfect-ui-skill

A portable Agent Skill that makes production-grade UI design-system discipline reusable across **Codex, Claude Code, Cursor, and Google Antigravity**.

It is not just a visual style prompt. The package includes:

- A strict UI discovery → contract → implementation → verification workflow.
- Rules for tokens, spacing, typography, colors, components, states, responsiveness, accessibility, motion, loading, dashboard/data UX, and performance.
- Existing-project migration guidance.
- A 100-point quality gate and release blockers.
- A safe global/project installer.
- A non-destructive design-system bootstrap script.
- A heuristic static UI audit script.
- Mandatory-use snippets for project/global instruction systems.

## Why one package works across the four tools

The package follows the open Agent Skills `SKILL.md` directory format. Each tool can load the same skill folder on demand. The installation path differs by product.

## Quick install — all tools, global scope

From inside the extracted `perfect-ui-skill` folder:

```bash
python scripts/install_global.py --platform all
```

This copies the skill to:

| Tool | Global location |
|---|---|
| Codex | `~/.agents/skills/perfect-ui-skill/` |
| Claude Code | `~/.claude/skills/perfect-ui-skill/` |
| Cursor | `~/.cursor/skills/perfect-ui-skill/` |
| Antigravity | `~/.gemini/config/skills/perfect-ui-skill/` |
| Antigravity CLI compatibility | `~/.gemini/antigravity-cli/skills/perfect-ui-skill/` |

Use `--force` to replace an older installed copy. Use `--mode symlink` during development so edits to this source folder update every installation; on Windows, copy mode is safer unless symlink support is enabled.

Install for one tool:

```bash
python scripts/install_global.py --platform cursor
python scripts/install_global.py --platform claude
python scripts/install_global.py --platform codex
python scripts/install_global.py --platform antigravity
```

## Project-local install

To commit the skill with a repository:

```bash
python scripts/install_global.py --scope project --project-root /path/to/project --platform all
```

Project locations:

- Codex / Antigravity: `.agents/skills/perfect-ui-skill/`
- Claude Code: `.claude/skills/perfect-ui-skill/`
- Cursor: `.cursor/skills/perfect-ui-skill/`

## Make it mandatory for every UI task

A skill is normally selected when its description matches the task. To make the policy explicit, copy the relevant snippet from `integration/`:

- Codex/project agent instructions: `integration/AGENTS.md.snippet`
- Claude memory/instructions: `integration/CLAUDE.md.snippet`
- Cursor project rule: copy `integration/cursor-perfect-ui.mdc` to `.cursor/rules/perfect-ui.mdc`
- Antigravity global/project Rules: paste `integration/antigravity-rule.md`

The installer intentionally does not edit these instruction files automatically.

## Invoke it

Examples:

```text
Use perfect-ui-skill to audit this existing dashboard and create a phased migration plan before changing code.
```

```text
Use perfect-ui-skill to build this settings page using the existing design system. Include responsive, loading, empty, validation, error, success, keyboard, and reduced-motion behavior, then verify it.
```

```text
Use perfect-ui-skill to bootstrap a design system for this new React Native app without changing the brand assets.
```

Codex can be explicitly invoked with `$perfect-ui-skill`. Claude Code exposes it as `/perfect-ui-skill`. Cursor and Antigravity can select it automatically or when named in the prompt.

## Bootstrap a project design-system baseline

Preview the files it would create:

```bash
python scripts/bootstrap_project.py --root /path/to/project
```

Apply after review:

```bash
python scripts/bootstrap_project.py --root /path/to/project --apply
```

It creates neutral starter documentation/tokens without overwriting existing files. These defaults are not a brand; the agent must adapt them to the actual product and validate contrast.

## Run the static audit

```bash
python scripts/audit_ui.py /path/to/project --format markdown --output perfect-ui-audit.md
```

CI-style threshold example:

```bash
python scripts/audit_ui.py . --fail-on high
```

The scanner flags common risks such as removed focus outlines, clickable non-semantic elements, missing image alt attributes, positive tabindex, large fixed widths, tiny text, huge z-index values, raw colors, `transition: all`, and missing reduced-motion handling. It is heuristic and does not replace rendered/manual accessibility testing.

## Validate the skill package

```bash
python scripts/verify_package.py
```

## Recommended workflow for a new project

1. Install the skill globally or in the repo.
2. Add the mandatory-use instruction snippet.
3. Ask the agent to inspect the stack and product before scaffolding.
4. Run the bootstrap script only after confirming the project has no stronger existing structure.
5. Build representative components/templates with complete states.
6. Verify compact/medium/expanded layouts, keyboard, focus, reduced motion, content extremes, and network states.
7. Keep the token source, component state matrix, and audit record in version control.

## Recommended workflow for an existing project

1. Ask for audit-only mode first.
2. Inventory existing tokens/components and capture current behavior.
3. Fix critical accessibility/data-loss/responsive defects.
4. Introduce semantic token aliases and canonical components.
5. Migrate flow by flow, not through a blind rewrite.
6. Remove compatibility layers only after consumers and tests migrate.

## Important limitation

No prompt or static scanner can guarantee a universally “perfect” UI. This skill makes the process strict, evidence-based, and repeatable; product research, brand decisions, real-device testing, assistive-technology testing, and human review still matter.
