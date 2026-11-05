# White paper — NEAR Ecosystem Compatibility Badge

**Recipient:** `sarusensei.tg`
**Contact:** https://nearbuilders.org/builders/sarusensei.tg
**Their project:** NEAR Ecosystem Compatibility Badge (`near-ecosystem-compatibility-badge-5e6ood`)
**Tier:** 3
**From:** `jollydragonroger.near` — ZEDEC/ZXV

---

## What you are building

A checklist that shows how NEAR-friendly a project really is: wallet
compatibility, correct standards, APIs, docs, security — with what is done, what
is missing, and what could be better.

## Why we are a useful case

We would score unusually well on some axes and badly on others, which makes us a
good calibration test for your checklist.

**Strong:**

| Check | Our answer |
|---|---|
| NEP-141 standard | `ft-1.0.0`, verified metadata |
| Token contract | `unog.near`, 24 decimals, no admin mint |
| Source of truth | code hash published and verified against chain |
| Security posture | 8 of 12 contracts sealed with zero access keys |
| Standards | FIPS 204/205 verification on-chain |
| Docs | 21 documents, including what is *not* proven |

**Weak — and we say so publicly:**

| Check | Our answer |
|---|---|
| Front-end | **does not exist** |
| Liquidity | thin; Ref pool was 40 cents until two days ago |
| Third-party audit | **none** |
| Wallet support | no wallet integration |
| Distribution | 93.6% of supply in one wallet |

## Why that makes us a good test case

A checklist that scores us 100% is not measuring anything. A checklist that
correctly separates "sealed and verifiable" from "no interface and unaudited" is
measuring something real.

## How it could fit

**Option A — score us and publish the result.** We will not dispute it; we will
link it.

**Option B — use our answers to calibrate the checklist.** If a criterion cannot
distinguish us from a project with an admin key and no published binary, the
criterion is not working.

**Option C — we help define the security axis.** "Sealed" (zero access keys) is
a stronger and more checkable claim than "audited", and most checklists do not
ask about it.

## Why this is worth your time

- **A case that spans the range.** Strong on verifiability, weak on
  distribution.
- **A checkable security criterion.** `view_access_keys` returns a list; empty
  means sealed. That is a one-call test any reviewer can run.
- **We will publish the result.**

## What we are asking

Score us, and tell us what we failed. We will publish it either way.

## Proof

```
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/REPRODUCIBILITY.md
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/JUDGES_START_HERE.md
```

---

## Ready-to-send message

```
Hi — your compatibility badge needs test cases that span the range, otherwise it's measuring nothing.

We'd score unusually well on some axes and badly on others. Strong: NEP-141 verified, code hash published and matched to chain, 8 of 12 contracts sealed with zero access keys, FIPS 204/205 on-chain. Weak: no front-end, no audit, thin liquidity, 93.6% of supply in one wallet — all of which we say publicly.

A checklist that scores us 100% isn't measuring anything. One that separates "sealed and verifiable" from "no interface and unaudited" is.

One suggestion for your security axis: `view_access_keys` returning empty is a one-call, checkable definition of "sealed". Most checklists don't ask.

Score us and tell us what we failed. We'll publish it either way.

Detail: https://github.com/sykomiked/zedec-zxv-deployment
```
