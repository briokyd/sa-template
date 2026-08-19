# Optional Platform Capabilities Audit

> Task: AUD-050
> Status: VERIFIED
> Authority: AUDIT-001

Scope: factual audit of ads, analytics, technical SEO, i18n, AI, storage/R2 suitability, Turnstile, and the related optional surfaces declared by the Task contract. No application, module, configuration, dependency, schema, or secret value was changed or exposed.

## Audit boundary

The audited baseline is `503ca9a0f46bc732fe974b6d336e1d1fcd2eb8a4` on `audit/kyd-starter-v1`. AUD-010 established absent OpenNext/Workers deployment integration and broad environment-validation gaps. AUD-020, AUD-030, and AUD-040 are referenced only where their verified findings bear on the optional modules.

No provider call, upload, AI generation, deployment, or browser test was run. A missing runtime smoke result is recorded as `NOT VERIFIED`, not a confirmed incompatibility.

## 1. Ads / AdSense

- `src/providers/adsense.tsx` renders the AdSense loader only in production and only when `NEXT_PUBLIC_GOOGLE_ADCODE` is non-empty. It returns `null` otherwise.
- `src/providers/theme.tsx` mounts `Adsense` in the client-side theme provider. `src/app/layout.tsx` independently adds the account meta tag when the same public value is present; that meta tag is not production-gated.
- No ad-unit component, slot configuration, consent gate, or additional ad provider was found by repository-wide source search. The loader is sufficient as a retained AdSense integration point, but actual production loading and consent policy are not evidenced.
- Status: `PRESENT`. Starter Action: `KEEP + TEST`. Default: `OFF` when the public code is unset. Cloudflare: `COMPATIBLE` for the browser-only external script; deployment/browser verification remains a test need.

## 2. Analytics / telemetry

- `src/components/analytics/index.tsx` mounts OpenPanel, Google Analytics, and Plausible together only when `NODE_ENV` is production.
- Google Analytics uses `@next/third-parties/google` and `NEXT_PUBLIC_GOOGLE_ANALYTICS_ID`; OpenPanel uses `@openpanel/nextjs` and `NEXT_PUBLIC_OPENPANEL_CLIENT_ID`; Plausible requires both `NEXT_PUBLIC_PLAUSIBLE_DOMAIN` and `NEXT_PUBLIC_PLAUSIBLE_SCRIPT_URL`.
- Each provider returns `null` when its required public variable is absent. Therefore no analytics provider is active from the example configuration. Multiple configured providers coexist rather than selecting one.
- The visible OpenPanel options enable screen views, attributes, and outgoing-link tracking. No custom application event calls, server telemetry, consent mechanism, or privacy configuration were found.
- Status: `PRESENT`. Starter Action: `KEEP + TEST`. Default: `OFF` unless a provider's public configuration is supplied. Cloudflare: `COMPATIBLE` for these client/browser integrations.

## 3. Technical SEO

- `src/app/[locale]/layout.tsx` provides localized title, description, and keywords through the Next Metadata API. Landing, posts list, and post detail pages each add a canonical URL using `NEXT_PUBLIC_WEB_URL` and the `en` / non-`en` URL rule. Docs pages provide title and description metadata from MDX front matter.
- `src/app/layout.tsx` emits alternate language links and an `x-default` link. The current implementation uses `NEXT_PUBLIC_WEB_URL || ""`; absent or incorrect environment configuration can produce incorrect absolute metadata links.
- `public/robots.txt` is a static file that excludes query URLs and the two legal pages. `public/sitemap.xml` is static, contains only one URL, and retains `https://shipany.ai/` with a fixed 2024 timestamp. The robots file does not declare a sitemap location.
- No `metadataBase`, Open Graph, Twitter-card, JSON-LD, dynamic sitemap/robots route, staging noindex branch, or structured-data helper was found in source search. Canonical metadata is therefore present but incomplete across the technical SEO surface.
- Status: `PARTIAL`. Starter Action: `PATCH`. Default: `NOT_APPLICABLE`. Cloudflare: `LIKELY_COMPATIBLE_NEEDS_VERIFICATION`; the observed Metadata API and static assets are runtime-neutral, but the absent Workers deployment path prevents an end-to-end claim.

