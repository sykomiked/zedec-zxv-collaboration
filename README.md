# ZEDEC/ZXV — collaboration proposals

**19 custom proposals, one per NEAR Builders project.** Each is written for
that project specifically: what you are building, the failure mode your design
will hit, what we have that addresses it, and how it would integrate.

If you received an invite to this repository, your proposal is in
[`proposals/`](proposals/) and is named after your project.

---

## What this is

ZEDEC/ZXV is a settlement stack deployed on NEAR mainnet. Not a proposal —
a running system:

| | |
|---|---|
| Contracts | **12** on NEAR mainnet |
| Sealed (zero access keys) | **8** |
| Core | `unog.near` — 1,156,670 bytes, 151 operations, 214 ABI descriptors, 46 governance kinds, 12 layers |
| Token | TIAMAT (PQOS), 24 decimals, NEP-141, **no admin mint** |
| Bridge | `chiglet.unog.near`, 3-of-5 attested, 889 ppm, immutable per-chain caps |
| Outposts | 5 live — Ethereum, Sui, TON, Tron, Aptos |
| QA | 1,858,226 assertions, 0 failed; 26 VM scenarios inside NEAR's own runtime |
| Bytecode | all 12 published and hash-verified against chain |

The full record: https://github.com/sykomiked/zedec-zxv-deployment

---

## The one idea that repeats

Eleven of the nineteen proposals land on the same primitive. It is here
because it is genuinely the answer to eight different problems:

**Every claim evaluates to one of four values, and only `TRUE` settles.**

| Verdict | Meaning |
|---|---|
| `TRUE` | verified, consistent — settles |
| `FALSE` | refuted — rejected |
| `BOTH` | two valid claims that conflict — **held** |
| `NEITHER` | nothing verifiable — held |

A conventional system resolves `BOTH` by rule — last writer wins, majority
wins, or timeout — and **destroys the evidence that it was ever uncertain**.
For anything that moves value, that is the difference between paying a valid
claim and denying one.

| Their problem | The case a boolean cannot represent |
|---|---|
| disputed escrow | both parties claim success |
| coverage | half-settled transfer |
| solver reputation | two credible attestations disagree |
| futarchy | market cannot resolve cleanly |
| agent spending limits | policy rules conflict |
| activity feed | relays disagree about an event |
| double-booking | two valid reservations |
| disputed data payment | settled payment, open dispute |

---

## The proposals

| # | Project | Owner | Tier |
|---|---|---|---|
| 01 | NEAR Interface Commons | `bassoman.tg` | 1 |
| 02 | NEAR Quantum Shield | `bhft11.tg` | 1 |
| 03 | Backstop — Intents Coverage | `bhft11.tg` | 1 |
| 04 | Solver Reputation & Risk Network | `ftxnear.near` | 1 |
| 05 | KINU — Liquidity Terminal | `kinuonnear.near` | 1 |
| 06 | leash — agent spending limits | `musa_ais.tg` | 2 |
| 07 | Clearance — crash test | `selliks.near` | 2 |
| 08 | Deal Settler — P2P escrow | `i5022803831.tg` | 2 |
| 09 | VRX — reservation primitive | `vetted.near` | 2 |
| 10 | Datagent — private data | `harrydhillon.near` | 2 |
| 11 | Gas relay | `marsbark.tg` | 2 |
| 12 | Nostr ↔ NEAR | `efiz.near` | 2 |
| 13 | nearly.trade | `nearlytrade.near` | 2 |
| 14 | Verdikt — futarchy | `nexchangenear.near` | 2 |
| 15 | Open Crosspost | `crosspost.near` | 3 |
| 16 | NEAR Trust | `imrohitoma.near` | 3 |
| 17 | Ecosystem Compatibility Badge | `sarusensei.tg` | 3 |
| 18 | Ajo Agent | `xerofom.tg` | 3 |
| 19 | Portfolio risk intelligence | `dulfariz.near` | 3 |

---

## What we are offering

Nothing commercial. No token allocation, no investment ask, no exclusivity.

**We are offering work we have already done**, and asking whether it saves you
time:

- **214 ABI descriptors** across 12 contracts, keyed by code hash
- **FIPS 204 / 205 verifiers** running on-chain
- **A sealed attestation registry** — records nobody can edit, including us
- **A four-valued settlement evaluator** — implemented, live, sealed
- **A content-addressed store** — hash-verified retrieval
- **An attested bridge with immutable caps** — 5 chains, proven round trip
- **A provenance chain** — QC log hash = published binary = on-chain code hash

Take what is useful. Ignore the rest.

---

## How to respond

Open an issue on this repository, or comment on the proposal file. If you want
your proposal changed, say so and it will be changed.

**What we will not do:** ask you for money, ask for exclusivity, or claim a
partnership you have not agreed to.

---

## The honest part

This is a system that launched recently and has been operated by one person on
a small budget. That shapes what it looks like:

- **Supply is 61.47 PQOS** — small, because every token required collateral
- **Liquidity is thin** — Ref pool 8992 holds 12.6 wNEAR
- **Distribution is concentrated** — 93.6% in the operator's wallet
- **The bridge is attested, not trustless** — a 3-of-5 quorum, cap-bounded
- **It is unaudited** by any third party
- **There is no front-end** — the protocol works, the interface does not exist

All of that is in the public documentation, on the first page, not in a
footnote. A proposal that overstated the maturity of this system would not be
worth reading, and you would find out anyway.

---

## Licence

Apache-2.0. These proposals are free to use, quote, or ignore.
