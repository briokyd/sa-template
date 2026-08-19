# Deletion Review Candidates

> Empty is a valid result. No deletion is authorized by this file.

> Task: `AUD-080`  
> Final result: **NO DELETE CANDIDATE**

## Decision

No verified workstream identified an object for which retention, `KEEP-DISABLED`, `WRAP`, or `PATCH` is insufficient. Therefore no Deletion Review is opened and no deletion is authorized.

## Retention Rationale

| Existing surface | Final Action | Why deletion is not justified |
|---|---|---|
| Vercel and Docker deployment | KEEP-DISABLED | Low-cost alternate paths do not conflict with Cloudflare-first |
| GitHub OAuth and Google One Tap | KEEP-DISABLED | Existing optional providers can stay off; activation risks are bounded |
| Credits and Stripe subscriptions | KEEP-DISABLED | Reusable product capabilities outside the one-time V1 default |
| Other AI providers | PATCH | Add explicit opt-in policy, then retain disabled; provider removal is unnecessary |
| Blog/docs/charts/editor/carousel | KEEP-DISABLED | Mature optional UI/content capabilities with future reuse value |
| API keys and affiliate/invite | KEEP-DISABLED | Product-specific surfaces can remain off pending domain security tests |
| Multiple icon systems, shells, hooks, wrappers | KEEP + TEST | Duplication/aesthetic preference is not deletion evidence |
| ShipAny-specific copy/assets/content | KEEP-DISABLED | Excluded from Starter Authority and replaced per product, but no repository deletion is required |

## Approval Boundary

Any later deletion must provide the full `AUDIT-001` Deletion Review fields and obtain explicit user approval. “Not Core in Starter V1” remains insufficient justification.