## 4. i18n / next-intl

- `next-intl` is configured through `next.config.mjs`, `src/middleware.ts`, `src/i18n/routing.ts`, and `src/i18n/request.ts`. The configured locales are `en` and `zh`; `en` is the default; locale prefix is `as-needed`.
- `NEXT_PUBLIC_LOCALE_DETECTION === "true"` controls browser locale detection, and `.env.example` sets it false. Detection is therefore off by default, but i18n itself is structurally active: the App Router is under `src/app/[locale]`, middleware always invokes `createMiddleware(routing)`, root/locale layouts read next-intl state, and client/server components import next-intl APIs.
- English and Chinese root-message files plus landing, pricing, and showcase page JSON resources are present. `request.ts` falls back invalid/missing locales and failed message imports to English.
- No `I18N_ENABLED` or equivalent module flag was found. Removing localization from a project would not be a clean configuration-only path today; it would still retain locale routing, middleware, providers, and translation imports. This is a confirmed optional-default gap, not a reason to remove i18n.
- Status: `PRESENT`. Starter Action: `PATCH`. Default: `ON` for locale routing; locale detection is `OFF` in the example. Cloudflare: `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` because next-intl middleware has no OpenNext/Workers smoke evidence.

## 5. AI providers

- Three public demo route handlers exist: `src/app/api/demo/gen-text/route.ts`, `gen-stream-text/route.ts`, and `gen-image/route.ts`. Each accepts caller-provided `prompt`, `provider`, and `model`; no operator-side default provider/model, allowlist, timeout, retry, rate limit, usage accounting, or authentication check was found in these handlers.
- OpenAI is supported in all three handlers through `@ai-sdk/openai`: text/stream handlers call `openai(model)` and image calls `openai.image(model)`. The repository does not construct that provider with an explicit key/base URL or document an OpenAI configuration variable in `.env.example`; SDK default configuration behavior is not established by repository code alone.
- Other provider cases are DeepSeek, OpenRouter, SiliconFlow-compatible, Replicate image, and custom Kling image/video. OpenRouter and SiliconFlow read server-only variable names in the routes. Kling reads `KLING_ACCESS_KEY` and `KLING_SECRET_KEY` in its provider. AUD-010 already established these and several AI variables are absent from `.env.example`.
- Streaming is present through `streamText(...).toDataStreamResponse`. The stream handler logs every chunk and completed text. The image handler stores generated images through `newStorage`; it catches upload failure and returns the provider/filename without a durable upload result.
- OpenAI status: `PARTIAL`; Starter Action: `PATCH`; Default: `OFF` (only invoked by a caller to a demo route); Cloudflare: `LIKELY_COMPATIBLE_NEEDS_VERIFICATION`.
- Other AI provider status: `PRESENT`; Starter Action: `PATCH`; Default: `OFF` as a product default, but the unauthenticated demo routes still allow a caller to select them; Cloudflare: `LIKELY_COMPATIBLE_NEEDS_VERIFICATION`. A small explicit provider/default policy is needed before they can be cleanly `KEEP-DISABLED`; deletion or a general provider refactor is not justified.

## 6. Storage / R2 suitability

- `src/lib/storage.ts` is an S3-compatible `aws4fetch` helper. It uses `STORAGE_ENDPOINT`, `STORAGE_REGION`, `STORAGE_ACCESS_KEY`, `STORAGE_SECRET_KEY`, `STORAGE_BUCKET`, and optional `STORAGE_DOMAIN`; the example configuration documents these names but supplies no values.
- It supports server-side `uploadFile` and `downloadAndUpload`; no direct browser upload/download API, signed URL, object listing, bucket binding, authorization policy, object-size policy, or general MIME validation was found. `src/app/api/demo/gen-image/route.ts` is the only observed caller and writes generated PNG bytes to a `shipany/` key with inline disposition.
- AWS Signature V4 plus a configurable endpoint is compatible in shape with an S3-compatible R2 endpoint. No R2 binding/configuration, R2 production evidence, or Cloudflare deployment configuration exists, so R2 support is not confirmed.
- The image route and storage helper use the Node `Buffer` global (`Buffer.from` and `body instanceof Buffer`). That requires a Workers/OpenNext compatibility check or a bounded byte-conversion patch before the image-to-storage path can be asserted portable. The helper otherwise uses `fetch`, `Request`, `Uint8Array`, and `aws4fetch`.
- Status: `PARTIAL`. Starter Action: `PATCH`. Default: `OFF` when storage variables are absent, although an invoked image route catches upload failure rather than rejecting up front. Cloudflare: `LIKELY_COMPATIBLE_NEEDS_VERIFICATION`.

