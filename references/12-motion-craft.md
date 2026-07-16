# Motion Craft, Gestures, and Interaction Feel

Motion is part of the interaction contract, not decoration added after layout. The correct default is restraint: motion must improve feedback, orientation, continuity, comprehension, or perceived responsiveness. When it does none of those, remove it.

## 1. Motion decision gate

Run every proposed animation through these questions in order.

### Frequency

| Expected frequency | Default decision |
| --- | --- |
| 100+ times/day or keyboard-initiated | Instant; normally no animation |
| Tens of times/day | None or near-imperceptible feedback |
| Occasional: dialogs, drawers, toasts | Standard short motion |
| Rare/first-time: onboarding, completion, celebration | May use a measured delight budget |

The more often an interaction occurs, the less motion it can tolerate. Do not make command palettes, keyboard shortcuts, focus jumps, or core navigation wait for an animation.

### Purpose

An animation must name at least one purpose:

- **Feedback:** confirm that input was received.
- **Spatial continuity:** show where a surface came from or where it went.
- **State indication:** make a state change understandable.
- **Explanation:** demonstrate how a feature works, usually in onboarding or marketing.
- **Jarring-change prevention:** bridge content appearing, disappearing, or moving.
- **Delight:** reserved for rare, emotionally meaningful moments.

“It looks cool” is not a sufficient purpose for frequently used product UI.

### Function

Do not animate information the user is actively reading or acting on merely for style. Dense dashboards, financial charts, tables, and operational controls need stability. Decorative motion belongs primarily in low-frequency or non-functional surfaces.

### Budget

The motion must fit a short response budget. If the idea only works as a slow showpiece, reject it for normal product UI.

## 2. Timing and easing system

Centralize motion values as tokens. Adapt to the product’s existing conventions rather than creating a parallel scale.

```css
:root {
  --motion-duration-press: 120ms;
  --motion-duration-tooltip: 150ms;
  --motion-duration-control: 180ms;
  --motion-duration-surface: 240ms;

  --motion-ease-out: cubic-bezier(0.23, 1, 0.32, 1);
  --motion-ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
  --motion-ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
}
```

Use this decision order:

- Entering or exiting in response to the user → strong `ease-out`.
- An element already on screen moving or morphing → `ease-in-out`.
- Hover, color, and subtle emphasis → standard `ease` or a restrained project token.
- Constant-speed progress, marquee, or rotation → `linear`.
- Avoid `ease-in` for normal UI response because it withholds visible movement at the moment the user expects feedback.

Practical budgets:

| Interaction | Typical budget |
| --- | --- |
| Press/tap feedback | 100–160ms |
| Tooltip/small popover | 125–200ms |
| Dropdown/select | 150–250ms |
| Dialog/drawer/sheet | 200–300ms for normal product UI; longer only with evidence |
| Marketing/explanatory sequence | May be longer, but must not block interaction |

Do not treat numbers as laws divorced from feel. Test the rendered result. The key constraint is immediate response and no unnecessary waiting.

## 3. Physicality and origin

### Press feedback

Pressable surfaces should acknowledge pointer-down immediately when a scale response is appropriate.

```css
.pressable {
  transition: transform var(--motion-duration-press) var(--motion-ease-out);
}

.pressable:active {
  transform: scale(0.97);
}
```

Keep scale subtle, usually `0.95–0.98`. Do not apply scale to controls where resizing causes layout, text-rendering, or precision problems. A color/surface response may be better.

### Entrances

Do not animate from `scale(0)`. It makes the element appear from nothing. Start close to the final size and combine with opacity.

```css
.popover {
  opacity: 1;
  transform: scale(1);
  transition:
    opacity 160ms var(--motion-ease-out),
    transform 160ms var(--motion-ease-out);

  @starting-style {
    opacity: 0;
    transform: scale(0.96);
  }
}
```

### Origin-aware surfaces

Popover, menu, and tooltip motion should originate from the trigger or anchor. Dialogs are different: a viewport-centered dialog may remain center-origin because it is not spatially attached to a single trigger.

```css
/* Radix-style example */
.popover {
  transform-origin: var(--radix-popover-content-transform-origin);
}
```

