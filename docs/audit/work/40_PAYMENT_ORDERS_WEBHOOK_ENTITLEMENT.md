# Payment / Orders / Webhook / Entitlement Audit

> Task: AUD-040
> Status: VERIFIED
> Authority: AUDIT-001

Scope: factual audit of existing orders, Stripe, Creem, callbacks, webhooks, subscriptions, credits, and paid-access paths. No payment/order/schema/application implementation, configuration, dependency, or secret value was changed or exposed.

## Audit boundary

The audited baseline is 503ca9a0f46bc732fe974b6d336e1d1fcd2eb8a4 on audit/kyd-starter-v1. AUD-020 established PostgreSQL/Drizzle and no evidenced transaction use; AUD-030 established the session-derived users.uuid identity. This workstream references those facts without re-auditing either system. The Runtime/bootstrap pack is pre-existing untracked state.

## 1. Orders and payment data model

- src/db/schema.ts defines orders with identity id and unique order_no. It persists user UUID/email, amount, interval, expiration, status, currency, product ID/name, credit count, payment timestamps/details, and subscription fields.
- stripe_session_id is the one provider-named column. Both Stripe and Creem write their checkout IDs through updateOrderSession. The name does not block the two current provider paths and is not a refactor justification.
- Statuses are created, paid, and deleted. The observed payment path creates created orders and transitions only to paid. No refund, cancellation, chargeback, expiry, or deletion state-transition handler was found.
- POST /api/checkout receives only product_id, currency, and locale from the client. It resolves the item from server-side locale pricing JSON, derives amount/interval/credits/product data there, and rejects unknown products/intervals. Client-side price/amount tampering is not evidenced in this path.
- A provider checkout failure after insertOrder leaves a created order. No failure/cancel update is implemented.

## 2. Provider selection and product configuration

- PAY_PROVIDER is an environment-variable-controlled checkout branch. Literal creem selects Creem; every other, absent, or unrecognized value selects Stripe. Selection is operator-controlled, not request-controlled, and no automatic failover exists.
- .env.example gives stripe as the default and declares Stripe private/webhook variables plus CREEM_ENV, API key, webhook secret, and CREEM_PRODUCTS. No values were inspected.
- Stripe creates server-side price_data from the server-resolved pricing item, embeds order/user/product/credits metadata, and stores the Checkout Session ID.
- Creem parses CREEM_PRODUCTS as a JSON mapping from local pricing product IDs to Creem product IDs. It sends the server-generated order_no as requestId, customer email, success URL, and the same metadata. Invalid JSON or missing mapping throws after the order exists.
- The switch matches the frozen operator-controlled selection shape but needs a bounded configuration validation/test patch.

## 3. Stripe checkout, callback, and webhook

- stripeCheckout creates a card Checkout Session for one-time products or a subscription session for month/year pricing. It uses an explicit success URL containing Checkout Session ID and order number, then stores the session ID/detail.
- Browser callback /api/pay/callback/stripe retrieves the Checkout Session with server credentials and delegates to handleCheckoutSession. The query order_no is required but the update derives the actual order from signed provider session metadata.
- Webhook /api/pay/notify/stripe reads raw text and calls stripe.webhooks.constructEventAsync with stripe-signature and STRIPE_WEBHOOK_SECRET. It handles checkout.session.completed and invoice.payment_succeeded; other events return success after a log.
- handleCheckoutSession rejects non-paid sessions and calls updateOrder for one-time payments. For subscriptions it retrieves/updates subscription metadata and calls updateSubOrder.
- No refund, cancellation, dispute, or payment-failure event handling was found. Signature acceptance, success/cancel redirects, and live/test credentials were not executed.

## 4. Creem checkout, callback, and webhook

- newCreemClient selects production or test API host from CREEM_ENV, falling back to NODE_ENV, and requires CREEM_API_KEY.
- creemCheckout sends mapped product ID, internal order number as requestId, customer email, and metadata. Its success URL supplies only locale; callback correctness depends on Creem appending expected checkout_id and request_id parameters, which was not verified.
- Browser callback /api/pay/callback/creem retrieves the checkout using the server API key, requires matching request ID and a paid provider order, then calls updateOrder. It does not trust query values alone.
- Webhook /api/pay/notify/creem reads raw text, computes SHA-256 HMAC through Web Crypto, compares the creem-signature header, parses JSON, and handles only checkout.completed with a paid order and metadata order number.
- The repository does not prove header format, signature algorithm requirements, timing-safe comparison, retry behavior, or real provider delivery. Creem has an evidenced one-time checkout/callback/notify chain, but needs staging verification and focused patching before production readiness.