## 7. Turnstile / bot protection

- Repository-wide searches for Turnstile, CAPTCHA, hCaptcha, reCAPTCHA, Cloudflare challenge, widget, and corresponding environment names found no implementation, dependency, client widget, server validation route, or configuration entry.
- Status: `ABSENT` and a confirmed gap for the optional module. Starter Action: `PATCH`. Default: `OFF`. Cloudflare: `NOT_APPLICABLE` until an implementation is selected. Its absence is not a V1 Core blocker.

## 8. Related content and SaaS capability mapping

- Fumadocs/MDX content is present in `content/docs/`, with docs route generation and search endpoint under `src/app/[locale]/(docs)` and `src/app/api/docs/search/route.ts`. The docs page has static params plus title/description metadata. Deeper content publication, UI, and runtime audit remains outside this task's optional-infrastructure depth.
- API-key models/services and authenticated console pages are present. Affiliate/invite models, services, routes, and console pages are present; their paid-order update path is covered by AUD-040. Dashboard, pricing, console, and admin routes are present but UI keep-list decisions remain reserved for AUD-060.
- These existing surfaces are retained without redesign recommendation. Their security, payment correctness, and UI behavior remain bounded by AUD-040, AUD-060, and AUD-070 rather than being re-audited here.

## 9. Environment and clean-disable evidence

| Capability | Environment/config evidence | Missing config behavior | Cleanly optional today? |
|---|---|---|---|
| AdSense | `NEXT_PUBLIC_GOOGLE_ADCODE` | Script returns `null`; root meta absent when unset | Yes |
| Analytics | provider-specific `NEXT_PUBLIC_*` identifiers | Each provider returns `null`; wrapper is production-only | Yes |
| SEO | `NEXT_PUBLIC_WEB_URL` | Canonical/alternate URLs can fall back to empty base | No, configuration correctness is required |
| i18n | `NEXT_PUBLIC_LOCALE_DETECTION` | Detection defaults false, but next-intl routing remains active | No |
| OpenAI | no explicit repo-side key/base-url construction or documented variable | A caller can reach demo route; provider configuration failure is caught generically | No |
| Other AI | `OPENROUTER_API_KEY`, `SILICONFLOW_API_KEY`, `SILICONFLOW_BASE_URL`, `KLING_ACCESS_KEY`, `KLING_SECRET_KEY` | A caller can select a provider even when unconfigured | No |
| Storage | `STORAGE_*` variables | Invoked upload fails for a missing bucket; image route catches failure | No |
| Turnstile | none | No module exists | Not applicable |

## 10. Required module conclusions

| Module | Status | Starter Action | Default | Cloudflare |
|---|---|---|---|---|
| AdSense | PRESENT | KEEP + TEST | OFF | COMPATIBLE |
| Analytics | PRESENT | KEEP + TEST | OFF | COMPATIBLE |
| Technical SEO | PARTIAL | PATCH | NOT_APPLICABLE | LIKELY_COMPATIBLE_NEEDS_VERIFICATION |
| i18n | PRESENT | PATCH | ON | LIKELY_COMPATIBLE_NEEDS_VERIFICATION |
| OpenAI | PARTIAL | PATCH | OFF | LIKELY_COMPATIBLE_NEEDS_VERIFICATION |
| Other AI providers | PRESENT | PATCH | OFF | LIKELY_COMPATIBLE_NEEDS_VERIFICATION |
| Storage | PARTIAL | PATCH | OFF | LIKELY_COMPATIBLE_NEEDS_VERIFICATION |
| Turnstile | ABSENT | PATCH | OFF | NOT_APPLICABLE |

