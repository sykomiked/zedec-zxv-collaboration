# White paper — Clearance — a crash test for AI agents that hold money

**Recipient:** `selliks.near`
**Contact:** https://nearbuilders.org/builders/selliks.near
**Their project:** Clearance — a crash test for AI agents that hold money (`clearance-a-crash-test-for-ai-agents-that-hold-money-mhjzgx`)
**Tier:** 2
**From:** `jollydragonroger.near` — ZEDEC/ZXV

---

## What you are building

You hide the scams that work on people in the data an agent reads — lookalike
payee, padded invoice, fake "payment failed, retry", email from a fake owner —
let the agent pay with real transfers, and score it by the money that left the
vault.

Your test is only as good as the venue. A sandbox lets you reset. **A sealed
contract does not.**

## Why we are a harder venue than a sandbox

`unog.near` has **zero access keys**. There is no admin function, no upgrade
path, no pause, no recovery. An agent that drains it cannot be helped by
anyone, including us.

That is a stronger crash test than a sandbox, because a sandbox teaches an agent
that mistakes are recoverable. They are not.

| | |
|---|---|
| `unog.near` | 1,156,670 B, 151 ops, zero keys |
| Balance model | internal 32-byte accounts, nonces, per-asset balances |
| Fee | 8.889 bps on routed transfers |
| Verdicts | `TRUE` / `FALSE` / `BOTH` / `NEITHER` |

## How it integrates

**Step 1 — add a sealed-venue scenario.** Same scam data, but the agent pays
into `unog.near`, which has no recovery path. Score the difference.

**Step 2 — use the four verdicts as a grading axis.** An agent that treats
`BOTH` or `NEITHER` as "probably fine" is dangerous. Our core distinguishes
them; your test can score whether the agent respects the distinction.

**Step 3 — test the refund trap.** Your scenario "payment failed, retry" maps
directly onto our bridge behaviour: an invalid message is **silently refunded**
with no error. An agent that does not notice a refund is as dangerous as one
that overpays.

**Step 4 — publish the result.** A Clearance certificate for an agent tested
against a contract with no admin key is a stronger claim than one tested
against a sandbox.

## Why this is worth your time

- **Harder test, better product.** "Tested against an ownerless contract" is a
  meaningful distinction.
- **You get an unusual venue.** Most test targets are permissive.
- **The refund trap is a real scenario you can lift.** It cost us a transaction
  to discover; it is free for you.
- **No integration cost.** Your agents just transact with a deployed contract.

## What we are asking

Add `unog.near` as a test venue, or at least consider the sealed-venue variant.
We will document the call shapes.

## Proof

```
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/TRANSACTION_FLOWS.md    includes the silent-refund failure
https://nearblocks.io/address/unog.near
```

---

## Ready-to-send message

```
Hi — Clearance scores agents by the money that left the vault. Your venue matters: a sandbox teaches an agent that mistakes are recoverable.

I run unog.near — 1.16MB, 151 operations, zero access keys. No admin, no upgrade, no pause, no recovery. An agent that drains it can't be rescued by anyone, including me. That's a harder crash test than a sandbox.

One scenario you can lift for free: our bridge silently refunds invalid messages with no error. An agent that doesn't notice a refund is as dangerous as one that overpays. It cost me a transaction to find.

Happy to document the call shapes if a sealed-venue variant is interesting.

Detail: https://github.com/sykomiked/zedec-zxv-deployment
```
