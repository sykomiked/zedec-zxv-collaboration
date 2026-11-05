# Verification

Everything in these proposals is checkable. This is how.

## One command

```bash
git clone https://github.com/sykomiked/zedec-zxv-deployment
cd zedec-zxv-deployment && ./tools/verify.sh
```

It checks all 12 contracts against mainnet, confirms 8 are sealed with zero
keys, verifies the QC log hash equals the deployed hash, and reads token
metadata. Read-only RPC, no keys, no gas. Exit 0 means everything agrees.

## The provenance chain

```
QC log recorded : 8f3936888224eee740353b669b6eaaf1401db3ad5d20566c50c0c5d961fc3050
published file  : 8f3936888224eee740353b669b6eaaf1401db3ad5d20566c50c0c5d961fc3050
base58 of that  : Ae5uDVYKhZpwgCBDTcSQGk26azY4ytzBH69kUL2FD8y5
chain reports   : Ae5uDVYKhZpwgCBDTcSQGk26azY4ytzBH69kUL2FD8y5
```

A test log written **before** deployment, a file published **after** it, and
the live chain all carry the same value. Tested, published and running are the
same bytes. Most projects cannot show a test log that predates deployment and
records the same digest.

## Check the seal yourself

```bash
near view-access-keys unog.near --nodeUrl https://rpc.mainnet.near.org
# → []
```

Empty means no admin, no upgrade, no pause, no recovery. Eight contracts return
this.

## Check the token

```bash
near view unog.near ft_metadata --nodeUrl https://rpc.mainnet.near.org
# {"spec":"ft-1.0.0","name":"TIAMAT","symbol":"PQOS","decimals":24}
```

## Read a balance record directly

Balance records are `sha256("B" ‖ account_id ‖ asset_id)`. No prefix scan —
compute the key for a candidate and look.

```python
import hashlib
key = hashlib.sha256(b'B' + account32 + asset32).digest()
# then view_state on unog.near with prefix_base64 = base64(key)
```

## The QA record

| Gate | Result |
|---|---|
| Host suite, ASan + UBSan | 1,858,226 checks, 0 failed |
| VM gate, 26 scenarios in NEAR's runtime | QC: PASS, 0 wrong |
| Strict wasm MVP | 807 function bodies, 990,140 code bytes |
| Determinism | plain and `-j16` builds byte-identical |
| Floating point in code | none |

Logs: `build-logs/` in the main repository — actual output, not a summary.

## What cannot be verified, and why

| Not verifiable | Reason |
|---|---|
| Rebuild from source | source withheld — it is the project's property |
| Third-party audit | none exists |
| Future behaviour | the core is sealed, but unaudited code is unaudited |

Verification is complete. Rebuilding is not. Those are different claims and
they are kept separate deliberately.
