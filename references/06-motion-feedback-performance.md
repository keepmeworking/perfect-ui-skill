# Motion, Feedback and Performance

Motion must explain change, hierarchy or spatial relationship. Use short consistent duration tokens, generally 80–120ms for press/hover, 150–240ms for small transitions and 250–400ms for larger transitions. Avoid `transition: all` and support `prefers-reduced-motion`.

Async UI should model idle, loading, success, empty, error and stale/revalidating states. Use skeletons for initial structured content, inline progress for local actions and determinate progress when measurable.

Use optimistic updates only for reversible, low-risk operations. On failure, roll back and explain recovery. Critical actions such as payment or account deletion should wait for authoritative confirmation.

Performance rules:
- Render the shell and independent regions without waiting for unrelated dependencies.
- Prevent layout shift with reserved dimensions.
- Compress API responses and assets.
- Paginate or virtualize large data.
- Debounce search and cancel stale requests.
- Lazy-load heavy charts and routes.
- Set timeouts and fallbacks for third-party services.
- Keep feedback immediate even when processing continues.