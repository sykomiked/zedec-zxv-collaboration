# Architecture

The system is one vertical stack: a chain running inside a NEAR contract,
wrapped in satellites, bridged to five external chains.

## The stack

```
APPLICATION      front-ends · bots · routers          (does not exist yet)
     |
SETTLEMENT       unog.near — sealed, zero access keys
                 151 ops · 214 ABI descriptors · 46 governance kinds
                 12 booted layers · internal AMM · content store
     |
SATELLITES       chiglet.unog.near      bridge, 3-of-5 attested, 889 ppm
                 post.jollydragonroger  mint desk / redemption kiosk
                 mission.unog.near      ENVOY — jobs, bounties
                 chancery.unog.near     REGISTRAR — attestations
                 consulate.unog.near    TRANSIT — routes
                 protocol.unog.near     PROTOCOL — governance seat
     |
PLATFORM         zedec.near   kernel, boots the core
                 scp144.near   post-quantum engine (FIPS 204/205)
                 zedei.near    interface / automation
     |
OUTPOSTS         Ethereum · Sui · TON · Tron · Aptos   (each capped)
```

## The core is a chain inside a contract

`unog.near` keeps its own accounts, balances, nonces and keys — separate from
NEAR's account model. It is 1,156,670 bytes and has **zero access keys**.

Storage key derivation:

```
account record : 0x00 ‖ sha256("A" ‖ account_id)
balance record : sha256("B" ‖ account_id ‖ asset_id)
NEAR → L2 map  : sha256("near-account:" ‖ accountId)
```

**There is no prefix scan.** A balance key hashes its preimage, so the account
set is opaque while every individual balance stays provable. That is deliberate.

### The consequence everyone hits

Minting credits an **internal account**, not a wallet:

```
deposit  →  internal balance   (visible only in contract storage)
export   →  NEP-141 wallet     (visible everywhere)
```

A user who mints and sees nothing has not lost anything — the tokens are in the
ledger, one export away. Any interface that shows both steps removes the entire
class of support question.

## The four-valued state machine

Every claim evaluates to one of four values, and only `TRUE` settles. See
[FOUR-VALUED-LOGIC.md](FOUR-VALUED-LOGIC.md) for the full treatment.

## The token

TIAMAT (PQOS), 24 decimals, NEP-141, contract `unog.near`.

```
backing per new TIAMAT = phi^(21 × supply / cap) NEAR
```

Because the exponent rises with supply, collateral per token rises
monotonically. Issuance is bounded by collateral, not by time. Redemption burns
the token and returns a pro-rata slice of the reserve.

**No admin mint.** The contract has zero access keys.

## The bridge

```
lock PQOS on NEAR  →  3-of-5 attestation  →  mint on destination
fee: 889 ppm, funds destination-chain gas
```

Each outpost is pinned to the core by an immutable code hash and carries an
immutable supply cap. **Attested, not trustless** — a 3-of-5 quorum can mint up
to the cap and not one token beyond it.

## What is proven, and what is not

| Claim | Status |
|---|---|
| 12 contracts deployed, hashes published | verified against chain |
| 8 sealed with zero access keys | verified |
| Mint, redeem, export, transfer | proven on-chain |
| Internal AMM create/add/swap/remove | proven on-chain |
| Lock → attest → mint on Ethereum | proven — 0.5 PQOS route completed |
| Deep liquidity | **not yet** — Ref pool holds 12.6 wNEAR |
| Trustless bridging | **no** — 3-of-5 attested, cap-bounded |
| Third-party audit | **none** |
| Front-end | **does not exist** |

The last four are the ones a reviewer should check first.
