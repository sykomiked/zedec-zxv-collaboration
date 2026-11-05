# White paper — Backstop — NEAR Intents Coverage Layer

**Recipient:** `bhft11.tg`
**Contact:** https://nearbuilders.org/builders/bhft11.tg
**Their project:** Backstop — NEAR Intents Coverage Layer (`backstop-near-intents-coverage-layer-tysl8f`)
**Tier:** 1
**From:** `jollydragonroger.near` — ZEDEC/ZXV

---

## What you are building

Opt-in, parametric protection for individual NEAR Intents transactions. When a
user moves meaningful value across chains, there is settlement risk underneath
the abstraction. Backstop prices and covers it.

Coverage is a bet on an outcome. **The hard part is not pricing — it is proving
what happened when the outcome is contested.**

## The problem your design will hit

A parametric product needs a resolver. When a transaction settles cleanly, the
payout is obvious. When it half-settles — the source chain debited, the
destination chain did not credit, or two attestations disagree — a conventional
system has to pick a winner.

Every option it has is bad:

- **Last writer wins** — one attestation is silently discarded
- **Majority wins** — a 2-of-3 can be wrong together
- **Timelock then default** — the default is arbitrary and someone loses

All three destroy the evidence that the system was uncertain. For a coverage
product, that is the difference between paying a valid claim and denying one.

## What we have

A settlement core where **contradiction is a state, not an error**:

| Verdict | Meaning | Releases value |
|---|---|---|
| `TRUE` | verified, consistent | **yes** |
| `FALSE` | refuted | no |
| `BOTH` | two valid claims that conflict | **no — held** |
| `NEITHER` | nothing verifiable | no |

Only `TRUE` settles. `BOTH` means the system records that it cannot decide and
stops, rather than choosing.

This is exactly the primitive a coverage layer needs. "Neither chain can prove
settlement" is `NEITHER`. "Both attestors claim success but disagree on amount"
is `BOTH`. Neither should trigger an automatic payout **or** an automatic
denial — both should hold, visibly, with the contradiction preserved.

Alongside it:

| | |
|---|---|
| `chiglet.unog.near` | attested bridge, 3-of-5 quorum, **immutable per-chain caps** |
| `chancery.unog.near` | attestation registry, sealed |
| `unog.near` | the sealed core, 151 ops, zero access keys |

## How it integrates

**Option A — use our verdict evaluator as your resolver.**

```
contract : unog.near
verdicts : TRUE / FALSE / BOTH / NEITHER
rule     : only TRUE releases
```

Your policy contract reads the verdict and pays only on `TRUE`. On `BOTH` or
`NEITHER` it holds and emits an event. No judgement call, no arbitrary default.

**Option B — use our bridge as the settlement rail.** `chiglet.unog.near`
already locks value on NEAR, attests 3-of-5, and mints on five chains with an
immutable cap. A coverage product needs exactly that: a rail whose maximum loss
is bounded in advance.

**Option C — use `chancery.unog.near` as the evidence store.** Attestations are
recorded and sealed; a claim can cite them without trusting the claimant.

## Why this is worth your time

- **Your hardest engineering problem already has an implementation.** The
  four-valued resolver is live, sealed and verifiable — not a design document.
- **The cap model bounds your exposure.** An outpost cannot mint beyond its
  immutable ceiling, so your worst-case payout is computable before you write a
  policy.
- **`BOTH` is a feature for an insurer.** It is the case you must not resolve
  automatically, and it is the case most systems cannot represent.
- **You get a differentiator.** "Our resolver can prove it was uncertain" is a
  stronger claim than "our resolver is fast".

## What we are asking

A conversation about whether the four-valued verdict is the right resolution
semantics for your policies. If it is, we will document the exact call shapes
for your team.

We are not asking for capital or a commitment. We are pointing out that the
piece you would otherwise have to build exists, is sealed, and has a published
binary.

## Proof

```
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/ARCHITECTURE.md      the four-valued state machine
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/TRANSACTION_FLOWS.md bridge sequence with real tx ids
https://nearblocks.io/address/unog.near
```

---

## Ready-to-send message

```
Hi — you're building parametric coverage for cross-chain intents, which means your hard problem is resolution: proving what happened when a transfer half-settles.

That problem has an implementation already. unog.near evaluates every claim to four values — TRUE, FALSE, BOTH, NEITHER — and only TRUE releases value. When two valid attestations conflict, it records BOTH and holds instead of picking a winner. That's precisely the case an insurer must not resolve automatically.

Alongside it, chiglet.unog.near is an attested bridge with immutable per-chain caps, so your worst-case payout is computable before you write a policy.

Happy to document the call shapes if the semantics fit.

Detail: https://github.com/sykomiked/zedec-zxv-deployment
```
