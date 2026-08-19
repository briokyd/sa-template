# UI Foundation Audit

> Task: AUD-060
> Status: VERIFIED
> Authority: AUDIT-001

Scope: factual audit of the UI stack, tokens, primitives, layouts, pages, shells, assets, responsive and accessibility source evidence, and A-002 keep-list evidence. No UI, application, configuration, dependency, asset, or route implementation was changed.

## Audit boundary

The audited baseline is `503ca9a0f46bc732fe974b6d336e1d1fcd2eb8a4` on `audit/kyd-starter-v1`. AUD-030 findings are referenced for the absence of an Email Magic Link path and editable profile route. AUD-040 findings are referenced for the payment checkout boundary. AUD-050 findings are referenced only for optional platform mounting in the app provider. This task does not make A-002 final; it supplies repository-grounded evidence for that decision.

Visual output, keyboard behavior, screen-reader behavior, browser breakpoints, and visual regression were not run. Statements about responsive behavior are source evidence only, not browser-verification claims.

## 1. Actual UI stack

- The repository uses Tailwind CSS `4.1.4` through `@tailwindcss/postcss`, `globals.css`, and `theme.css`. No runtime Tailwind configuration file exists, despite `components.json` naming `tailwind.config.ts`.
- `components.json` is a shadcn schema with RSC, TypeScript, CSS-variable, `@/components/ui`, and `@/lib/utils` settings. `src/components/ui/` contains 33 shadcn-style primitives with concrete application imports, not merely unused generated files.
- Radix primitives back accordion, avatar, checkbox, collapsible, dialog, dropdown menu, label, navigation menu, radio group, select, separator, slot, switch, tabs, toggle, toggle group, and tooltip. `vaul` backs Drawer, Sonner backs toasts, and React Hook Form plus Zod backs the generic form block.
- `cn` in `src/lib/utils.ts` composes `clsx` and `tailwind-merge`. Icons are supplied by Lucide in primitives, Remix icons through `src/components/icon/index.tsx`, direct React Icons usage, and a smaller Tabler use in dashboard/data-card components.
- Additional observed UI libraries are Framer Motion, Embla carousel, TanStack Table dependency, Recharts, dnd-kit, `@uiw/react-md-editor`, and `next-themes`.

## 2. Tokens, typography, and theme

- `src/app/theme.css` declares light/dark CSS variables for background, foreground, card, popover, primary, secondary, muted, accent, destructive, border, input, ring, chart, sidebar, radius, spacing, shadow, and font families; `@theme inline` maps them into Tailwind v4 tokens.
- `src/app/globals.css` supplies a max-width container, base border/ring styles, and base input/select/textarea/button styles. Major components consume semantic token utilities such as `bg-card`, `text-muted-foreground`, `border-input`, `ring-ring`, and sidebar tokens.
- The named `Outfit` and `Fira Code` font families have no `next/font`, `@font-face`, or other source import evidence. Browser font availability/fallback is therefore `NOT VERIFIED`.
- `ThemeProvider` uses `next-themes` class mode with a public default-theme variable and system theme support. It also mounts Sonner, analytics, AdSense, and an Auth sign modal, so it is an application composition provider as well as a theme provider.
- `components/theme/toggle.tsx` changes theme from clickable SVG icons rather than semantic buttons. This is a concrete keyboard/accessibility gap; it does not require a theme-system replacement.

## 3. Primitive groups and source usage