## 5. Webhook idempotency and atomicity

Webhook idempotency status: PARTIAL.

- updateOrder reads unique order_no and returns when status is already paid. Ordinary sequential duplicate callback/webhook delivery therefore does not repeat later side effects.
- It updates the order to paid before updateCreditForOrder and updateAffiliateForOrder. AUD-020 found no Drizzle transaction call. If a credit or affiliate write fails after the status update, retry sees paid and returns, leaving dependent state incomplete.
- Concurrent deliveries can both read created before either update. Credits and affiliate idempotency are read-before-insert checks only: findCreditByOrderNo and findAffiliateByOrderNo have no corresponding unique database constraints. Concurrent grants are not proven safe.
- Neither webhook stores a provider event ID or processed-event record. Authentication is not replay accounting.
- The smallest future delta is a bounded transaction/idempotency patch for state transition plus credit/affiliate side effects, coordinated with AUD-020. A schema-wide payment redesign is not justified.

## 6. Paid access, entitlement, and credits

Durable paid-access / entitlement status: PARTIAL.

- Durable paid-order records are present: user order pages query orders with status paid; getUserCredits sets is_recharged if a first paid order exists.
- Credits are a durable ledger-like table with unique trans_no, user UUID, transaction type, signed amount, optional order number, and expiry. updateCreditForOrder creates a positive order_pay row when an order has credits; decreaseCredits adds a negative record and valid-credit reads sum non-expired rows.
- getUserCredits derives is_pro from a positive valid-credit balance. There is no separate generic entitlement/access table, feature-unlock policy, or refund/revocation behavior.
- Credits are visible in the current console and current pricing products, but are not frozen as Starter V1 Core. The default Starter recommendation is KEEP-DISABLED: preserve this reusable capability and enable it only for products requiring credit metering.

## 7. Subscription implementation

- Stripe has current month/year checkout, first payment, invoice renewal, renewal-order, subscription metadata, and billing-portal code.
- Creem checkout sends no interval/subscription behavior in the audited code. Provider equivalence is not evidenced for subscriptions.
- Subscription is outside frozen V1 one-time scope. Existing Stripe subscription functionality should remain KEEP-DISABLED, not removed, pending lifecycle testing.

## 8. Payment security and Cloudflare/OpenNext implications

- Stripe webhook uses provider SDK signature construction against raw body. Creem webhook uses Web Crypto crypto.subtle over raw body, which is Worker-native in principle. Neither endpoint declares a Node runtime.
- Stripe SDK, Creem SDK, database connection, raw-body preservation, provider calls, and OpenNext deployment have no Cloudflare smoke evidence. Status is LIKELY_COMPATIBLE_NEEDS_VERIFICATION, not confirmed incompatibility.
- Payment callbacks log complete provider session/result objects, and checkout logs the parsed Creem products map. Secret redaction and production log policy are payment-security observations deferred to AUD-070.
- Success/failure/cancel URLs come from public environment variables. Callback URLs are server-constructed, but environment-specific URL correctness and redirect behavior require integration tests.

## 9. Required payment conclusions

- Minimal-delta payment conclusion: YES — PATCH. Existing Creem one-time, Stripe one-time, and PAY_PROVIDER selection are present. KEEP, KEEP + TEST, and WRAP cannot address confirmed partial idempotency and state consistency; bounded patches plus tests are sufficient, so no REFACTOR is justified.
- Webhook idempotency: PARTIAL.
- Durable paid-access / entitlement: PARTIAL.
- Credits default Starter role: KEEP-DISABLED.

## Findings Table

