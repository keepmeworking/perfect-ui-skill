# Async Feedback, Loading, and UI Performance

This reference covers asynchronous behavior and system performance. Load `references/12-motion-craft.md` for detailed animation, gesture, easing, physicality, and motion-review rules.

## Feedback hierarchy

Feedback should be proportional and local to the action.

- Use an immediate visual pressed/selected state to acknowledge input.
- Use inline status for a local action or field.
- Use a toast for a completed background action that does not require a decision.
- Use a banner/section error for a persistent scoped problem.
- Use a modal only when the user must make a blocking decision.
- Do not show duplicate feedback through a state change, toast, and modal for the same simple action.

## Async state model

Model applicable states explicitly:

`idle → pending → success | empty | error | stale/revalidating | offline | permission-limited`

Do not collapse “no data,” “no results,” “not loaded,” and “not allowed” into one empty screen.

## Loading

- Use skeletons for initial structured content when the final layout is known.
- Use inline progress for local actions.
- Use determinate progress when measurable.
- Keep button dimensions stable while loading.
- Prevent duplicate submission without unnecessarily blocking the rest of the page.
- Allow cancellation when an operation is long and safely cancellable.
- Explain what happens if the user navigates away.
- Add timeout/retry/recovery behavior for dependencies that may hang.

## Optimistic UI

Use optimistic updates only when the action is low-risk, likely to succeed, and reversible.

Good candidates include lightweight preferences, favorites, reordering, and reversible status changes. Critical actions such as payment, irreversible deletion, security changes, or final submission should wait for authoritative confirmation.

On optimistic failure:

1. Reconcile or roll back accurately.
2. Preserve user-entered data.
3. Explain what failed.
4. Provide a clear retry or recovery action.
5. Avoid duplicate server-side execution.

## Perceived and actual performance

Immediate feedback can improve perceived speed, but it must not hide actual slowness or failure.

Performance rules:

- Render the shell and independent regions without waiting for unrelated dependencies.
- Prevent layout shift with reserved dimensions and stable placeholders.
- Compress API responses and assets.
- Paginate or virtualize large data.
- Debounce search appropriately and cancel stale requests.
- Cache/revalidate deliberately; show data freshness when it matters.
- Lazy-load heavy charts, editors, and routes without hiding essential controls.
- Set timeouts, circuit-breaker-like fallbacks, and partial-failure states for third-party services.
- Keep feedback immediate even when processing continues.
- Avoid main-thread-heavy animation during data loading.
- Preserve focus and scroll position across revalidation.

## Dependency isolation

A slow widget or third-party call must not block unrelated UI.

Example desired behavior:

- App shell and navigation render.
- Available cards load independently.
- Delayed regions show a scoped skeleton/status.
- Failed regions show scoped retry and diagnostics.
- Other actions remain available.

Do not replace partial failure with a full-page spinner or generic fatal error.

## Verification

Test:

- Fast success.
- Slow success.
- Empty response.
- Validation failure.
- Server failure.
- Timeout.
- Offline/reconnect.
- Stale data/revalidation.
- Duplicate click/tap.
- Navigation during pending work.
- Partial dependency failure.
- Reduced motion and screen-reader status announcements.
- Layout stability under loading and error content.