- Buttons, Input, Textarea, Label, Select, Radio Group, Checkbox, Dialog, Sheet, Drawer, Dropdown Menu, Tooltip, Tabs, Accordion, Table, Card, Badge, Alert, Skeleton, Avatar, Breadcrumb, Separator, Sidebar, Carousel, Chart, and Sonner wrappers are present.
- Button has variants/sizes, disabled state, `asChild`, and `focus-visible`/invalid attributes. Input, Textarea, Select, Dialog, Drawer, Dropdown Menu, Tabs, Accordion, Avatar, Breadcrumb, and Sidebar retain Radix/shadcn-style structural semantics and focus treatment.
- Import coverage outside the primitive directory confirms repeated use of Button (16 files), Card (9), Badge (9), Sidebar (8), Avatar (5), Dropdown Menu (4), Dialog (3), Input (3), Select (3), and Table (1). Some primitives are present but not imported outside primitives today: Checkbox, Switch, Alert, Skeleton, Tabs, and Tooltip.
- The generic `blocks/form` uses React Hook Form, Zod, FormLabel, FormDescription, FormMessage, Input/Textarea/Select, and Markdown editor. It is rendered by both console and admin slots. Its HTML tips use `dangerouslySetInnerHTML`; safety is an AUD-070 boundary, not a UI refactor conclusion.
- The generic `blocks/table` renders columns, empty data, image/time/label/copy cells. Admin and console wrappers both feed it with typed slot data and give their card/table regions horizontal overflow handling.

## 4. Shells, routes, and page inventory

| Surface | Routes / implementation | Reuse boundary | Source evidence |
|---|---|---|---|
| Marketing shell | `src/app/[locale]/(default)/layout.tsx`, blocks Header/Footer | Structural shell is data-driven; brand, links, copy, and optional controls come from localized page data | Header has desktop NavigationMenu and mobile Sheet; Footer renders supplied brand/nav/social/agreement data |
| Landing / showcase | default root and showcase pages, 33 block files | Section structures are reusable; all supplied content/images are product-specific | Landing composes Hero, Features, Showcase, Stats, Pricing, Testimonials, FAQ, and CTA from `getLandingPage` |
| Pricing | pricing page and `blocks/pricing` | Card/feature/CTA structure reusable; product groups, currency, CNY image, and checkout behavior are product-specific | Calls `/api/checkout`, opens sign modal if no user, and renders server data |
| Auth UI | sign-in route and `components/sign/*` | Google/GitHub button/card/modal patterns reusable; provider details and legal copy are product-specific | Desktop Dialog and mobile Drawer modal; provider buttons use public enable flags |
| Console | console layout, sidebar nav, table/form slots, orders/credits/invites/API keys pages | Generic slots reusable; current navigation and business surfaces are product-specific | Auth boundary redirects unauthenticated users; desktop row/mobile-column layout |
| Admin dashboard | admin layout, dashboard shell, sidebar/header/slots, users/orders/posts/feedback pages | Sidebar/dashboard structure reusable; ShipAny brand, external links, and menu content are product-specific | DashboardLayout consumes Sidebar data; admin layout creates hard-coded brand/nav/social/account data |
| Blog | posts pages and `blocks/blog*` | Article/list structure reusable for projects that need posts | Uses post data, Markdown renderer, Avatar, Card, responsive article grid |
| Docs | Fumadocs layout/routes/content | Optional content system, not Starter Core UI | Fumadocs RootProvider/DocsLayout, search endpoint, localized docs tree; currently ShipAny-branded |
| Legal | legal MDX layout/pages | Product-specific legal copy and links | Separate layout and MDX pages |

No page-level `loading`, `error`, or `not-found` route file was found. Existing `Empty` is a simple centered message and is used for selected absent/auth/access states. Skeleton and Alert primitives exist, but no page-level loading/error orchestration is evidenced.

## 5. Dashboard and console evidence

- `DashboardLayout` uses the shadcn Sidebar provider/inset with defined sidebar/header dimensions. `DashboardSidebar` is `collapsible="offcanvas"`, uses an accessible Sidebar trigger, can show navigation, library, bottom navigation, social links, user dropdown, and mobile-dependent dropdown position.
- `DashboardHeader` includes a Sidebar trigger and responsive breadcrumbs that hide non-active crumbs at `md`. Its users menu contains avatar, account navigation, and logout.
- `ConsoleLayout` is a separate lightweight shell: horizontal navigation on small layouts becomes vertical at `lg`, with a content column. It does not reuse the full Dashboard Sidebar.
- Both app shells use the same data-driven Table/Form block layer through different wrappers. The wrappers differ in header/card/page framing; this is evidence of parallel shell composition, not proof that a consolidation/refactor is required.
- The console navigation logs `pathname` to the browser console, and several UI event handlers log errors/values. Logging/redaction policy belongs to AUD-070.

