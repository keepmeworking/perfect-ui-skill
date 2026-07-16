# Accessibility

Target WCAG 2.2 AA for web and equivalent native platform guidance.

Release requirements:
- Native semantics and accessible names.
- Complete keyboard operation with logical focus order.
- Visible `:focus-visible`; never remove outlines without an equivalent.
- Normal text contrast at least 4.5:1; large text and essential UI graphics at least 3:1.
- Status is not conveyed by color alone.
- Reflow at narrow widths and 200% zoom without lost functionality.
- Labels, instructions and error associations for forms.
- Live announcements only for meaningful asynchronous updates.
- Reduced-motion support.
- Touch targets preferably 44×44px and adequately spaced.
- Headings and landmarks reflect the page structure.
- Images have meaningful alt text or are correctly decorative.

Automated tests are useful but insufficient. Perform keyboard, focus, zoom/text scaling, reduced-motion and assistive-technology spot checks.