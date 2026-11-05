# White paper — leash — on-chain spending limits for AI agents

**Recipient:** `musa_ais.tg`
**Contact:** https://nearbuilders.org/builders/musa_ais.tg
**Their project:** leash — on-chain spending limits for AI agents (`leash-on-chain-spending-limits-for-ai-agents-9dlnpl`)
**Tier:** 2
**From:** `jollydragonroger.near` — ZEDEC/ZXV

---

## What you are building

Funds sit in a vault, not in the agent's account. The agent asks the vault to
pay; the contract enforces the owner's policy — per-payment cap, daily cap,
destination allowlist, per-agent pause, global kill switch. Every denied attempt
is recorded.

The design is right. One question decides whether it holds: **what does the
vault do when it cannot decide?**

## The gap

Your policy engine has two outcomes today: pay or deny. Real requests have a
third and fourth:

- the destination is on the allowlist, but the amount cannot be verified against
  the invoice
- two policy rules conflict — one permits, one blocks

A boolean policy engine must pick. If it picks "pay", the guardrail has a hole.
If it picks "deny", legitimate payments fail and the owner overrides the leash —
which is how every spending limit eventually dies.

## What we have

A four-valued evaluator where the ambiguous cases have their own states:

| Verdict | Meaning | Vault action |
|---|---|---|
| `TRUE` | policy satisfied, request verified | **pay** |
| `FALSE` | policy violated | deny |
| `BOTH` | two valid rules conflict | **hold, notify owner** |
| `NEITHER` | cannot verify | hold |

Only `TRUE` pays. `BOTH` and `NEITHER` are recorded and escalated rather than
silently resolved. That is what turns "spending limit" into "spending policy
with a dispute path".

## How it integrates

**Step 1 — replace the boolean with a verdict.** Your policy contract returns
`TRUE` / `FALSE` / `BOTH` / `NEITHER` instead of a bool.

**Step 2 — map actions.**

```
TRUE     → release payment
FALSE    → deny, log
BOTH     → hold, emit event, require owner co-signature
NEITHER  → hold, emit event, require owner co-signature
```

**Step 3 — record every verdict.** Denied and held attempts are the audit trail
that makes the leash credible. Our `chancery.unog.near` is a sealed attestation
registry if you want a ready-made store.

**Step 4 — optionally settle through `unog.near`.** The sealed core gives you an
execution environment with no admin key, so a compromised operator cannot
override a policy.

## Why this is worth your time

- **It closes the override hole.** The reason spending limits fail is that
  owners disable them when they block legitimate work. `BOTH` gives the owner a
  third option: approve this one case without disabling the leash.
- **It is a differentiator.** Every competitor in this space is building
  boolean policy. Four-valued policy is a real distinction, not marketing.
- **The implementation exists.** We can document the tables and the call shape;
  you are not starting from a spec.
- **It matches your audit story.** "Every denied attempt is recorded" becomes
  "every denied *and every ambiguous* attempt is recorded".

## What we are asking

Consider a four-valued policy result instead of a boolean. If it fits, we will
write the integration notes.

We are not asking you to depend on our contracts. The idea is portable — you can
implement the four states in your own vault.

## Proof

```
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/ARCHITECTURE.md#4-the-four-valued-state-machine
```

---

## Ready-to-send message

```
Hi — leash has the right architecture (vault holds funds, contract enforces policy). One question decides whether it survives contact with users: what does the vault do when it can't decide?

Your engine is boolean today. Real requests have two more outcomes: the destination is allowlisted but the amount can't be verified, or two rules conflict. Boolean has to pick, and either choice is wrong — pay and the guardrail has a hole, deny and the owner disables the leash.

I built a four-valued evaluator for exactly that: TRUE / FALSE / BOTH / NEITHER, only TRUE pays, BOTH and NEITHER hold and escalate. It gives the owner a third option — approve this case without switching the leash off.

The idea is portable; you could implement the four states in your own vault.

Detail: https://github.com/sykomiked/zedec-zxv-deployment
```