## 6. Marketing, pricing, auth, and content evidence

- Header is responsive: desktop navigation at `lg`, mobile Sheet with Accordion child navigation, locale/theme/sign controls, and button data. Footer supports data-driven logo/nav/social/legal links plus a ShipAny-powered footer controlled by an environment variable.
- Marketing blocks use responsive grids, headings, cards, carousels, tabs, accordion, image assets, and data supplied from localized JSON. The structural components can be retained even though all default copy, images, URLs, logo, testimonial data, and product claims are template-specific.
- Pricing uses Radio Group and labels for plans, selected/product loading state, Button, Badge, toast feedback, and client checkout. Dynamic class construction for `grid-cols-${pricing.groups.length}` and `md:grid-cols-${filtered count}` is source evidence of a Tailwind generation risk; browser/build output was not run. The CNY payment image/control is product/payment-specific and uses a clickable `div`.
- Auth UI has Google/GitHub provider buttons and sign state controls; Email/Magic Link UI is absent, consistent with AUD-030. The user menu offers orders/admin/logout rather than a dedicated editable profile route.
- Blog details use a Card/Markdown/Avatar layout. Docs uses Fumadocs styles and controls; its navigation title, logo, and locale options include current-template branding.

## 7. Responsive and accessibility baseline

- Source responsive evidence is present: global container padding changes at `md`; marketing blocks use `sm`, `md`, `lg`, and `2xl` grid/type/layout rules; Header switches to Sheet navigation; SignModal chooses Dialog at `min-width: 768px` and Drawer otherwise; Dashboard Sidebar is off-canvas; console switches from row to column; dashboard cards enable horizontal table/form overflow.
- `useMediaQuery` and duplicate `useIsMobile` hooks use `matchMedia`; `data-charts` consumes the `.ts` hook. No browser viewport execution was performed, so responsive correctness is `NOT YET BROWSER-VERIFIED`.
- Accessibility source evidence includes Radix semantics, FormLabel/FormMessage relationships, Alert `role="alert"`, Breadcrumb `aria-label` and current-page attributes, visually hidden menu text, image alt properties, Dialog/Drawer titles/descriptions, focus-visible classes, Radio Group with Label, and a chart aria label.
- No accessibility test, keyboard test, screen-reader test, or browser test was found. Clickable theme SVGs and the CNY pricing `div` are concrete semantic/keyboard follow-ups. No WCAG conformance claim is made.

## 8. Assets, icons, and duplication evidence

- `public/` contains `logo.png`, favicon, static feature/showcase/user imagery, icons, masks, badges, and brand-logo SVGs. Components use a mixture of `next/image` and native `img`; asset URLs and image alt data are often supplied through page data.
- UI primitives consistently use Lucide. Product navigation uses the custom Remix-icon adapter, while brand/provider icons use direct React Icons and selected dashboard/data-card components import Tabler. This is a confirmed multi-library icon system, but not a correctness reason to consolidate it during audit.
- `src/hooks/use-mobile.ts` and `src/hooks/use-mobile.tsx` contain the same `useIsMobile` implementation. The `.ts` path is the observed import used by `data-charts`. Dashboard and console each have Table/Form slot wrappers around the same generic block components. Retaining these parallel forms is lower risk than a consolidation without behavior tests.
- The custom icon adapter always applies a cursor-pointer class even without an `onClick`, and accepts icons by string. Its mapping supports only the imported Remix set. This is reusable as a data-driven product icon adapter but needs test/usage review before being treated as a universal icon system.

## 9. A-002 evidence table

This table is repository evidence for A-002, not the final A-002 decision.

