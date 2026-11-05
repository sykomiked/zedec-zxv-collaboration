# Four-valued logic

This is the idea that appears in eleven of the nineteen proposals. It is here
in full because it is the reason the rest of the architecture is shaped the way
it is.

## The problem with two values

A conventional system asks "did this happen?" and answers yes or no. When two
valid, conflicting claims arrive — two attestations, both correctly signed,
that cannot both be true — it resolves by rule:

- last writer wins
- majority wins
- timelock then default

All three **destroy information**. After resolution, nobody can tell the system
was ever uncertain. The conflict is gone, and with it the evidence.

## The four values

| Verdict | Meaning | Settles value |
|---|---|---|
| `TRUE` | verified, consistent | **yes** |
| `FALSE` | refuted | no |
| `BOTH` | two valid claims that conflict | **no — held** |
| `NEITHER` | nothing verifiable | no |

**Only `TRUE` releases value.** `BOTH` is a first-class outcome, not an error
path: the system records that it cannot decide, and stops.

```
        ┌──────────┐
        │ PENDING  │
        └────┬─────┘
     ┌───────┼────────┬──────────┐
     v       v        v          v
  ┌──────┐┌──────┐┌───────┐┌─────────┐
  │ TRUE ││FALSE ││ BOTH  ││ NEITHER │
  └──┬───┘└──┬───┘└───┬───┘└────┬────┘
     v       v        v         v
  SETTLED REJECTED  HELD      HELD
```

## Why "held" is the right answer

If two attestors disagree and both are cryptographically valid, one is lying or
one is wrong. Settling on either releases value on a claim the system cannot
verify. Holding costs time; settling wrongly costs money.

For a system that moves value, refusing to decide is the safe failure.

## Where it is implemented

- in the core `unog.near`, as the verdict evaluator behind every settlement
- in `scp144.near`, as a **145-state** logic core (144 lanes plus the whole)
- in every outpost, which applies the same tables before minting

The same four values appear at every layer, so a contradiction at the edge is
representable at the centre. That consistency is the design.

## The eight problems it answers

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

## What this is not

- Not a formal verification of the protocol
- Not a proof that these tables are the only correct ones
- Not Belnap's lattice — the kernel uses its own conjoin/disjoin ordering

It is an engineering choice: represent uncertainty explicitly rather than
collapse it, and fail closed when uncertain. Anyone implementing against this
must use the kernel's tables, not re-derive them.
