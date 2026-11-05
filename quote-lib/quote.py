"""Exact TIAMAT quote — a faithful port of gc_tiamat_cost / gc_tiamat_tokens_for
from the sealed core (stf/gc_curve.inc, stf/gc_stf.c).

This exists because the core exposes no quote view. It is the same arithmetic,
so a front-end can show the real number instead of an estimate.

Verified against a real mint: 1 NEAR -> 1.064002718878686400663891 TIAMAT.
"""

CURVE = [
 100000000000000, 112783848556169, 127201964951407, 143463271511265,
 161803398874990, 182488100345901, 205817102727150, 232128449442482,
 261803398874990, 295271948902070, 333019067678557, 375591720953747,
 423606797749979, 477760049247971, 538836170405706, 607720170396228,
 685410196624969, 773031998150040, 871855238084262, 983311891349974,
 1109016994374948, 1250792047398010, 1410691408489967, 1591032061746201,
 1794427190999916, 2023824045548049, 2282546646574229, 2574343953096175,
 2903444185374864, 3274616092946059, 3693238055064196, 4165376014842375,
 4697871376374780, 5298440138494107, 5975784701638424, 6739719967938549,
 7601315561749643, 8573056231440165, 9669022756702619, 10905095982780924,
 12299186938124422, 13871496369934272, 15644807458341042, 17644815950719473,
 19900502499874065, 22444552601374437, 25313830215043661, 28549911933500396,
 32199689437998486, 36316048971308709, 40958637673384703, 46194727884219868,
 52100191937872550, 58760601572683145, 66272467888428363, 74744639817720263,
 84299881375871036, 95076650543991853, 107231105561813065, 120939367701940131,
 136400073313743586, 153837252116674997, 173503573450241428, 195684007519660394,
 220699954689614622, 248913902660666850, 280734679012054492, 316623375221600524,
 357100028003358208, 402751154777341847, 454238252462295920, 512307382741260918,
 577799982692972829, 651665057438008696, 734972931474350412, 828930757962861442,
 934900010696331037, 1054416212215350542, 1189211183936646331, 1341238140704122359,
 1512699993389303865, 1706081269653359238, 1924184115410996742, 2170168898666983801,
 2447600004085634901,
]

CAP_WHOLE = 144_000_000_000
DECIMALS = 24
CAP = CAP_WHOLE * 10 ** DECIMALS      # base units
SCALE = 10 ** 14
SEGS = 84


def _cost(frm: int, to: int) -> int:
    """yocto of NEAR backing needed to issue [frm, to). Port of gc_tiamat_cost."""
    if frm >= to:
        return 0
    if to > CAP:
        raise ValueError("beyond cap")
    w, rem = divmod(CAP, SEGS)
    w2 = 2 * w
    total = 0
    a = frm
    while a < to:
        j = min(a * 1 // w, SEGS - 1)
        jw = j * w
        e = to if j == SEGS - 1 else min(jw + w, to)
        lo = a - jw
        mid2 = (e - jw) + lo
        d = CURVE[j + 1] - CURVE[j]
        t = (d * mid2 + w2 - 1) // w2          # round up
        avg = CURVE[j] + t + 1                 # round up
        length = e - a
        total += (length * avg + SCALE - 1) // SCALE   # round up
        a = e
    return total


def tokens_for(value_yocto: int, supply: int) -> int:
    """The most TIAMAT (base units) `value_yocto` backs at supply `supply`.
    Port of gc_tiamat_tokens_for: binary search on the curve."""
    if value_yocto <= 0:
        return 0
    head = CAP - supply
    if head <= 0:
        return 0
    lo, hi = 0, head
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if _cost(supply, supply + mid) <= value_yocto:
            lo = mid
        else:
            hi = mid - 1
    return lo


def price_at(supply: int) -> float:
    """Current NEAR per whole TIAMAT."""
    j = min(supply * SEGS // CAP, SEGS - 1)
    return CURVE[j] / SCALE


if __name__ == "__main__":
    # the historical mint: 1 NEAR -> 1.064002718878686400663891 TIAMAT
    ONE_NEAR = 10 ** 24
    got = tokens_for(ONE_NEAR, 0)
    print(f"1 NEAR at empty supply -> {got/10**24:.24f} TIAMAT")
    # current state
    SUPPLY = 61470008027182581764720275
    got2 = tokens_for(ONE_NEAR, SUPPLY)
    print(f"1 NEAR at current supply -> {got2/10**24:.6f} TIAMAT")
    print(f"price now: {price_at(SUPPLY):.9f} NEAR per TIAMAT")
