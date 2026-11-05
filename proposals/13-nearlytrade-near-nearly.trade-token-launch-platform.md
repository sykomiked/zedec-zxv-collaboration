# White paper — nearly.trade — token launch platform

**Recipient:** `nearlytrade.near`
**Contact:** https://nearbuilders.org/builders/nearlytrade.near
**Their project:** nearly.trade — token launch platform (`nearly-trade`)
**Tier:** 2
**From:** `jollydragonroger.near` — ZEDEC/ZXV

---

## What you are building

Tokens deploy with a concentrated liquidity pool on Rhea and are tradable
immediately. A launch venue that removes the "deploy and hope" gap.

We are a token that launched **without** a venue, and the consequences are
instructive.

## What happened to us

PQOS launched with collateral-backed issuance — no premine, no ICO, no team
allocation. Every token was bought with NEAR.

The result:

| | |
|---|---|
| Supply | 61.47 PQOS |
| Holder concentration | 93.6% one wallet |
| First pool depth | 0.18 PQOS / 0.22 wNEAR — about forty cents |
| Days at that depth | weeks |
| DexScreener index | **not indexed** |
| GeckoTerminal | indexed, but with **stale supply** (shows 0.4) |

Two days ago we fixed the depth by hand: 10.42 PQOS + 12.61 wNEAR, 57× growth,
price unchanged, and we now hold 100% of the LP.

**The lesson: a token without a launch venue is a token nobody can buy.** Our
technical work was complete for weeks while the market was forty cents deep.

## Why we are a useful case study for you

- **A live example of the failure you prevent.** Not hypothetical — 15 NEAR
  Builders posts, 12 deployed contracts, and no market.
- **An unusual token.** Collateral-backed issuance means supply is genuinely
  scarce; that is a launch story your platform could tell.
- **We did the math publicly.** The exact ratio needed to add liquidity without
  moving price is documented in our repository.
- **We will write it up.** A case study with real numbers is better marketing
  than a feature list.

## How it could fit

**Option A — list PQOS as an existing token.** We are live on Ref 8992 with real
depth now.

**Option B — use us as a documented case study.** "This token launched without a
venue and here is what it cost them" is a stronger pitch than a feature list.

**Option C — advise on a Rhea pool.** Our liquidity is on Ref; a concentrated
position on Rhea might serve better.

## Why this is worth your time

- **A concrete before/after.** Forty cents of depth versus 12.6 wNEAR — same
  token, one decision apart.
- **A token with an honest story.** No premine is rare and sellable.
- **A willing subject.** We will publish whatever you write.

## What we are asking

Consider listing PQOS, or using our launch as the cautionary case study your
product needs. Either is useful to us and both are free to you.

## Proof

```
https://app.ref.finance/#/pools/8992
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/WHITEPAPER_PQOS.md
https://nearblocks.io/token/unog.near
```

---

## Ready-to-send message

```
Hi — nearly.trade exists because deploying a token and having no market is a real failure. I lived it.

PQOS launched with collateral-backed issuance (no premine, no ICO — every token bought with NEAR). Supply 61.47, 93.6% in one wallet, first pool depth about forty cents. DexScreener wouldn't index it. GeckoTerminal indexed it with stale supply.

Two days ago I fixed the depth by hand: 10.42 PQOS + 12.61 wNEAR, 57x growth, price unchanged. I now hold 100% of the LP.

That's a concrete before/after for your pitch — same token, one decision apart. Happy to be the case study, or to list PQOS if that's useful.

Detail: https://github.com/sykomiked/zedec-zxv-deployment
```
