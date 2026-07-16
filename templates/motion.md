# Project Motion and Gesture Rules

## Product personality

- Desired feel: crisp / calm / playful / expressive / other
- High-frequency interactions:
- Rare delight moments:
- Gesture-driven surfaces:
- Supported reduced-motion/transparency/contrast modes:

## Tokens

| Token | Value | Use |
|---|---:|---|
| `--motion-duration-press` | | Press/tap feedback |
| `--motion-duration-control` | | Dropdowns, selects, small state changes |
| `--motion-duration-surface` | | Dialogs, drawers, sheets |
| `--motion-ease-out` | | Enter/exit and immediate UI response |
| `--motion-ease-in-out` | | On-screen movement/morphing |
| `--motion-ease-drawer` | | Drawer/sheet settling |

## Decision rules

- What frequency tiers receive no motion?
- Which purposes are allowed?
- Which properties may animate?
- Maximum normal-product duration:
- When are springs allowed?
- How is hover motion gated?
- Reduced-motion replacement:

## Component motion contracts

| Component | Purpose | Frequency | Enter/exit | Press | Gesture/interruptibility | Reduced motion |
|---|---|---|---|---|---|---|
| | | | | | | |

## Verification

- Slow-motion/frame review:
- Busy-main-thread test:
- Real-device gesture test:
- Interruption/reversal test:
- Reduced motion:
- Reduced transparency/high contrast:
