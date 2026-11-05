# White paper — Nostr <> NEAR Integration

**Recipient:** `efiz.near`
**Contact:** https://nearbuilders.org/builders/efiz.near
**Their project:** Nostr <> NEAR Integration (`nostr-near-integration-w4u9yb`)
**Tier:** 2
**From:** `jollydragonroger.near` — ZEDEC/ZXV

---

## What you are building

An activity layer: reputations, points, personalities and footprints all need
the same plumbing, delivered as a standalone aggregation service.

You are right that they need the same plumbing. **They also need the same trust
model**, and that is where most activity layers quietly fail — an aggregation
service that says "this happened" is only as credible as its database.

## What we have

**A sealed attestation registry.** `chancery.unog.near` — 44,496 bytes, **zero
access keys**. Records cannot be edited after the fact by anyone, including us.

**A four-valued evaluator.** Activity claims conflict: two clients report
different events for the same key, or one reports an event the relay never saw.
That is `BOTH` or `NEITHER`, and both should be visible rather than resolved.

**A content-addressed store** inside `unog.near` — publish the hash of an
activity record, prove it later without republishing.

**An existing `social.near` presence** — we already publish there, so we have
hands-on knowledge of what a NEAR social activity feed actually looks like.

## How it integrates

**Step 1 — attest, do not assert.** Your aggregation service writes claims to a
registry rather than a database. The claim carries who said it and what verdict
it received.

**Step 2 — four-valued activity.**

```
TRUE     → the event happened, confirmed by the source
FALSE    → contradicted
BOTH     → two sources disagree, both credible → show both
NEITHER  → cannot verify → show as unverified
```

An activity feed that can say "unverified" is more useful than one that shows
everything at equal weight.

**Step 3 — hash the payload.** Store the activity record against its hash; the
feed shows the hash, and anyone can verify later.

**Step 4 — Nostr side stays yours.** We are not proposing to touch your relay
integration; we are proposing the NEAR-side record be attestable.

## Why this is worth your time

- **"Verified" becomes a real claim.** Right now an activity feed says what its
  database says. With a sealed registry, it says what cannot be edited.
- **Conflicting sources become representable.** Nostr has multiple relays; they
  will disagree. `BOTH` is the honest answer.
- **You get a reference implementation** — we already publish to `social.near`
  and can share the shapes.
- **No dependency on our operator.** There is no operator.

## What we are asking

Consider an attestation registry rather than a plain database for the NEAR-side
record. If it fits, we will document the calls.

## Proof

```
https://nearblocks.io/address/chancery.unog.near
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/ARCHITECTURE.md#4-the-four-valued-state-machine
```

---

## Ready-to-send message

```
Hi — your Nostr↔NEAR activity layer is right that reputations, points and footprints all need the same plumbing. They also need the same trust model, which is where activity layers usually fail: an aggregator that says "this happened" is only as credible as its database.

I run chancery.unog.near — a sealed attestation registry, zero access keys, so records can't be edited after the fact by anyone including me.

And multiple Nostr relays will disagree about events. That's a four-valued case for us: BOTH means two credible sources conflict, show both, don't pick one.

We also publish to social.near already, so I can share the shapes.

Detail: https://github.com/sykomiked/zedec-zxv-deployment
```