Enter and exit along the same spatial path. A panel that enters from the right should normally leave to the right.

## 4. Interruptibility

Rapidly retriggered and gesture-driven motion must continue from its current on-screen state rather than restarting from an old logical state.

- Prefer CSS transitions for simple state changes that can retarget smoothly.
- Prefer springs or an interruptible animation API for drag, swipe, momentum, and elements that can be grabbed mid-flight.
- Avoid keyframes for rapidly repeated toggles, toasts, or gesture settling when restarting would cause a jump.
- Never lock input only because a transition is playing.
- On reversal, preserve velocity when the animation system supports it.

For predetermined entry/exit motion, CSS transitions or WAAPI are usually simpler and more resilient than a runtime animation library. Use JavaScript when the target, velocity, or trajectory is genuinely dynamic.

## 5. Direct manipulation and gesture rules

A touched or dragged object should feel attached to the input.

- Give feedback on pointer-down; commit the action on release when appropriate.
- Use Pointer Events and `setPointerCapture()` so tracking continues outside the original bounds.
- Preserve the grab offset; do not snap the object’s center under the pointer.
- Track recent position/time samples so release velocity is reliable.
- Apply a small movement threshold before deciding that a tap became a drag.
- Ignore extra touch points after a drag starts unless multi-touch is intentionally supported.
- Permit cancellation by reversing or dragging away when the platform pattern allows it.

### Velocity handoff

When a drag ends, the settling animation should begin with the release velocity. A hard reset to zero velocity creates a visible seam.

### Momentum projection

Choose the resting target using both position and velocity, not position alone.

```js
function project(initialVelocity, decelerationRate = 0.998) {
  return (initialVelocity / 1000) * decelerationRate / (1 - decelerationRate);
}

const projected = currentPosition + project(releaseVelocity);
const target = nearestSnapPoint(projected);
```

Then animate toward `target` while carrying `releaseVelocity` into the spring or inertia system.

### Rubber-banding

At a boundary, increase resistance progressively rather than stopping dead.

```js
function rubberband(overshoot, dimension, constant = 0.55) {
  return (overshoot * dimension * constant) /
    (dimension + constant * Math.abs(overshoot));
}
```

Use real-device testing for drawers, carousels, reordering, and swipe-to-dismiss. Desktop emulation is insufficient for gesture feel.

## 6. Springs

Use springs where continuity, velocity, interruption, or physical manipulation matter. Do not add bounce simply because a spring API is available.

Safe starting points:

```js
// Crisp default: no overshoot
{ type: 'spring', duration: 0.4, bounce: 0 }

// Momentum-driven interaction: slight overshoot
{ type: 'spring', duration: 0.4, bounce: 0.2 }
```

Guidelines:

- Default product UI to critically damped or nearly non-bouncy motion.
- Reserve bounce for motion that inherited momentum from a flick, drag, throw, or playful product personality.
- Keep bounce subtle, commonly `0.1–0.3`.
- Use independent X and Y behavior when their velocities differ.
- Test interruption: start, reverse, grab mid-flight, release again.

## 7. Performance

Prefer motion that remains smooth while the application is busy.

- Animate `transform` and `opacity` by default.
- Avoid per-frame animation of layout properties such as `width`, `height`, `margin`, `padding`, `top`, and `left` when an alternative interaction or transform can achieve the result.
- Do not use `transition: all`.
- Do not update a parent CSS custom property every frame merely to drive one child if setting the child transform directly avoids broad style recalculation.
- Use CSS/WAAPI for predetermined compositor-friendly motion; use runtime animation only when dynamic control is necessary.
- Treat blur and `backdrop-filter` as expensive; apply them to limited surfaces, keep animated blur modest, and test Safari/mobile hardware.
- Use `will-change` shortly before meaningful motion, not permanently across large parts of the page.
- Staggered entrances must never delay interactivity.

When an animation feels wrong, check frame pacing and layout/paint cost before endlessly tuning the curve.

## 8. Reduced motion, pointer capability, transparency, and contrast

Reduced motion does not mean removing all feedback. Replace vestibular movement with a short opacity/color transition or an instant state where needed.

