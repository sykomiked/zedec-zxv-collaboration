# White paper — Deal Settler — P2P escrow for real-world agreements

**Recipient:** `i5022803831.tg`
**Contact:** https://nearbuilders.org/builders/i5022803831.tg
**Their project:** Deal Settler — P2P escrow for real-world agreements (`deal-settler-cex-style-p2p-escrow-for-real-world-agreements-nlmkfj`)
**Tier:** 2
**From:** `jollydragonroger.near` — ZEDEC/ZXV

---

## What you are building

Funds lock between two known parties, release when both confirm, and a
mutually-agreed admin steps in only on dispute.

That last clause is the whole product, and it is also the whole problem.

## The dispute case is a logic problem, not a UI problem

"Both confirm" is easy. "Neither confirms" is easy. **"Both claim they
confirmed and the other did not"** is the case that decides whether your escrow
is trusted.

A boolean escrow must resolve it: admin decides, or a timeout decides. Either
way the losing party believes the contract is unfair, and that belief is
correct — the contract genuinely could not tell the difference between a liar
and an honest party.

## What we have

A settlement core where that case has a name:

| Verdict | Meaning | Escrow action |
|---|---|---|
| `TRUE` | both confirmations verified | release |
| `FALSE` | refuted | refund |
| `BOTH` | two valid, conflicting claims | **hold, escalate to admin** |
| `NEITHER` | nothing verifiable | hold, escalate |

`BOTH` is exactly your dispute case, formalised. The contract does not have to
pretend it knows; it records that it cannot, and hands the decision to the
admin **with the evidence intact**.

## How it integrates

**Step 1 — two confirmations, four outcomes.** Each party's confirmation is a
claim. Evaluate them together: both true → `TRUE`; both false → `FALSE`; one
each → `BOTH`; neither → `NEITHER`.

**Step 2 — only `TRUE` auto-releases.** `BOTH` and `NEITHER` escalate. The
admin sees why, not just that.

**Step 3 — record the verdict.** Our `chancery.unog.near` is a sealed
attestation registry — an escrow dispute record that cannot be edited later is
worth more than one that can.

**Step 4 — optionally settle inside `unog.near`.** Sealed execution means the
admin cannot unilaterally move funds outside the policy.

## Why this is worth your time

- **It makes the admin honest.** With `BOTH` recorded, the admin decides a
  documented conflict rather than an undocumented one.
- **It removes the timeout default.** Most escrows resolve by timeout, which
  punishes whichever party was slower. `BOTH` gives a real decision instead.
- **It is a trust argument you can sell.** "Our escrow can prove it was
  uncertain" beats "our escrow has an admin".
- **The primitive is implemented.** Not a spec.

## What we are asking

Consider a four-valued settlement result rather than a boolean. If it fits, we
will write the integration notes.

## Proof

```
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/ARCHITECTURE.md#4-the-four-valued-state-machine
```

---

## Ready-to-send message

```
Hi — Deal Settler's whole product is the dispute clause: both confirm, release; otherwise an admin steps in.

That dispute case is a logic problem. "Both claim they confirmed and the other didn't" is what decides whether your escrow is trusted — and a boolean contract genuinely can't tell a liar from an honest party.

I built a settlement core where that case has a name. Four verdicts: TRUE, FALSE, BOTH, NEITHER. BOTH means two valid conflicting claims — held and escalated to the admin with the evidence intact, instead of resolved by timeout.

It removes the timeout default, which is the thing that punishes whoever was slower.

Detail: https://github.com/sykomiked/zedec-zxv-deployment
```