| Major UI group | Starter role | Action | Evidence paths | Key risks / tests required |
|---|---|---|---|---|
| Tailwind v4, CSS variables, `cn` utility | CORE | PATCH | `src/app/globals.css`, `src/app/theme.css`, `src/lib/utils.ts`, `components.json` | Test token/dark-mode output; reconcile stale `components.json` Tailwind config reference; verify supplied font loading/fallback |
| Base shadcn/Radix primitives | CORE | KEEP + TEST | `src/components/ui/*`, `package.json` | Component rendering, keyboard/focus, disabled/invalid, dialog/menu/tooltip behavior tests |
| Forms and data tables | CORE | KEEP + TEST | `components/blocks/form`, `blocks/table`, console/dashboard slots | Field type, validation, submit/error, empty/copy, overflow, and server-action integration tests |
| Theme provider and toggle | CORE | WRAP | `src/providers/theme.tsx`, `components/theme/toggle.tsx` | Separate theme composition from optional app modules at future integration boundary; test keyboard theme toggle and hydration |
| Dashboard Sidebar / admin shell | CORE | KEEP + TEST | `components/dashboard/*`, admin layout | Desktop/mobile navigation, user menu/logout, access and layout tests; replace product menu data per project |
| Console shell | CORE | KEEP + TEST | `components/console/*`, console layout | Responsive nav, tables/forms, protected route and empty-state tests |
| Marketing Header/Footer/section blocks | CORE | KEEP + TEST | `components/blocks/header`, `footer`, Hero/Feature/FAQ/CTA/etc. | Browser responsive, navigation, image/alt, section data, and visual regression tests; replace content/assets |
| Pricing UI | CORE | PATCH | `components/blocks/pricing`, pricing page | Build/browser grid behavior, semantic CNY control, sign-in/checkout/loading/error tests; preserve payment boundary from AUD-040 |
| Auth/account UI | CORE | PATCH | `components/sign/*`, sign-in route, dashboard user menu | Google/auth error/loading/logout tests; add UI only when AUD-030 Magic Link patch is authorized; no editable profile UI evidence |
| Blog and Fumadocs | OPTIONAL | KEEP-DISABLED | blog blocks/pages, docs layout/content | Docs/blog rendering, locale, Markdown, search, content asset tests; replace brand content if enabled |
| Charts, carousel, editor, data cards | OPTIONAL | KEEP-DISABLED | `blocks/data-*`, `showcase1`, `mdeditor`, UI carousel/chart | Enable only per product; responsive/chart/editor behavior tests |
| Asset conventions and icon adapters | CORE | KEEP + TEST | `public/*`, `components/ui/icon.tsx`, `components/icon/index.tsx` | Asset/image behavior, alt coverage, icon mapping, and bundle/use tests; branding is product-specific |
| Empty/loading/error states | CORE | PATCH | `blocks/empty`, UI Skeleton/Alert, app route search | Add page-level loading/error/not-found behavior only as a bounded future patch; test user-visible failure paths |
| Accessibility and responsive baseline | CORE | PATCH | primitives, Header, SignModal, Pricing, Sidebar, hooks | Keyboard, focus order, semantic controls, screen-reader, desktop/mobile browser and visual regression tests |

## 10. Required UI conclusion

Can the current sa-template UI Foundation be reused for Kyd SaaS Starter V1 with minimal delta?

YES — PATCH

The tokenized Tailwind/shadcn/Radix foundation, utility helper, generic data blocks, app shells, marketing structures, and content surfaces can be retained. KEEP and KEEP + TEST are sufficient for most primitives and data-driven shells. They are insufficient for the confirmed configuration/semantic/default gaps: stale shadcn Tailwind config reference, composed theme provider, dynamic pricing classes and controls, absent Magic Link/profile UI, no route-level error/loading states, and keyboard semantics. Localized PATCH or WRAP work is sufficient; no REFACTOR or DELETE is justified.

## Findings Table

