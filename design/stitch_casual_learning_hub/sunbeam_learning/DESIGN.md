# Design System Strategy: The Tactile Playground

## 1. Overview & Creative North Star
This design system is built upon the Creative North Star of **"The Tactile Playground."** While many educational platforms lean toward rigid, grid-locked layouts or overly "childish" aesthetics, this system pursues a high-end editorial feel that remains approachable and warm. 

The goal is to break the "standard template" look. We achieve this through **Intentional Asymmetry**—where elements breathe in varying amounts of white space—and **Tonal Depth**, moving away from flat UI into a world of layered, physical surfaces. We trade harsh dividers for soft color transitions, making the interface feel like a curated collection of smooth, matte paper and frosted glass.

---

## 2. Colors & Surface Logic
The palette is rooted in warmth (`background: #fbf9f1`) and punctuated by soft, sophisticated pastels. We use the Material Design token logic to ensure the UI feels dynamic and accessible.

### The "No-Line" Rule
**Explicit Instruction:** Designers are prohibited from using 1px solid borders for sectioning or layout containment. Boundaries must be defined solely through background color shifts. 
- Use a `surface_container_low` section sitting on a `surface` background to define a sidebar or header. 
- If a section needs separation, use white space or a subtle transition to `surface_container_high`.

### Surface Hierarchy & Nesting
Think of the UI as a series of physical layers. We use the surface-container tiers to create depth:
- **Level 0 (Base):** `surface` or `background` (#fbf9f1) — The canvas.
- **Level 1 (Sections):** `surface_container_low` (#f5f4ec) — Defining large content areas.
- **Level 2 (Cards/Modules):** `surface_container_lowest` (#ffffff) — Drawing the eye to actionable content.
- **Level 3 (Interactive):** `surface_bright` — For elements that need to pop against the background.

### The "Glass & Gradient" Rule
To elevate the platform above generic "flat" design, use **Glassmorphism** for floating elements (like navigation bars or modals). 
- **Backdrop Blur:** 12px to 20px.
- **Color:** A semi-transparent version of `surface` (e.g., 80% opacity).
- **Gradients:** For hero backgrounds or Primary CTAs, use a subtle radial gradient transitioning from `primary` (#745b00) to `primary_container` (#f2c94c). This adds "soul" and a sense of light that flat fills lack.

---

## 3. Typography
We utilize **Plus Jakarta Sans** for its geometric yet friendly personality. It bridges the gap between professional editorial and casual accessibility.

- **Display & Headline Scale:** Use `display-lg` to `headline-sm` for high-impact moments. These should be set with tight letter-spacing (-0.02em) to feel authoritative and "branded."
- **Body & Title Scale:** Use `body-lg` for primary reading. Ensure a generous line-height (1.6) to maximize the "high white space" aesthetic.
- **Labeling:** Use `label-md` in all-caps with increased letter-spacing (+0.05em) for small metadata or categories to provide a sophisticated, functional contrast to the friendly headline styles.

---

## 4. Elevation & Depth
In this design system, depth is a feeling, not a structure.

- **The Layering Principle:** Achieve lift by stacking tokens. A `surface_container_lowest` card placed on a `surface_container_low` background creates a soft, natural lift without the need for heavy shadows.
- **Ambient Shadows:** When an element must "float" (like a primary action button or a modal), use a shadow tinted with the `on_surface` color at 5% opacity. Shadows must have a large blur radius (30px+) and no spread to mimic natural, ambient light.
- **The "Ghost Border" Fallback:** If a border is required for accessibility (e.g., in high-contrast modes), use the `outline_variant` token at **15% opacity**. Never use a 100% opaque border.
- **Edge Softness:** Every container follows the **xl radius (3rem)** for primary containers and **DEFAULT (1rem)** for smaller components to maintain the friendly, "organic" feel of the system.

---

## 5. Components

### Buttons
- **Primary:** Pill-shaped (`full` roundedness), using the `primary_container` background with `on_primary_container` text. Apply a subtle top-down gradient.
- **Secondary:** Transparent background with a `surface_container_high` fill on hover. No border.
- **Tertiary:** Text-only with `label-md` styling, using the `secondary` color token.

### Cards
- **Construction:** Use `surface_container_lowest` (#ffffff).
- **Prohibition:** No divider lines. Use vertical white space (32px or 48px) to separate the image, headline, and body text within the card.
- **Radius:** Strictly `lg` (2rem) for an approachable, modern feel.

### Input Fields
- **Background:** `surface_container_highest` (#e4e3db) to provide a clear, "sunken" interactive area.
- **Focus State:** Instead of a thick border, use a 2px "Ghost Border" of `primary` at 40% opacity and a soft outer glow.

### Interactive Chips
- **Selection:** Use `secondary_container` for the active state.
- **Filter:** Use `surface_container_low` with `body-sm` typography.

### Progress Visuals (Education Specific)
- Use thick, rounded strokes (12px width) for progress bars using `primary_container` as the track and `primary` as the indicator. Avoid thin, clinical lines.

---

## 6. Do's and Don'ts

### Do
- **Do** lean into asymmetry. It’s okay if a layout has more white space on the left than the right.
- **Do** use "Plus Jakarta Sans" Bold for headings to create a strong visual anchor.
- **Do** use the `secondary_fixed_dim` (#9ecfd1) for success states or "friendly" accent moments to maintain the pastel vibe.

### Don't
- **Don't** use pure black (#000000) for text. Always use `on_surface` (#1b1c17) or `on_surface_variant` (#4d4635) for a softer, premium feel.
- **Don't** use standard "Drop Shadows." If it looks like a default Photoshop shadow, it's too heavy.
- **Don't** use 1px dividers to separate list items. Use a 12px or 16px gap and a subtle background shift on hover.
- **Don't** use sharp corners. Every corner must be at least `sm` (0.5rem) to stay within the "Tactile Playground" ethos.