# White paper — KINU — Liquidity Terminal on NEAR

**Recipient:** `kinuonnear.near`
**Contact:** https://nearbuilders.org/builders/kinuonnear.near
**Their project:** KINU — Liquidity Terminal on NEAR (`kinu-liquidity-terminal-on-near-0vp9rs`)
**Tier:** 1
**From:** `jollydragonroger.near` — ZEDEC/ZXV

---

## What you are building

A concentrated-liquidity terminal on Rhea: range builder, per-position PnL
including fees, and an agent that reads pools. Non-custodial, user signs
everything.

You need one thing above all others: **users who actually have liquidity to
manage.** We are one, and we are unusual in a way that helps you.

## Our situation

We launched a token, PQOS, with collateral-backed issuance — no premine, no
ICO, no team allocation. That means supply is small (61.47) and the owner holds
most of it.

Two days ago we seeded Ref pool 8992:

| | Before | After |
|---|---|---|
| PQOS | 0.181868 | **10.423297** |
| wNEAR | 0.220000 | **12.608750** |
| Depth | — | **57×** |
| LP shares | — | 57.3140 of 57.3141 (**100%**) |

We are the entire LP. That is not a healthy pool; it is a pool waiting for a
tool.

## Why we are a good first user for you

- **We hold the whole LP position.** One decision-maker, no governance.
- **We have a real token with a real contract** — `unog.near`, 24 decimals,
  NEP-141, verifiable metadata.
- **We understand the mechanics.** We already computed the exact ratio needed to
  add liquidity without moving price: 10.2414 PQOS + 12.38875 wNEAR.
- **We are actively looking for range strategy.** A single full-range position
  is the least efficient possible deployment of 12.6 wNEAR.
- **We have no front-end.** We do everything by CLI, which is exactly the pain
  your product removes.

## How it integrates

**Step 1 — list PQOS/wNEAR.** Contract `unog.near`, quote `wrap.near`, 24
decimals both sides. Ref pool 8992.

**Step 2 — show us a range.** Our pool is 10.42 / 12.61 at 1.2097 wNEAR per
PQOS. A concentrated position around that price would use the same capital far
more efficiently than full-range.

**Step 3 — track PnL per position.** We need to know whether the fees are
out-earning impermanent loss. Right now we cannot tell.

**Step 4 — let your agent read our pool.** `get_pool(8992)` on
`v2.ref-finance.near` returns reserves and total shares; our LP share is
`get_pool_shares(8992, "jollydragonroger.near")`. Public, no key needed.

## Why this is worth your time

- **A real user with real capital, immediately.** Not a testnet account.
- **An unusual token that makes a good case study.** Collateral-backed issuance
  means supply is genuinely scarce — a story your content could use.
- **A gap you can demonstrate.** "This user is full-range with 12.6 wNEAR and
  cannot see their PnL" is a concrete before/after.
- **We will document it.** If you help us, we publish the result in a repository
  that already has 15 NEAR Builders entries pointing at it.

## What we are asking

List the pair, and show us what a sensible range looks like for a small pool
with one LP. If your terminal can beat full-range, we will say so publicly.

We are not asking for incentives. We are asking to be your first worked
example.

## Proof

```
https://app.ref.finance/#/pools/8992
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/WHITEPAPER_PQOS.md
https://nearblocks.io/token/unog.near
```

---

## Ready-to-send message

```
Hi — I run a token (PQOS, contract unog.near) and I'm the only LP in Ref pool 8992. I put 10.42 PQOS and 12.61 wNEAR in two days ago, 57x the previous depth, and now it's sitting full-range earning whatever it earns because I have no tooling to manage it.

That's your exact use case. One LP, real capital, no idea whether fees are out-earning IL.

I did the ratio math by hand to add without moving price (10.2414 PQOS + 12.38875 wNEAR), which is a good sign I need a terminal.

Would you list PQOS/wNEAR and show me what a sensible range looks like for a pool this small?

Pool: https://app.ref.finance/#/pools/8992
Repo: https://github.com/sykomiked/zedec-zxv-deployment
```