| Module / Capability | Existing implementation | Existing files | Current behavior | Starter planned role | Required behavior | Gap | Action | Default enabled? | Tests today | Tests required | Cloudflare compatibility | Risk | Reason | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tailwind/token foundation | Tailwind v4 CSS variables, semantic colors, radius, spacing, shadow, light/dark tokens, `cn` | `globals.css`, `theme.css`, `components.json`, `utils.ts` | Primitives consume semantic utility tokens | CORE | Reusable token foundation with accurate tool config/font behavior | `components.json` names absent `tailwind.config.ts`; named fonts have no source import evidence | PATCH | ON | NO EVIDENCED TEST | Token/theme/font/build tests | NOT_APPLICABLE | Medium | Existing CSS token system is mature enough to keep; localized configuration correction is sufficient | CSS variables and absent config/font searches |
| shadcn/Radix primitives | 33 UI primitives, Radix wrappers, variants and focus styles | `src/components/ui/*`, `package.json` | Heavily used Button/Card/Badge/Sidebar/Avatar/Menu; less-used primitives retained | CORE | Accessible reusable controls | No component/a11y/browser test evidence | KEEP + TEST | ON | NO EVIDENCED TEST | Render, keyboard, focus, invalid/disabled, overlay/menu tests | NOT_APPLICABLE | Medium | Concrete usage supports retention; no replacement needed | Primitive imports and usage counts |
| Generic form/table blocks | RHF/Zod dynamic forms and column-driven table with empty/copy/image/time cells | `blocks/form`, `blocks/table`, slot wrappers | Shared by admin and console with typed data | CORE | Data-driven CRUD surface | No test coverage; HTML tip safety deferred to AUD-070 | KEEP + TEST | ON | NO EVIDENCED TEST | Validation, submit, error, empty, copy, overflow, server-action tests | NOT_APPLICABLE | High | Shared implementation has real multi-surface use; not duplicated business UI | Both shell slot imports |
| Theme composition/toggle | next-themes provider, Sonner, optional modules, SVG toggle | provider/theme, theme/toggle | Class theme with system default; provider mounts app-wide extras | CORE | Reusable theme boundary and keyboard control | Theme provider mixes optional app modules; toggle is nonsemantic SVG click target | WRAP | ON | NO EVIDENCED TEST | Theme persistence/hydration, keyboard and focus tests | NOT_APPLICABLE | Medium | A thin composition boundary preserves provider; no theme replacement required | Provider and toggle source |
| Dashboard/admin shell | SidebarProvider, off-canvas sidebar, header/breadcrumb/user menu/slots | `components/dashboard/*`, admin layout | Layout accepts sidebar data; current admin layout hard-codes ShipAny content | CORE | Configurable authenticated shell | Browser/a11y tests absent; menu/brand data product-specific | KEEP + TEST | ON | NO EVIDENCED TEST | Desktop/mobile nav, logout, access, table/form layout tests | NOT_APPLICABLE | Medium | Generic shell already separates sidebar structure from data | DashboardLayout and sidebar props |
| Console shell | Responsive nav plus generic slots | `components/console/*`, console pages/layout | Small-screen row navigation changes to desktop column navigation | CORE | Reusable member-area shell | Separate shell style, no browser tests; pathname debug log | KEEP + TEST | ON | NO EVIDENCED TEST | Responsive nav, active route, auth/empty/table/form tests | NOT_APPLICABLE | Medium | Keep independent shell; differences are intentional composition, not refactor proof | ConsoleLayout and slot use |
| Marketing shell/blocks | Data-driven header/footer, hero/features/showcase/stats/testimonials/FAQ/CTA | `components/blocks/*`, default pages, i18n JSON | Localized page data selects shown blocks; Header has desktop/mobile navigation | CORE | Reusable marketing structure with replacement content | Copy, links, imagery and brand content are product-specific; no visual/browser tests | KEEP + TEST | ON | NO EVIDENCED TEST | Responsive nav/sections, accessibility, image, visual regression tests | NOT_APPLICABLE | Medium | Structural blocks are reusable independently of content | Default layout and landing composition |
| Pricing UI | Radio plan groups, plan cards, checkout CTA/toasts/loading | `blocks/pricing`, pricing page | Calls shared checkout API with selected product/currency | CORE | Product-configured pricing and robust layout/semantic controls | Dynamic Tailwind grid names; clickable CNY div; payment data/content product-specific | PATCH | ON when page data enables it | NO EVIDENCED TEST | Build/browser grid, plan selection, keyboard, unauth/auth checkout, loading/error tests | NOT_APPLICABLE | High | Preserve UI and payment boundary; targeted layout/control patches suffice | Pricing source and AUD-040 checkout evidence |
| Auth/account UI | Sign modal/card, provider buttons, avatar/user menu, logout | `components/sign/*`, sign-in page, dashboard user | Google/GitHub buttons env-gated; desktop dialog/mobile drawer; orders/admin/logout menu | CORE | Google plus Magic Link UI, profile/account shell, error/loading behavior | Magic Link and editable profile UI absent; no auth UI tests | PATCH | OFF when Auth disabled | NO EVIDENCED TEST | Provider visibility, dialog/drawer, errors, logout, Magic Link/profile after authorized Auth patch | NOT_APPLICABLE | High | AUD-030 requires a bounded Auth patch; no visual-system migration needed | Provider flags, sign form/modal, user menu |
| Blog/docs/content UI | Blog list/detail, Markdown, Fumadocs DocsLayout/search | blog blocks/pages, docs layout/content | Existing optional content surfaces with ShipAny branding | OPTIONAL | Retain for projects selecting content/docs | Not Starter default; no content/browser test evidence | KEEP-DISABLED | ON in current template | NO EVIDENCED TEST | Blog/docs/Markdown/search/locale/image tests | NOT_APPLICABLE | Medium | Retention disabled is lower risk than deletion or redesign | Fumadocs/blog route code |
| Optional charts/editor/carousel | Recharts chart, Embla showcase, MD editor, data cards | `blocks/data-*`, `showcase1`, `mdeditor`, UI chart/carousel | Existing optional, selectively imported capability set | OPTIONAL | Retain for product opt-in | No default Starter requirement or tests | KEEP-DISABLED | ON only where current pages render them | NO EVIDENCED TEST | Enablement/render/responsive/editor/chart tests | NOT_APPLICABLE | Low | No removal evidence; keep optional | Component inventory and imports |
| Empty/loading/error states | Empty message; Skeleton/Alert primitives | `blocks/empty`, UI Skeleton/Alert, app route search | Empty used for selected cases; no route-level loading/error/not-found components found | CORE | Predictable loading/error/not-found UI | Confirmed missing route-level states | PATCH | PARTIAL | NO EVIDENCED TEST | Empty/loading/error/not-found route tests | NOT_APPLICABLE | Medium | Additive state components are smaller than a page redesign | Route search and current Empty use |
| Assets/icons/duplicate systems | Public asset tree; Lucide, Remix adapter, React Icons, Tabler; duplicate mobile hook/slot wrappers | `public/*`, icon files, hooks, slots | Multiple icon sources and parallel wrappers; native img plus next/image | CORE | Retain conventions while keeping brand data replaceable | Mixed systems and duplicated hook/wrappers; no behavior failure evidenced | KEEP + TEST | ON | NO EVIDENCED TEST | Asset/alt, icon mapping, image, hook and wrapper behavior tests | NOT_APPLICABLE | Low | No correctness proof for consolidation; preserve and test | Asset/icon/import and duplicate-path search |
| Responsive/accessibility baseline | Breakpoint classes, Sheet/Drawer/Sidebar, Radix semantics, labels/aria/alt | Header, SignModal, Pricing, Sidebar, primitives, hooks | Source evidence exists for mobile/desktop branches and semantic cues | CORE | Browser-verified responsive and keyboard-safe UI | No browser/a11y tests; clickable SVG and pricing div are semantic gaps | PATCH | ON | NO EVIDENCED A11Y TEST | Keyboard, focus, screen-reader, viewport, visual-regression tests | NOT_APPLICABLE | High | Targeted semantics and tests are sufficient; no broad visual rewrite justified | Breakpoint/aria/focus source searches |

## Verification notes

- No test framework, test script, test directory, test/spec file, browser/E2E suite, accessibility suite, or visual-regression suite was found.
- No REFACTOR or DELETE action is recommended. The documented PATCH and WRAP findings are localized and do not justify a component-system or route redesign.
- No UI/application/configuration implementation file was modified during AUD-060.
