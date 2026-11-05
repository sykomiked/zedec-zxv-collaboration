# White paper — NEAR Intents Solver Reputation & Risk Network

**Recipient:** `ftxnear.near`
**Contact:** https://nearbuilders.org/builders/ftxnear.near
**Their project:** NEAR Intents Solver Reputation & Risk Network (`near-intents-solver-reputation-risk-network-r29ws5`)
**Tier:** 1
**From:** `jollydragonroger.near` — ZEDEC/ZXV

---

## What you are building

An open reputation and risk layer for NEAR Intents solvers — so users, wallets
and dApps can judge reliability before and during execution.

Reputation systems fail in a specific, predictable way: **two credible parties
disagree and the system is forced to pick one.** Whoever it picks is now wrong
about the other, and the score degrades silently.

## The failure mode, concretely

A solver completes 400 intents cleanly. One intent is contested:

- the solver has an attestation that it delivered
- the user has an attestation that it did not
- both are correctly signed

A conventional scoring system must choose. If it picks the user, the solver's
score drops on a possibly-false claim. If it picks the solver, the user is
marked as a bad actor. Either way, **the next reader cannot tell that the system
was ever uncertain** — the evidence is gone.

That is not a scoring bug. It is a representation failure.

## What we have

A settlement core with four verdicts, where contradiction has its own state:

| Verdict | Meaning | Effect |
|---|---|---|
| `TRUE` | verified, consistent | settles |
| `FALSE` | refuted | rejected |
| `BOTH` | two valid claims that conflict | **held, recorded** |
| `NEITHER` | nothing verifiable | held |

Plus a sealed attestation registry:

| | |
|---|---|
| `chancery.unog.near` | REGISTRAR — attestation tallies, 44,496 B, **0 access keys** |
| `unog.near` | the core, 151 ops, zero keys, code hash `Ae5uDVYK…` |
| `protocol.unog.near` | governance seat, sealed |

## How it integrates

**A three-valued score instead of a scalar.**

Most reputation systems output `0..100`. Yours can output a tuple:

```
reliability = (clean_fills, contested_fills, unverifiable_fills)
```

A solver with 400 clean and 3 `BOTH` is meaningfully different from one with
400 clean and 3 `FALSE`. A single number cannot express that; a four-valued
tally can.

**Step 1 — record attestations in `chancery.unog.near`.** Every claim about a
fill, by either party, with its verdict. Sealed, so the record cannot be edited
after the fact.

**Step 2 — evaluate conflicts with the core's tables.** Two valid claims →
`BOTH`. The registry stores it as `BOTH`, not as a win for either side.

**Step 3 — surface the tuple, not a score.** Downstream consumers decide how
much weight to give contested fills. That is their risk appetite, not yours.

**Step 4 — optionally, cite our bridge as a settlement reference.**
`chiglet.unog.near` already runs 3-of-5 attestation with immutable caps; its
tickets are a worked example of attestation under constraint.

## Why this is worth your time

- **You avoid the resolution trap.** The most common failure of reputation
  systems is forcing a winner on a genuine conflict. You do not have to.
- **Sealed registry means the record is credible.** `chancery.unog.near` has
  zero access keys — nobody, including us, can edit an attestation after the
  fact.
- **The tuple is a better product.** "3 contested fills" is more useful to a
  sophisticated consumer than "score 94".
- **You get a working resolver, not a spec.** The tables are implemented and
  live.

## What we are asking

Consider four-valued tallies instead of a scalar score. If the idea is useful,
we will document the registry calls and the verdict semantics so your team can
implement against them.

We are not asking to be the reputation layer. We are offering the resolution
primitive it needs.

## Proof

```
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/ARCHITECTURE.md#4-the-four-valued-state-machine
https://nearblocks.io/address/chancery.unog.near
```

---

## Ready-to-send message

```
Hi — solver reputation has one failure mode that kills most implementations: two credible parties disagree and the system has to pick a winner, destroying the evidence that it was uncertain.

I built a settlement core where that case has its own state. Four verdicts — TRUE, FALSE, BOTH, NEITHER — and only TRUE settles. Two valid conflicting attestations produce BOTH, which is held and recorded rather than resolved.

There's also chancery.unog.near, a sealed attestation registry with zero access keys, so records can't be edited after the fact.

The practical suggestion: emit a tuple (clean, contested, unverifiable) instead of a 0-100 score. "400 clean, 3 contested" says something a scalar can't.

Detail: https://github.com/sykomiked/zedec-zxv-deployment
```
