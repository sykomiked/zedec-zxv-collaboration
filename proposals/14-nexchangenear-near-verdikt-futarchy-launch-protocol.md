# White paper — Verdikt — futarchy launch protocol

**Recipient:** `nexchangenear.near`
**Contact:** https://nearbuilders.org/builders/nexchangenear.near
**Their project:** Verdikt — futarchy launch protocol (`verdikt-2u8yhy`)
**Tier:** 2
**From:** `jollydragonroger.near` — ZEDEC/ZXV

---

## What you are building

Conditional prediction markets decide whether an ICO launches, instead of the
owner deciding alone. A futarchy primitive for NEAR.

Futarchy has one unsolved failure: **what happens when the market cannot
resolve cleanly?**

## The resolution problem

A conditional market resolves on an event. Real events produce:

- clean resolution — the event happened or it did not
- **ambiguous resolution** — two credible oracles disagree
- **unresolvable** — the event's definition does not fit what occurred

Conventional markets handle the first and improvise the rest: an admin decides,
or the market resolves `50/50`, or it is voided. All three destroy the
information that the outcome was unclear — which is precisely the information a
futarchy needs, because the whole point is that the market knows better than the
owner.

## What we have

A four-valued evaluator built for this:

| Verdict | Meaning | Market action |
|---|---|---|
| `TRUE` | event verified | resolve YES |
| `FALSE` | event refuted | resolve NO |
| `BOTH` | two valid, conflicting oracles | **hold — do not resolve** |
| `NEITHER` | cannot verify | hold |

Only `TRUE` and `FALSE` resolve. `BOTH` and `NEITHER` hold, visibly, with the
conflict recorded. That is the honest outcome and it is the one futarchy
requires: **an unresolvable market must not manufacture a resolution**, because
a manufactured resolution is exactly the central authority futarchy exists to
remove.

## How it integrates

**Step 1 — oracle claims become verdicts.** Each oracle's report is a claim.
Two credible reports that disagree → `BOTH`.

**Step 2 — resolution gates on the verdict.** `TRUE`/`FALSE` resolve; `BOTH` and
`NEITHER` hold and emit an event.

**Step 3 — record the verdict on-chain.** `chancery.unog.near` is a sealed
attestation registry — the resolution history cannot be rewritten after the
fact, which is the only way a market's track record means anything.

**Step 4 — optionally, run the market inside `unog.near`.** Sealed execution
means the market operator cannot override a resolution.

## Why this is worth your time

- **It closes futarchy's biggest hole.** "The market decides" only works if the
  market can decline to decide.
- **It is philosophically consistent.** A protocol whose premise is removing
  central authority cannot resolve ambiguity by appointing an admin. `BOTH` is
  the only answer that does not reintroduce one.
- **The primitive is implemented and sealed.**
- **A genuine differentiator.** Every other prediction market resolves by
  admin, oracle majority, or void.

## What we are asking

Consider four-valued resolution instead of a binary with an admin fallback. If
it fits, we will document the calls.

## Proof

```
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/ARCHITECTURE.md#4-the-four-valued-state-machine
```

---

## Ready-to-send message

```
Hi — Verdikt uses conditional markets to decide whether an ICO launches. That's the right use of futarchy, but it has one unsolved case: what happens when the market can't resolve cleanly?

Real events produce ambiguity — two credible oracles disagree, or the event's definition doesn't fit what happened. Conventional markets improvise: admin decides, resolve 50/50, or void. All three destroy the information that the outcome was unclear, which is exactly what futarchy is supposed to capture.

I built a four-valued evaluator: TRUE, FALSE, BOTH, NEITHER. Only TRUE and FALSE resolve; BOTH and NEITHER hold and record the conflict.

A protocol whose premise is removing central authority can't resolve ambiguity by appointing an admin. BOTH is the only answer that doesn't reintroduce one.

Detail: https://github.com/sykomiked/zedec-zxv-deployment
```
