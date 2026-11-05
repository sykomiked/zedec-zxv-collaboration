# White paper — Gas relay — NEAR Intents gas abstraction

**Recipient:** `marsbark.tg`
**Contact:** https://nearbuilders.org/builders/marsbark.tg
**Their project:** Gas relay — NEAR Intents gas abstraction (`gas-relay-6e3d3p`)
**Tier:** 2
**From:** `jollydragonroger.near` — ZEDEC/ZXV

---

## What you are building

A gas relay with NEAR Intents underneath: a user should not need the destination
chain's native token to move value there.

**So do we, and we built it into the fee.** Worth comparing notes before both
of us solve it twice.

## What we already run

`chiglet.unog.near` — the RouteLock bridge — charges **8.889 basis points (889
ppm)** on routed transfers. That fee exists specifically to fund
destination-chain gas, so a client never needs the other chain's token:

```
lock PQOS on NEAR  →  3-of-5 attestation  →  mint on destination
fee: 889 ppm, readable on-chain at chiglet.unog.near.fee_ppm()
```

Proven end to end: 0.5 PQOS locked, 0.5095555 wPQOS minted on Ethereum,
transaction `0xf091c443…`, receipt status 1. The 0.0004445 difference is the
fee, measured.

Five outposts live: Ethereum, Sui, TON, Tron, Aptos — each with an immutable
supply cap.

## Where we differ, and why it matters

| | Ours | Yours |
|---|---|---|
| Model | fee funds gas, charged on the value moved | relay abstraction |
| Trust | 3-of-5 attested, cap-bounded | depends on design |
| Scope | 5 chains, fixed set | Intents — broader reach |
| Verdicts | four-valued, only `TRUE` settles | — |

Yours reaches further because Intents reaches further. Ours has a settlement
model that can represent a failed route without defaulting.

## How it could fit together

**Option A — you use our outposts as a settlement leg.** For the five chains we
already cover, `chiglet.unog.near` is live with caps. You handle Intents routing;
we handle the final settlement on those chains.

**Option B — we adopt your relay for gas.** Our 889 ppm covers gas on our five
chains; Intents reaches chains we do not. A relay would extend our reach.

**Option C — share the fee model.** If a relay is funded by a bps fee on value
moved, our 889 ppm is a working reference for what that looks like and what it
pays for.

## Why this is worth your time

- **You avoid rebuilding five outposts.** They exist, with caps and attestation.
- **Our fee model is proven, not proposed.** 889 ppm measured on a real
  transaction.
- **The trust question gets answered once.** Attested and cap-bounded is a
  weaker claim than trustless, but it is a *stated* one — which is more than
  most relays offer.

## What we are asking

Twenty minutes to compare designs. Either we complement each other or we are
building the same thing twice, and both outcomes are worth knowing.

## Proof

```
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/outposts/FEE_AND_ARBITRAGE_ECONOMICS.md
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/TRANSACTION_FLOWS.md
```

---

## Ready-to-send message

```
Hi — you're building a gas relay with Intents underneath, so users don't need the destination chain's native token. I built that into a fee instead, and we should compare before both of us solve it twice.

chiglet.unog.near charges 889 ppm on routed transfers specifically to fund destination gas. Proven end to end: 0.5 PQOS locked on NEAR, 0.5095555 wPQOS minted on Ethereum, status 1, fee measured at 0.0004445. Five outposts live with immutable caps.

Yours reaches further — Intents goes where we don't. Ours has a settlement model that represents a failed route instead of defaulting.

Either we complement each other or we're duplicating work. Both worth knowing.

Detail: https://github.com/sykomiked/zedec-zxv-deployment
```
