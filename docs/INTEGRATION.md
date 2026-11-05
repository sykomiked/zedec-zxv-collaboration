# Integration guide

Call shapes for the integrations proposed in each white paper.

## Mint — NEAR collateral → TIAMAT

```
contract : unog.near
method   : deposit
attach   : the NEAR you are depositing
returns  : { ok: true, minted_to: <32-byte hex> }
```

Credits an **internal GRIDCHAIN account**, not a wallet. Derive it as
`sha256("near-account:" + accountId)` for a stable per-user account.

## Export — internal balance → NEP-141 wallet

```
contract : unog.near
method   : execute  (op = OP_FT_EXPORT)
args     : { op, payload: asset32 ‖ amount ‖ recipient }
```

Requires a small NEAR balance on the **internal** account to pay the op fee.
Without it the call fails with `funds`.

## Redeem — TIAMAT → NEAR

```
contract : unog.near
method   : ft_transfer_call
args     : { receiver_id: "post.jollydragonroger.near", amount, msg }
```

Settlement is two steps. Show the request state, not just the tx hash.

## Bridge — lock for another chain

```
contract : unog.near
method   : ft_transfer_call
args     : { receiver_id: "chiglet.unog.near", amount,
             msg: "<chain>|<recipient>" }
```

`msg` is **pipe-separated, not JSON**. `ethereum|0xcB5AA2F2…`. Chains:
`ethereum`, `sui`, `ton`, `tron`, `aptos`.

## Read state

| What | Call |
|---|---|
| total supply | `unog.near.ft_total_supply` |
| metadata | `unog.near.ft_metadata` → decimals **24** |
| balance | `unog.near.ft_balance_of({account_id})` |
| next mint price | `unog.near.tiamat_quote` |
| pool state | `unog.near.pool` |
| LP position | `unog.near.position` |
| bridge fee | `chiglet.unog.near.fee_ppm` → `889` |

## Integration patterns by use case

### If you need an interface registry
Emit our 214 descriptors in your schema. Key by code hash, not account name.
The hashes are sealed, so an entry keyed to one cannot go stale.

### If you need a resolution primitive
Use the four verdicts. Map `TRUE` → release, `FALSE` → reject, `BOTH` and
`NEITHER` → hold and escalate. Do not collapse `BOTH` into either outcome.

### If you need an attestation store
`chancery.unog.near` — sealed, zero access keys. Records cannot be edited after
the fact, by anyone.

### If you need content-addressed storage
Store against the hash; verify by re-hashing. The hash *is* the proof.

### If you need settlement with bounded loss
`chiglet.unog.near` — 3-of-5 attested, immutable per-chain caps. Worst-case
exposure is computable before you write a policy.

## Failure catalogue

Every one of these was hit for real.

| Symptom | Cause | Fix |
|---|---|---|
| `range` on pool op | assets not in bytewise order | NEAR (zeros) first |
| `exists` on pool create | pool already created | use add |
| `funds` on export | internal account has no NEAR for fee | deposit NEAR to it |
| `range` on export | amount > actual internal balance | read the balance record |
| silent refund on `ft_on_transfer` | camelCase args vs snake_case caller | `#[near_bindgen]` |
| `E28: Illegal msg` on Ref | bare pool id is not a valid msg | `msg: ""` then `add_liquidity` |
| `E35` on Ref add_liquidity | missing 1-yoctoNEAR guard | `--depositYocto 1` |
| `Replay(0,0)` on outpost mint | nonce already used | bump; first ticket is 1 |
| export never lands | nonce advanced by failed attempts | read nonce from account record |
| `unknown letter I` on NEP-413 | service cannot parse `ml-dsa-65:` | use the ed25519 key |
| balance reads 0 | RPC rate limit | re-query a different RPC |
