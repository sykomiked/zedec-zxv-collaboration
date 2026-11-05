# White paper — NEAR Quantum Shield

**Recipient:** `bhft11.tg`
**Contact:** https://nearbuilders.org/builders/bhft11.tg
**Their project:** NEAR Quantum Shield (`near-quantum-shield-vd8kbe`)
**Tier:** 1
**From:** `jollydragonroger.near` — ZEDEC/ZXV

---

## What you are building

A post-quantum readiness tool: scan an account's active signing keys, show its
ML-DSA-65 status, and let a user safely add a post-quantum key without touching
the CLI.

The scan is the easy half. **The hard half is what happens after the key is
added** — every service that parses a public key has to understand
`ml-dsa-65:` or it breaks. We have already been through that wall.

## What we have

`scp144.near` — a 77,823-byte contract that verifies post-quantum signatures
**on-chain, inside a NEAR transaction**:

| | |
|---|---|
| FIPS 204 | ML-DSA (Dilithium) verifier |
| FIPS 205 | SLH-DSA (SPHINCS+) verifier |
| Logic core | 145-state paraconsistent evaluator |
| Matrix | 144-lane (12 × 12, matching the core's 12 layers) |
| Boot self-test | 10/10, refuses to start otherwise |
| Access keys | **0** — sealed |
| Code hash | `DDQ4uJXM26WhRoYfRPgQcUKPpybzhGrBXmCbK7e85dmN9` |

We also run a live account with **both** an ed25519 and an ML-DSA-65 key, and we
have the failure log from doing it.

## The failure you are about to hit

We added an ML-DSA-65 key to a mainnet account, then tried to sign in to a
third-party service with `near message sign-nep413`. The site returned:

```
could not parse output, unknown letter I
```

The parser read the public key string, hit `ml-dsa-65:`, and choked on a
character inside the base58 payload. **The signature was valid. The service
simply predates the algorithm.**

Our fix: add a conventional `ed25519` key alongside the post-quantum one, and
sign with that where the service cannot handle ML-DSA. Both keys are full-access
on the same account. The PQ key is never removed.

This is the single most useful thing we can hand you: **the compatibility
catalogue**, so your tool warns users before they hit it.

## How it integrates

**Step 1 — use our verifier as the on-chain check.** Your tool can call
`scp144.near` to confirm a signature is valid before telling a user their key
works, rather than trusting an off-chain library:

```
contract : scp144.near
method   : mldsa87_verify / slhdsa256s_verify / kem_publish
returns  : TRUE / FALSE / BOTH / NEITHER
```

**Step 2 — add the compatibility warning.** Before a user adds an ML-DSA key,
show them: services that cannot parse `ml-dsa-65:` will reject sign-in; keep an
ed25519 key on the account for those; the PQ key is additive, never a
replacement.

**Step 3 — link the reference implementation.** Our repository documents the
whole flow, including the exact error text and the fix.

**Step 4 — optionally, use our account as a live test case.** We have a mainnet
account with both key types. Your tool can be validated against a real account
that has already been through the process.

## Why this is worth your time

- **You skip the discovery phase.** We already paid for the compatibility
  failures in real transactions.
- **You get an on-chain verifier.** Most PQ tooling is off-chain JavaScript.
  `scp144.near` proves a signature inside a NEAR transaction, which is a much
  stronger claim.
- **You get a live dual-key account** as a test fixture.
- **The warning is the product.** A readiness tool that does not warn about
  parser incompatibility sends users into a wall.

## What we are asking

Read our failure catalogue, and if it is useful, link it. If you want an
on-chain verifier behind your check, we will write the call for you.

We are not asking for a partnership announcement. We are asking you not to
repeat our mistake, and to point at the evidence when you warn people.

## Proof

```
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/CONTRACT_ADDRESSES.md
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/ARCHITECTURE.md
https://nearblocks.io/address/scp144.near
```

---

## Ready-to-send message

```
Hi — I built the post-quantum layer you're writing tooling for, and I have the failure log you're about to need.

I added an ML-DSA-65 key to a mainnet account and then tried to sign in somewhere with near-cli. The service returned "could not parse output, unknown letter I" — it choked on the `ml-dsa-65:` prefix. Signature was valid; the parser predates the algorithm. Fix was to keep a conventional ed25519 key alongside it.

I also run scp144.near: FIPS 204 and FIPS 205 verifiers on-chain, sealed, 77KB, boot self-test 10/10. Your tool could call it instead of trusting an off-chain library.

The compatibility warning is the most valuable part of your product. Happy to hand over the catalogue.

Detail: https://github.com/sykomiked/zedec-zxv-deployment
```
