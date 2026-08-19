# UI Foundation Audit

> Task: `AUD-080`  
> A-002 result: `FROZEN — KEEP LIST`  
> Boundary: this freezes reusable foundation groups, not product-specific visual design, content, branding, or assets.

## Existing Foundation

The source provides Tailwind CSS 4 semantic CSS variables, light/dark theme support, `cn`, 33 concretely used shadcn-style primitives, Radix-backed interactions, React Hook Form/Zod forms, generic tables, dashboard/console shells, data-driven marketing blocks, pricing/Auth surfaces, Fumadocs/blog content, and multiple asset/icon conventions.

Source evidence supports retention. Browser, keyboard, screen-reader, responsive, and visual behavior is not yet verified and remains a release-gate requirement.

## Component-Level KEEP / PATCH / Other Actions

### A-002 frozen keep list

| Group | Starter role | Final Action | Exact evidence | Required bounded PATCH | Required tests |
|---|---|---|---|---|---|
| Tailwind v4 semantic tokens, global CSS, `cn` | CORE | PATCH | `src/app/globals.css`, `src/app/theme.css`, `src/lib/utils.ts`, `components.json` | Correct stale config reference and establish font behavior; preserve tokens | Build, light/dark, token, font fallback |
| shadcn/Radix primitives | CORE | KEEP + TEST | `src/components/ui/*`, Radix dependencies; 33 primitives with concrete imports | None unless tests expose behavior defects | Render, focus, keyboard, invalid/disabled, overlay/menu |
| Generic forms and tables | CORE | KEEP + TEST | `src/components/blocks/form`, `table`, console/dashboard slot wrappers | Handle verified HTML/input safety only through bounded security patch | Validation, submit/error, empty/copy, overflow, server actions |
| Theme provider/composition | CORE | WRAP | `src/providers/theme.tsx`, `src/components/theme/toggle.tsx` | Thin composition boundary for optional app modules; semantic toggle control | Hydration, persistence, keyboard/focus |
| Dashboard/admin shell | CORE | KEEP + TEST | `src/components/dashboard/*`, admin layout | Replace only product menu/brand data per project | Desktop/mobile navigation, access, user menu/logout |
| Console/member shell | CORE | KEEP + TEST | `src/components/console/*`, console layout/pages | Remove debug output as part of logging patch | Responsive navigation, protected states, slots |
| Marketing Header/Footer/section blocks | CORE | KEEP + TEST | `src/components/blocks/*`, localized page-data composition | Replace product content/assets, not structure | Responsive nav/sections, image/alt, visual smoke |
| Pricing UI structure | CORE | PATCH | pricing page and `src/components/blocks/pricing` | Static-safe grids, semantic controls, robust loading/error behavior | Plans, keyboard, sign-in/checkout, provider outcomes |
| Auth/account UI structure | CORE | PATCH | `src/components/sign/*`, sign-in route, dashboard user menu | Add Magic Link/profile/error states only with Auth patch | Provider visibility, modal/drawer, Magic Link, profile, logout |
| Asset and icon conventions | CORE | KEEP + TEST | `public/*`, Lucide primitives, Remix adapter, React Icons/Tabler use | No consolidation unless tests prove a defect; replace product assets | Image/alt, icon mapping, bundle behavior |
| Empty/loading/error/not-found states | CORE | PATCH | `blocks/empty`, UI Skeleton/Alert, absence in route scan | Add bounded route-level states | Empty/loading/error/not-found routes |
| Responsive/accessibility foundation | CORE | PATCH | breakpoints, Header Sheet, Sign Drawer/Dialog, Sidebar, labels/ARIA/focus styles | Fix clickable SVG/div semantics and any test-proven defects | Mobile/desktop, keyboard, focus, screen-reader, visual regression |
| Blog and Fumadocs | OPTIONAL | KEEP-DISABLED | blog blocks/pages, docs layout/content/search | Replace branding/content if selected | Build, render, Markdown, search, locale |
| Charts/carousel/editor/data cards | OPTIONAL | KEEP-DISABLED | chart/data blocks, Embla showcase, MD editor | Product-specific enablement only | Render, responsive, editor/chart behavior |
| ShipAny copy, claims, logos, images, links, pricing products, menus, legal content | PRODUCT-SPECIFIC | KEEP-DISABLED | localized JSON, public assets, hard-coded admin/docs/product data | Replace under future Product/UI Authority | Product-specific fidelity and content review |

No UI group is `NOT_RECOMMENDED`, `REFACTOR`, or `DELETE`. Multiple icon libraries, separate dashboard/console shells, duplicate mobile hooks, and wrapper variations are not correctness evidence for consolidation.

## Responsive / Accessibility Baseline

- Source evidence exists for responsive marketing navigation, Dialog/Drawer switching, off-canvas Sidebar, console layout changes, responsive grids, and table overflow.
- Radix semantics, labels, messages, focus-visible styles, ARIA attributes, Dialog titles/descriptions, and image-alt data provide a reusable accessibility base.
- Confirmed local gaps include clickable theme SVG controls and a clickable pricing `div`; no a11y/browser/visual tests exist.
- Final Action: `PATCH` for known semantics plus required tests. No WCAG compliance claim is made from static source.

## A-002 Evidence

### Decision

`FROZEN — KEEP LIST`

Evidence is sufficient to freeze the structural keep list because components are not merely present: primitives and shells have concrete multi-route imports, semantic tokens are actively consumed, forms/tables serve both admin and console, and marketing content is data-driven. Missing browser tests affect verification and bounded patches, not the repository-grounded keep classification.

The frozen list expressly excludes ShipAny product identity. It does not freeze page copy, colors for a future product, imagery, information architecture, pricing products, current navigation labels, legal language, or product-specific visual fidelity.

## Risks

| Risk | Severity | Final Action | Required control |
|---|---|---|---|
| No browser/a11y/visual test baseline | High | PATCH | Focused responsive, keyboard, accessibility and visual smoke |
| Pricing dynamic classes and nonsemantic controls | High | PATCH | Static-safe styling and semantic interaction tests |
| Magic Link/profile UI absent | High | PATCH | Coordinate with GAP-004/GAP-009; do not invent Auth architecture |
| Theme composition mixes optional modules | Medium | WRAP | Thin composition boundary, preserve provider/theme implementation |
| Route loading/error/not-found absent | Medium | PATCH | Add bounded shared route states |
| Product branding could be mistaken for Starter Authority | Medium | KEEP-DISABLED | Explicit content/asset replacement boundary |
| Multiple icon systems/parallel shells | Low | KEEP + TEST | Retain unless behavior evidence later proves consolidation necessary |
