# White paper — NEAR Trust — Project Verification & Reputation

**Recipient:** `imrohitoma.near`
**Contact:** https://nearbuilders.org/builders/imrohitoma.near
**Their project:** NEAR Trust — Project Verification & Reputation (`near-trust-project-verification-reputation-zhghbx`)
**Tier:** 3
**From:** `jollydragonroger.near` — ZEDEC/ZXV

---

## What you are building

A community-driven platform where projects submit themselves for review, prove
legitimacy, and build trust through transparent verification and on-chain
commitment.

Your hardest problem is **what "verified" means**. Most verification is a human
opinion recorded somewhere. We can offer something rarer: a project whose claims
resolve to hashes.

## What we can contribute as a case study

Our entire record is machine-checkable:

| Claim | How it resolves |
|---|---|
| 12 contracts deployed | code hash read from chain, per account |
| Published binary is the running binary | SHA-256 of published file == base58 code hash on chain |
| 8 contracts are sealed | `view_access_keys` returns empty |
| Token has no admin mint | the contract has zero access keys |
| Build passed QA | QC log hash == deployed hash |

One command proves all of it:

```bash
git clone https://github.com/sykomiked/zedec-zxv-deployment
cd zedec-zxv-deployment && ./tools/verify.sh
```

## The distinction worth building your product around

There are two kinds of verification:

1. **Attested** — a human or committee says the project is legitimate
2. **Provable** — the project's claims resolve to on-chain facts

Most platforms do only the first, because the second requires the project to
have published something verifiable. We do the second.

**A useful field for your platform: "can this project's claims be
independently checked, and how?"** — with a link and a command. That is more
valuable to a user than a badge.

## How it could fit

**Option A — we are your reference case.** A project whose legitimacy is
demonstrable, not asserted.

**Option B — add a "verifiable" tier.** Projects that publish a verification
path get a distinct mark from projects that only have attestations.

**Option C — we help define the check.** We have already built the tooling; we
can tell you what is cheap to verify and what is not.

## Why this is worth your time

- **A real example of the strongest category.** Almost nothing on the platform
  can prove its own claims.
- **It differentiates you from a badge mill.** "Provable" versus "attested" is a
  real distinction.
- **We will be honest about our gaps too** — we are unaudited, illiquid, and
  concentrated. A verification platform that can display weaknesses credibly is
  worth more than one that only displays strengths.

## What we are asking

Consider us as the worked example, and consider a "verifiable" tier separate
from attestation.

## Proof

```
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/REPRODUCIBILITY.md
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/CONTRACT_ADDRESSES.md
```

---

## Ready-to-send message

```
Hi — NEAR Trust's hardest question is what "verified" actually means. Most verification is a human opinion recorded somewhere.

I can offer a rarer case: a project whose claims resolve to hashes. Twelve contracts, code hash read from chain per account; published binary SHA-256 equals the base58 code hash on chain; eight contracts sealed with zero access keys; a QC log written before deployment carrying the same digest as the running contract.

One command proves all of it.

The distinction worth building around: attested vs provable. Most platforms do only the first because the second requires the project to have published something checkable.

Happy to be the reference case, and honest about our gaps — we're unaudited, illiquid and concentrated. A verification platform that can display weaknesses credibly is worth more than one that only shows strengths.

Detail: https://github.com/sykomiked/zedec-zxv-deployment/blob/main/REPRODUCIBILITY.md
```