```css
@media (prefers-reduced-motion: reduce) {
  .sheet {
    transform: none !important;
    transition: opacity 160ms ease;
  }
}

@media (hover: hover) and (pointer: fine) {
  .card:hover {
    transform: translateY(-2px);
  }
}

@media (prefers-reduced-transparency: reduce) {
  .floating-surface {
    background: var(--surface-solid);
    backdrop-filter: none;
  }
}

@media (prefers-contrast: more) {
  .floating-surface {
    background: var(--surface-solid);
    border-color: var(--border-strong);
  }
}
```

Rules:

- Gate hover-only motion behind hover/pointer capability.
- Remove parallax, large positional movement, elastic overshoot, and long looping oscillation for reduced motion.
- Keep feedback that aids comprehension.
- Avoid abrupt full-screen brightness changes.
- Provide solid/high-contrast alternatives for translucent materials.

## 9. Tooltips, lists, and repeated surfaces

- Delay the first tooltip enough to avoid accidental activation; once a tooltip group is active, adjacent tooltips may appear immediately without replaying an entrance each time.
- Use a short 30–80ms stagger only for low-frequency group entrances. Do not stagger dense lists the user opens constantly.
- For rapidly added/removed items, choose an interruptible transition and preserve list stability.
- Do not animate sorting/filtering in ways that make the user lose track of data.

## 10. Materials and depth

Translucency can communicate a floating layer, but it is not a universal style.

- Use translucent chrome only when content spatially passes beneath it and the hierarchy benefits.
- Avoid stacking multiple light translucent surfaces; legibility and depth collapse.
- Larger floating surfaces may require stronger separation than small chips.
- Use a scrim for blocking modal tasks; avoid a scrim for parallel, non-blocking panels.
- Prefer surface, border, and contextual shadow tokens over arbitrary glass effects.
- Verify reduced-transparency and high-contrast behavior.

## 11. Compact motion vocabulary

Use precise terms when discussing or prompting motion:

- **Origin-aware animation:** a surface grows from its trigger/anchor.
- **Continuity transition:** before and after remain visually connected.
- **Shared-element transition:** one element moves/transforms into its new representation.
- **Layout animation:** an element animates to its new layout position/size.
- **Crossfade:** outgoing and incoming content exchange opacity in place.
- **Morph:** one shape/content representation smoothly becomes another.
- **Stagger:** related items enter sequentially with small offsets.
- **Velocity handoff:** release velocity becomes the settling animation’s initial velocity.
- **Momentum projection:** velocity predicts the resting endpoint.
- **Rubber-banding:** progressive resistance beyond a boundary.
- **Interruptible motion:** motion can be redirected from its current state.
- **Press feedback:** immediate response while a pointer/touch is down.
- **Hold to confirm:** progress accumulates during a deliberate press and cancels on early release.
- **Direction-aware transition:** forward/back navigation uses opposite, meaningful directions.
- **Compositing:** transform/opacity update without repeating layout/paint.

When several terms fit, name the primary term and briefly distinguish the alternatives.

## 12. Motion review blockers

Block or flag strongly when applicable:

- Animation on keyboard-initiated or extremely frequent actions.
- `ease-in` on a normal UI response without an exceptional, tested reason.
- `scale(0)` entrances.
- Trigger-anchored surfaces animating from an unrelated center.
- Long normal-product UI animation that makes users wait.
- Keyframes that restart on rapidly retriggered or gesture-driven UI.
- Gesture motion that cannot be interrupted or jumps when grabbed.
- Avoidable layout-property animation causing jank.
- Movement without reduced-motion treatment.
- Hover motion not gated for pointer capability.
- Motion added to functional data only for decoration.

## 13. How to judge feel

Code review cannot fully determine animation quality. When feel is uncertain:

1. Slow the motion to 2–5× duration and inspect origin, path, overlap, and property synchronization.
2. Use browser animation/performance tooling frame by frame.
3. Test the real touch device for gesture interactions.
4. Interrupt and reverse the motion repeatedly.
5. Test while the main thread is busy.
6. Revisit with fresh eyes rather than inventing a confident answer from code alone.
