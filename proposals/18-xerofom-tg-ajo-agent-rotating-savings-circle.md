# White paper — Ajo Agent — rotating savings circle

**Recipient:** `xerofom.tg`
**Contact:** https://nearbuilders.org/builders/xerofom.tg
**Their project:** Ajo Agent — rotating savings circle (`ajo-agent-e6nw04`)
**Tier:** 3
**From:** `jollydragonroger.near` — ZEDEC/ZXV

---

## What you are building

A rotating savings circle (ajo/esusu) run by a verifiable agent instead of a
trusted person. The social structure is centuries old; the trust problem is the
reason it stays informal.

## Where we might fit

A savings circle needs three things a general-purpose token does not provide:

1. **A unit whose supply cannot be inflated** — otherwise the circle's payout is
   diluted by whoever controls the mint
2. **A settlement record nobody can edit** — the whole point is removing the
   trusted treasurer
3. **A way to represent a dispute** — someone misses a contribution and claims
   they paid

## What we have

**PQOS** — collateral-backed issuance, **no admin mint**, contract sealed with
zero access keys. Supply is 61.47 because 61.47 was paid for. Nobody can print
more.

**`chancery.unog.near`** — sealed attestation registry, zero access keys.
Contributions recorded there cannot be edited after the fact.

**Four-valued settlement** — a disputed contribution is `BOTH`: two valid claims
that conflict, held and visible rather than resolved by whoever shouts loudest.

## The honest caveat

PQOS is illiquid and concentrated. A savings circle denominated in it would be
denominated in something hard to convert. **We are not recommending it as a
savings asset today.**

What we are offering is the *model*: a token with provable non-inflation, and a
registry that removes the treasurer. That is directly relevant to your problem
even if you use a different unit.

## How it could fit

**Option A — the model, not the token.** Use the sealed-registry pattern for
contribution records.

**Option B — four-valued contribution status.** Paid / missed / disputed /
unverifiable, with the disputed case held rather than resolved.

**Option C — a later integration.** If PQOS gains liquidity, a circle denominated
in a non-inflatable unit is a genuine improvement over one denominated in a
token someone can print.

## Why this is worth your time

- **The treasurer problem is an attestation problem.** A sealed registry removes
  the role entirely.
- **Disputes are the failure mode of every savings circle.** `BOTH` represents
  them honestly.
- **We are honest about the liquidity gap** rather than pitching a token nobody
  can sell.

## What we are asking

Look at the sealed-registry pattern for contribution records. The token is
optional; the pattern is the useful part.

## Proof

```
https://nearblocks.io/address/chancery.unog.near
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/WHITEPAPER_PQOS.md
```

---

## Ready-to-send message

```
Hi — Ajo Agent replaces the trusted treasurer with a verifiable agent. That's an attestation problem before it's a payments problem.

Three things a savings circle needs that a general token doesn't give you: a unit nobody can inflate, a settlement record nobody can edit, and a way to represent "someone claims they paid and the record disagrees".

I have the second and third: chancery.unog.near is a sealed registry with zero access keys, and my settlement core treats a disputed contribution as BOTH — two valid conflicting claims, held and visible, not resolved by whoever shouts loudest.

Honest caveat: my token PQOS has provable non-inflation (no admin mint, sealed) but it's illiquid and concentrated, so I'm not pitching it as a savings asset today. The registry pattern is the useful part.

Detail: https://github.com/sykomiked/zedec-zxv-deployment
```
