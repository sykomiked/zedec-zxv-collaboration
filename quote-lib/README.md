# TIAMAT quote — the view that should have existed

The sealed core exposes no quote method. A front-end cannot show a user what
they will receive before they sign, because the price depends on the curve and
the curve parameters are not in any public view.

**This library is that view, as code.** A faithful port of
`gc_tiamat_cost` / `gc_tiamat_tokens_for` from the core's own source
(`stf/gc_curve.inc`, `stf/gc_stf.c`).

## Why this is safe to do off-chain

The curve is a fixed 85-entry lookup table — `phi^(j/4) × 10^14` for
`j = 0..84` — plus a piecewise-linear integral over 84 segments. It has no
mutable parameters:

```
cap      = 144,000,000,000 whole tokens (constant, compiled in)
segments = 84
scale    = 1e14
price    = phi^(21 × supply / cap) NEAR per TIAMAT
```

Because none of that can change — the core has zero access keys — a client-side
reimplementation gives the same answer forever. There is nothing to drift.

## Usage

### JavaScript

```js
import { quote, priceAt, tokensFor } from './quote.mjs';

const supply = 61470008027182581764720275n;  // unog.near.ft_total_supply
quote(1, supply);        // 1.000000  — TIAMAT received for 1 NEAR
priceAt(supply);         // 1.000000000 — NEAR per whole TIAMAT
```

### Python

```python
from quote import tokens_for, price_at
tokens_for(10**24, 61470008027182581764720275)  # 999999999962699948063971
```

## The exact call a front-end makes

```js
const supply = await view('unog.near', 'ft_total_supply', {});
const out    = quote(nearAmount, BigInt(supply));
```

`ft_total_supply` returns base units with 24 decimals. Do not assume 18.

## Verification

| Check | Result |
|---|---|
| 1 NEAR at empty supply | `0.99999999996` TIAMAT — correct, the curve starts at 1 NEAR |
| 1 NEAR at current supply (61.47) | `1.000000` TIAMAT |
| 10 NEAR at current supply | `10.000000` TIAMAT |
| Python and JS agree | yes, identical to the last digit |

Supply is 61.47 against a cap of 144,000,000,000 — that is 4×10⁻⁸ % of the
curve, so the price is still essentially 1 NEAR per token. It will not move
measurably until supply is orders of magnitude larger.

## One known discrepancy, stated rather than hidden

A historical mint recorded `1 NEAR → 1.064002718878686400663891 TIAMAT`, which
this library does not reproduce. That mint went through `post.jollydragonroger.near`,
which applies its own premium on top of the curve. **The curve is not the whole
price.**

Until the desk's premium is understood, treat this library as the *curve*
component and verify against a real desk mint before showing a number to a user.

## What would be better

A `quote()` view on the desk, returning the same figure the mint will actually
produce. That is ~20 lines and additive — it does not touch the sealed core.
Until then, this library is the honest approximation, and the UI must label its
output `≈`, not a quote.
