# Responsive and Adaptive Layout

Responsive design changes priority and interaction, not merely size.

Use content-driven breakpoints, with compact, medium and expanded layout modes. A practical starting point is 360px, 768px, 1024px and 1440px, but adapt to the product.

Rules:
- Prefer fluid widths, `minmax`, flex/grid wrapping and container queries.
- Avoid fixed widths that create unintended horizontal scrolling.
- Preserve a usable 320 CSS-pixel equivalent web layout except genuinely two-dimensional content.
- Convert desktop sidebars into drawers, rails or bottom navigation based on task frequency.
- Keep touch targets preferably 44px or larger.
- For tables, preserve priority columns and use horizontal scrolling, disclosure or mobile summaries rather than squeezing every column.
- Modals may become full-screen sheets on compact devices.
- Respect safe areas, on-screen keyboards, text scaling, orientation and coarse pointers.

Verify realistic long labels, localization expansion, validation text, empty states, dense data and zoom.