| Module / Capability | Existing implementation | Existing files | Current behavior | Starter planned role | Required behavior | Gap | Action | Default enabled? | Tests today | Tests required | Cloudflare compatibility | Risk | Reason | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Orders lifecycle and server pricing | Unique order number, user/product/amount/currency/credits/status fields; server pricing lookup | src/db/schema.ts, src/models/order.ts, src/app/api/checkout/route.ts, src/services/page.ts, pricing JSON | Creates a created order from server-derived pricing before provider checkout; observed transition is to paid only | Reuse order record for one-time payment | Server-authoritative price and coherent provider outcome state | Checkout failure/cancel/refund lifecycle is not represented | PATCH | Yes | NO EVIDENCED TEST | Invalid product/currency, provider failure, cancel, paid-state, and order-history tests | LIKELY_COMPATIBLE_NEEDS_VERIFICATION | High | Existing model supports both providers; focused lifecycle completion is smaller than schema replacement | Checkout validation, order enum/model, pricing JSON |
| Operator provider switch | PAY_PROVIDER checkout branch | src/app/api/checkout/route.ts, .env.example | Literal creem selects Creem; all other/missing values select Stripe; no request input or failover | Operator-controlled active provider | Validated selected provider with no automatic failover | Invalid values silently select Stripe; no provider-switch tests | PATCH | Stripe default in example config | NO EVIDENCED TEST | Stripe/Creem selection, invalid config, and no-failover tests | NOT_APPLICABLE | Medium | Environment switch already matches direction; add narrow validation rather than architecture change | PAY_PROVIDER branch and env example |
| Stripe one-time checkout and callback | Server-created Checkout Session, metadata, provider retrieval callback | checkout route, integrations/stripe, callback/stripe route, services/stripe | Uses server pricing/metadata and retrieves provider session before handling paid one-time order | V1 production one-time provider | Successful checkout and callback create one durable paid result | Side effects share partial idempotency/atomicity gap; provider flow not staged | PATCH | Selected unless PAY_PROVIDER is creem | NO EVIDENCED TEST | Checkout success/failure, paid/unpaid callback, metadata/order match, duplicate callback tests | LIKELY_COMPATIBLE_NEEDS_VERIFICATION | High | Existing path is complete enough to retain; narrow correctness tests/patches required | Stripe checkout options, callback retrieval, handleCheckoutSession |
| Stripe webhook signature and events | Raw-body Stripe SDK verification; handles checkout and invoice success | src/app/api/pay/notify/stripe/route.ts, src/services/stripe.ts | Calls constructEventAsync and returns 500 on failure | V1 production one-time webhook | Verify signature and safely process retry/duplicate events | No event ledger; no refund/cancel/dispute handling; no tests | PATCH | Endpoint active when configured | NO EVIDENCED TEST | Invalid signature, replay, duplicate, handler failure/retry, and event-filter tests | LIKELY_COMPATIBLE_NEEDS_VERIFICATION | High | Signature foundation exists; bounded idempotency/event handling is sufficient | Raw body/signature code and handled event switch |
| Creem one-time checkout and callback | Creem client, product map, request ID, provider retrieval callback | integrations/creem, checkout route, callback/creem route | Uses server product map and retrieves paid checkout before updating order | V1 production one-time provider | Configured product mapping and verified paid callback | Product-map JSON/missing mapping leaves created order; query injection assumptions not staged | PATCH | Only when PAY_PROVIDER is creem | NO EVIDENCED TEST | Mapping, test/live env, checkout creation, callback parameters/status, and failure tests | LIKELY_COMPATIBLE_NEEDS_VERIFICATION | High | One-time path exists; focused configuration/lifecycle patch is sufficient | Creem client host selection, CREEM_PRODUCTS, retrieve-checkout callback |
| Creem webhook signature and events | Raw-body HMAC with Web Crypto; handles paid checkout.completed | src/app/api/pay/notify/creem/route.ts | Computes SHA-256 HMAC and string-compares header before JSON/event handling | V1 production one-time webhook | Provider-correct signature and retry-safe processing | Header/algorithm and timing-safe behavior unverified; no event ledger/tests | PATCH | Endpoint active when configured | NO EVIDENCED TEST | Valid/invalid signature, replay, duplicate, payload/schema, and retry tests | LIKELY_COMPATIBLE_NEEDS_VERIFICATION | High | Web Crypto approach is reusable; narrow verification/comparison/idempotency work is smaller than refactor | generateSignature, raw body/header checks, event switch |
| Webhook idempotency and transaction boundary | Status guard plus read-before-insert credits/affiliate checks | services/order.ts, services/credit.ts, services/affiliate.ts, models/schema | Sequential already-paid delivery returns; order status update precedes credit/affiliate writes | One event causes one consistent paid result | Atomic state transition and exactly-once side effects under replay/retry/concurrency | Confirmed partial behavior: no transaction/event ledger; partial failure and concurrent races can be inconsistent | PATCH | Yes for paid flows | NO EVIDENCED TEST | Sequential/concurrent duplicate, crash-after-status, credit/affiliate failure, and retry tests | LIKELY_COMPATIBLE_NEEDS_VERIFICATION | High | Bounded transaction/idempotency patch addresses demonstrated risk; no general payment redesign needed | updateOrder; no transaction search; no order-level credit/affiliate unique constraint |
| Paid access and entitlement | Paid order queries plus credits-derived flags | models/order.ts, services/credit.ts, order/credit console pages | Paid orders are durable; is_recharged and is_pro derive from paid orders/valid credits | Durable one-time purchase ownership and optional metering | Queryable paid state and explicit product access policy | No generic entitlement/revocation/refund handling | PATCH | Paid orders/credits visible in current UI | NO EVIDENCED TEST | Paid ownership, access decision, expiry, refund/revocation, and entitlement tests | LIKELY_COMPATIBLE_NEEDS_VERIFICATION | High | Existing durable records can support a thin access policy; a new framework is not evidenced | Paid-order lookups, getUserCredits, absent entitlement table/service |
| Credits ledger | Credits table, order grant, consumption entries, console/API display | schema, models/credit.ts, services/credit.ts, api/get-user-credits | Grants positive order_pay credits and sums non-expired signed rows; consumes by negative entries | Optional Starter metering | Preserve available capability without making it mandatory | Grant correctness shares idempotency/transaction gap; not frozen as Core | KEEP-DISABLED | Yes in current pricing/console; recommended default disabled | NO EVIDENCED TEST | Grant/consume/expiry/double-grant/concurrent-balance tests | LIKELY_COMPATIBLE_NEEDS_VERIFICATION | Medium | Reusable feature should remain optional; no deletion or redesign needed | Credit schema/service and console paths |
| Stripe subscriptions | Month/year checkout, invoices, renewal orders, billing portal | checkout route, services/stripe and order, models/order | Stripe subscription paths create/renew orders and grant credits; Creem equivalent not evidenced | Outside V1 one-time default | Preserve without default activation | Lifecycle/refund/cancel/retry tests and provider parity absent | KEEP-DISABLED | Present in current pricing | NO EVIDENCED TEST | First charge, renewal, duplicate invoice, cancellation, refund, and portal tests | LIKELY_COMPATIBLE_NEEDS_VERIFICATION | High | Existing code can remain disabled; lack of V1 requirement is not deletion evidence | Month/year pricing, invoice handler, billing portal function |
| Payment logging and runtime | Stripe/Creem SDKs, Web Crypto HMAC, database and public URLs | Payment routes/services/integrations, .env.example | Logs provider session/results and product map; no Node runtime declaration | Cloudflare-first payment path | Redacted logs and verified Worker raw-body/SDK behavior | No OpenNext/Worker/provider smoke tests; log redaction not evidenced | PATCH | Yes when payment configured | NO EVIDENCED TEST | Cloudflare checkout/webhook smoke, raw body, SDK crypto, and redaction tests | LIKELY_COMPATIBLE_NEEDS_VERIFICATION | High | No confirmed incompatibility; focused runtime/logging verification and patches are required | Stripe raw-body SDK, Creem crypto.subtle, AUD-010/020 deployment facts |

## Verification notes

- No payment, webhook, integration, or database tests, test framework, or test script were found. No provider credentials, network calls, database calls, or deployment flows were executed.
- No REFACTOR or DELETE action is recommended. PATCH items are limited to observable lifecycle, provider configuration, webhook idempotency/atomicity, entitlement, and runtime/logging gaps.
