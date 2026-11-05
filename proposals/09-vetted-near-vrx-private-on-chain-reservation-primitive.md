# White paper — VRX — private on-chain reservation primitive

**Recipient:** `vetted.near`
**Contact:** https://nearbuilders.org/builders/vetted.near
**Their project:** VRX — private on-chain reservation primitive (`vrx-a-private-on-chain-reservation-primitive-one-source-of-truth-for-who-reserved-what-1huh9g`)
**Tier:** 2
**From:** `jollydragonroger.near` — ZEDEC/ZXV

---

## What you are building

An on-chain reservation primitive: one source of truth for who reserved what,
across multiple sales channels, with prices and terms confidential and customer
privacy protected. Land, luxury cars, fine art.

Your two hard requirements — **confidentiality** and **provable uniqueness** —
are usually in tension. Hiding the terms means hiding the record, and a hidden
record is hard to prove unique.

## What we have

**A content-addressed store** inside `unog.near`. Data is stored against its
hash, so a reader can verify what they received without trusting the writer, and
the record can be proven without being published.

**A sealed attestation registry** — `chancery.unog.near`, 44,496 bytes, **zero
access keys**. Reservations recorded there cannot be edited after the fact by
anyone, including us.

**A four-valued evaluator.** Two channels can both believe they sold the same
asset. That is `BOTH` — a state, not an error. The primitive records the
conflict rather than silently honouring whichever transaction landed second.

## How it integrates

**Step 1 — store the reservation hash, not the terms.** The asset, buyer and
price stay private; the hash of the reservation goes on-chain. Uniqueness is
proven by the hash; confidentiality is preserved because the preimage is never
published.

**Step 2 — record the reservation in `chancery.unog.near`.** Sealed, immutable,
auditable.

**Step 3 — evaluate double-booking as `BOTH`.** Two valid reservations for the
same asset hash produce `BOTH` and hold, rather than one silently winning. That
is the double-booking problem solved at the logic layer, not the UI layer.

**Step 4 — optional: settle deposits through `unog.near`.** Sealed execution,
no admin override.

## Why this is worth your time

- **Double-booking becomes a represented state.** Your core value proposition is
  "eliminates double-bookings". `BOTH` is how you prove you did.
- **Confidentiality and uniqueness stop fighting.** Hash the record; publish the
  hash.
- **The registry is sealed.** An audit trail nobody can edit is the only kind
  worth citing to an enterprise buyer.
- **No new trust assumptions.** You are not asked to trust our operator; there
  is no operator.

## What we are asking

A conversation about whether content-addressed reservation hashes fit your
model. If they do, we will document the store calls.

## Proof

```
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/ARCHITECTURE.md#3-the-sealed-core
https://nearblocks.io/address/chancery.unog.near
```

---

## Ready-to-send message

```
Hi — VRX needs confidentiality and provable uniqueness at the same time, which usually fight each other: hiding the terms means hiding the record, and a hidden record is hard to prove unique.

I built a content-addressed store inside unog.near. Data is stored against its hash, so you can prove a reservation is unique without publishing the terms — the preimage never leaves your side.

There's also chancery.unog.near, a sealed attestation registry with zero access keys, so a reservation record can't be edited after the fact.

And double-booking is a four-valued case for us: two valid reservations for the same asset produce BOTH and hold, rather than one silently winning.

Detail: https://github.com/sykomiked/zedec-zxv-deployment
```
