# White paper — Portfolio risk intelligence for AI agents

**Recipient:** `dulfariz.near`
**Contact:** https://nearbuilders.org/builders/dulfariz.near
**Their project:** Portfolio risk intelligence for AI agents (`portfolio-risk-intelligence-for-ai-agents-rzcc5w`)
**Tier:** 3
**From:** `jollydragonroger.near` — ZEDEC/ZXV

---

## What you are building

A read-only wallet risk API for AI agents: a 0–100 score, A–F grade, plain-English
findings, paid per call in USDC over x402, with an MCP server and spend caps.

## What we can offer

**A token with unusual risk characteristics that your model should be able to
describe correctly.**

PQOS is not a typical NEAR token:

| Property | Value | Risk implication |
|---|---|---|
| Contract | `unog.near` | — |
| Admin mint | **none** — zero access keys | cannot be inflated |
| Supply | 61.47 | very small |
| Concentration | 93.6% one wallet | severe |
| Liquidity | Ref pool 8992, 12.6 wNEAR | thin |
| Decimals | 24 | unusual; many indexers get this wrong |
| GeckoTerminal supply | **stale — shows 0.4** | third-party data is wrong |
| Audit | none | unknown code risk |

## Why we are a good calibration case

A risk score that rates us the same as a memecoin with an admin mint is not
measuring risk. A score that captures:

- **no admin mint** (reduces one class of risk to zero)
- **extreme concentration** (increases another)
- **thin liquidity** (exit risk)
- **stale third-party data** (the agent may be reading a wrong number)

…is measuring something real.

The last one matters most for an agent product: **GeckoTerminal currently
reports our supply as 0.4 PQOS when it is 61.47.** An agent that trusts that
number will be wrong by a factor of 150. A risk API that detects
supply-figure disagreement between sources is genuinely valuable.

## How it could fit

**Option A — add PQOS to your NEAR coverage.** We will give you accurate
figures.

**Option B — add a "data disagreement" finding.** Compare supply from the
contract against supply from indexers. Disagreement is itself a risk signal, and
it is cheap to compute.

**Option C — use us as a test case for the concentration axis.** 93.6% in one
wallet should produce a strong finding.

## Why this is worth your time

- **A case with contradictory signals** — excellent risk posture on issuance,
  terrible on distribution.
- **A live example of indexer error** to calibrate against.
- **We will give you the correct figures and the commands to verify them.**

## What we are asking

Add PQOS to your NEAR coverage, or use the supply-disagreement idea. Both are
free to you.

## Proof

```
https://nearblocks.io/token/unog.near
https://pikespeak.ai/token/unog.near
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/COINGECKO_SUPPLY_AND_DISTRIBUTION.md
```

---

## Ready-to-send message

```
Hi — your risk API scores NEAR wallets. I have a token with contradictory risk signals that would make a good calibration case.

PQOS (contract unog.near): no admin mint at all — zero access keys, so it can't be inflated. But 93.6% of supply sits in one wallet, liquidity is 12.6 wNEAR, and there's no audit. A score that rates it the same as a memecoin with an admin mint isn't measuring risk.

One concrete idea for your product: GeckoTerminal currently reports our supply as 0.4 PQOS when it's 61.47. An agent trusting that number is wrong by 150x. Supply disagreement between the contract and indexers is itself a cheap, useful risk finding.

Happy to give you accurate figures and the commands to verify them.

Detail: https://github.com/sykomiked/zedec-zxv-deployment/blob/main/COINGECKO_SUPPLY_AND_DISTRIBUTION.md
```