Optional-module minimal-delta conclusion: YES — PATCH.

KEEP and KEEP + TEST are sufficient for the environment-gated browser script integrations. They are insufficient for the confirmed technical SEO gaps, structural i18n default, caller-controlled AI/provider configuration, and storage portability/configuration gaps. Bounded patches can address those findings; no REFACTOR or DELETE action is recommended.

## Findings Table

| Module / Capability | Existing implementation | Existing files | Current behavior | Starter planned role | Required behavior | Gap | Action | Default enabled? | Tests today | Tests required | Cloudflare compatibility | Risk | Reason | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AdSense | Production-only external loader plus account meta | `src/providers/adsense.tsx`, `src/providers/theme.tsx`, `src/app/layout.tsx`, `.env.example` | Returns null without public code; mounted in theme provider | V1 production ads path | Load only when configured and verify deployment/consent expectations | No ad-unit/consent evidence; production browser behavior untested | KEEP + TEST | OFF | NO EVIDENCED TEST | Unset/set config, production-only loader, account meta, consent policy tests | COMPATIBLE | Medium | Existing narrow loader is reusable; no abstraction needed | Source env guards and mount path |
| Analytics | Google Analytics, OpenPanel, Plausible | `src/components/analytics/*`, `src/providers/theme.tsx`, `.env.example` | Production-only; each provider independently env-gated and can coexist | Optional telemetry | Enable selected configured providers without loading when unset | No consent, server telemetry, or custom-event evidence | KEEP + TEST | OFF | NO EVIDENCED TEST | Provider unset/set, production gating, pageview, multi-provider, consent tests | COMPATIBLE | Medium | Browser integrations are separately fail-closed when unconfigured | Provider components and public config reads |
| Technical SEO | Locale metadata, selected canonicals, static robots/sitemap | App/locale layouts, landing/posts/docs pages, `public/robots.txt`, `public/sitemap.xml` | Metadata/canonicals cover selected routes; sitemap retains one old URL | Reusable technical SEO baseline | Correct base URL, route coverage, crawl controls, social/structured metadata | Static stale sitemap; no metadata base, social, JSON-LD, noindex, or dynamic route coverage | PATCH | NOT_APPLICABLE | NO EVIDENCED TEST | Metadata, canonical, alternate, robots/sitemap, staging-noindex tests | LIKELY_COMPATIBLE_NEEDS_VERIFICATION | High | Focused metadata/crawl patch is smaller than redesign | Metadata functions, static files, `NEXT_PUBLIC_WEB_URL` use |
| i18n | next-intl plugin, middleware, locale routes/resources | `next.config.mjs`, `src/middleware.ts`, `src/i18n/*`, `src/app/[locale]/*` | `en`/`zh`, English fallback, as-needed URLs; detection defaults false | Supported/tested optional module | Allow i18n to be default off without forcing locale infrastructure | No module enable flag; routing/middleware/provider/imports are structural | PATCH | ON; detection OFF | NO EVIDENCED TEST | Default route, locale switch, fallback, disabled configuration, middleware/SEO tests | LIKELY_COMPATIBLE_NEEDS_VERIFICATION | High | Preserve existing implementation and add bounded optionality path | Routing, request fallback, mandatory layout/middleware imports |
| OpenAI | AI SDK text, stream, image provider cases | Demo AI routes, `package.json` | Caller supplies model/provider; no explicit default/operator policy | Standard V1 AI path | Explicit OpenAI standard path with controlled model/configuration | No repo-side documented OpenAI config, allowlist, auth, timeout, or accounting | PATCH | OFF | NO EVIDENCED TEST | Config absence, selected model, bad input, error, stream, auth/rate-limit tests | LIKELY_COMPATIBLE_NEEDS_VERIFICATION | High | Existing OpenAI cases can be retained; policy/config patch is bounded | `openai(model)` / `openai.image(model)` route cases |
| Other AI providers | DeepSeek, OpenRouter, SiliconFlow, Replicate, custom Kling | Demo routes, `src/aisdk/kling/*`, `package.json` | Request parameter selects provider/model; Kling custom provider reads server secrets | Preserve non-default providers safely | Retain without making unconfigured providers reachable by default | No config policy; missing-variable docs; custom Kling uses Buffer | PATCH | OFF as product default | NO EVIDENCED TEST | Provider opt-in, missing secrets, allowed model, stream/image/Kling error tests | LIKELY_COMPATIBLE_NEEDS_VERIFICATION | High | A policy/config patch enables later KEEP-DISABLED behavior; no provider removal/refactor justified | Route switches, provider env reads, Kling client |
| S3-compatible storage / R2 suitability | AwsClient signed PUT helper and download-then-upload | `src/lib/storage.ts`, image demo route, `.env.example` | Configurable endpoint/bucket; generated images write a fixed prefix | Optional R2/storage | Configurable S3/R2 operation with validated safe upload behavior | No R2 binding, direct upload/read flow, validation, signed URLs, or Worker smoke; Buffer dependency | PATCH | OFF | NO EVIDENCED TEST | Missing config, upload/read, S3/R2 endpoint, object privacy, size/type, Worker bytes tests | LIKELY_COMPATIBLE_NEEDS_VERIFICATION | High | S3 signature shape supports a narrow R2 compatibility path without replacement | `aws4fetch`, `STORAGE_*`, Buffer use, sole image caller |
| Turnstile | No implementation found | Repository-wide source/dependency/env search | No widget or server verification path | Optional bot protection | Opt-in protected-form verification when a later requirement selects it | Confirmed optional-module absence | PATCH | OFF | NO EVIDENCED TEST | Disabled bypass, valid/invalid/expired token, protected-route tests | NOT_APPLICABLE | Low | Optional absence is not a Core blocker; no deletion/refactor question exists | No search matches outside audit documents |
| Docs / MDX content | Fumadocs content, docs route, search endpoint | `content/docs/*`, docs route/layout, docs search route | Localized MDX docs and generated static params | Preserve optional content capability | Retain while later UI/runtime tests assess it | Detailed UI/content workflow is outside this task | KEEP + TEST | ON | NO EVIDENCED TEST | Docs route, locale, metadata, search, build/runtime tests | LIKELY_COMPATIBLE_NEEDS_VERIFICATION | Medium | Existing content capability is reusable and does not require redesign here | Fumadocs route/source files |
| API keys and affiliate/invites | Models/services/routes and console pages | `src/models/apikey.ts`, `src/services/apikey.ts`, affiliate/invite files, console routes | Existing authenticated optional SaaS surfaces; affiliate paid-order behavior references AUD-040 | Preserve for product-specific opt-in | Security/payment/UI verification in owning workstreams | No default feature boundary was found in this audit | KEEP + TEST | ON in console navigation | NO EVIDENCED TEST | API-key lifecycle/security, invite/affiliate, console visibility tests | LIKELY_COMPATIBLE_NEEDS_VERIFICATION | High | Keep the existing surfaces pending AUD-060/070 and AUD-040 findings | Route/model/service references; no re-audit performed |
| Dashboard / pricing surfaces | Console/admin routes and pricing blocks | `src/app/[locale]/(default)/(console)`, `(admin)`, pricing pages/components | Present application surfaces | Reuse candidates | UI foundation decision remains A-002/AUD-060 | This audit does not determine UI keep list | KEEP + TEST | ON | NO EVIDENCED TEST | Route/access/render/responsive tests in owning audits | NOT_APPLICABLE | Medium | Retain evidence only; no UI architecture action is authorized here | Inventory route map and layout/component imports |

## Verification notes

- No test framework, test script, test directory, or test/spec file was found in the repository.
- No REFACTOR or DELETE action is recommended. PATCH items are bounded to optional enablement/default policy, technical SEO completeness, AI configuration/access policy, storage portability/configuration, and an absent optional Turnstile module.
- No application/module/config implementation file was changed during AUD-050.
