# White paper — Datagent — private data, paid per access

**Recipient:** `harrydhillon.near`
**Contact:** https://nearbuilders.org/builders/harrydhillon.near
**Their project:** Datagent — private data, paid per access (`datagent-private-data-paid-per-access-onmuqk`)
**Tier:** 2
**From:** `jollydragonroger.near` — ZEDEC/ZXV

---

## What you are building

A market for private data records: a buyer's agent pays inside an owner-signed
NEAR Intents wallet policy, and only a settled payment adds the buyer to a NOVA
data group for a 60-minute decryption window. Membership and the capsule's data
hash are recorded on-chain.

You already solved the hard part — **pay-then-decrypt with a hash commitment**.
Two things could make it stronger.

## Where we overlap

You record a capsule's data hash on-chain. **We run a content-addressed store
inside `unog.near`** — the same primitive, already sealed and verifiable. A
reader can retrieve by hash and prove what they got without trusting the
server.

You evaluate whether a payment settled. **We evaluate claims to four values**,
where "payment settled" and "payment disputed" are distinguishable states
rather than a boolean and a retry.

## How it integrates

**Step 1 — store capsules in our content-addressed store.** Retrieval by hash;
verification is the hash, not the server's word.

**Step 2 — evaluate access grants four-valued.**

```
TRUE     → grant the 60-minute window
FALSE    → deny
BOTH     → payment and dispute both valid → hold, do not decrypt
NEITHER  → cannot verify → hold
```

The critical one is `BOTH`: a payment that settles while a dispute is open
should not open a decryption window. A boolean system grants access and hopes.

**Step 3 — record membership in `chancery.unog.near`.** Sealed registry, zero
access keys, immutable membership history.

**Step 4 — keep your Intents policy.** Our layer is complementary, not a
replacement — it hardens the access decision.

## Why this is worth your time

- **A disputed payment currently opens a window.** Four-valued evaluation closes
  that hole without adding an oracle.
- **Content-addressed storage removes a trust assumption.** Right now a buyer
  trusts your server to serve the right capsule.
- **The registry is sealed.** Membership history nobody can edit is a selling
  point to data owners.
- **Minimal change.** You keep NOVA, keep Intents, add a verdict and a hash
  store.

## What we are asking

Look at the `BOTH` case for access grants. If it matters, we will document the
calls.

## Proof

```
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/ARCHITECTURE.md#3-the-sealed-core
```

---

## Ready-to-send message

```
Hi — Datagent already solved the hard part: pay, then decrypt, with a hash commitment. Two things could make it tighter.

First: you record the capsule hash on-chain, but retrieval still trusts a server. I run a content-addressed store inside unog.near where the hash *is* the verification.

Second, and more important: what happens when a payment settles while a dispute is open? A boolean grants access and hopes. I evaluate to four values — TRUE, FALSE, BOTH, NEITHER — and BOTH means both claims are valid, so hold and don't open the decryption window.

You'd keep NOVA and Intents; this just hardens the access decision.

Detail: https://github.com/sykomiked/zedec-zxv-deployment
```
