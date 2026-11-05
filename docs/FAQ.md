# FAQ — the questions worth asking

## Is this actually deployed, or a mock-up?

Deployed. 12 contracts on NEAR mainnet, every code hash readable:

```bash
near view unog.near ft_metadata --nodeUrl https://rpc.mainnet.near.org
```

If that returns TIAMAT/PQOS/24, it is live.

## Who controls it?

Nobody. `unog.near` and seven others have **zero access keys**. There is no
admin function, no upgrade path, no pause, no recovery.

```bash
near view-access-keys unog.near --nodeUrl https://rpc.mainnet.near.org
# → []
```

That is not a policy — it is a property of the account.

## Can the supply be inflated?

No. There is no mint authority. Every token in existence was created by someone
depositing NEAR collateral.

## Then how do new tokens get created?

A minter deposits NEAR. The price rises with supply:

```
backing per new TIAMAT = phi^(21 × supply / cap) NEAR
```

Early minters pay less than late ones, and nobody can accelerate issuance by
waiting.

## Why is the supply so small?

61.47 PQOS. Because every token required collateral. That is the design
working, not failing — but it has a real consequence: there is not enough float
for a deep market.

## Why is 93.6% in one wallet?

Because one person bought it with collateral. There was no premine, no ICO, no
team allocation. It is the honest state of a token that launched recently.

## Is the bridge trustless?

**No.** A 3-of-5 attestor quorum signs every cross-chain mint. Each outpost
carries an immutable cap that bounds what a compromised quorum could create.
Attested and cap-bounded, not trustless. We say so on the first page.

## Has it been audited?

**No.** Not by any third party. The code is sealed and unaudited. That is the
largest credibility gap in the project and it is stated rather than hidden.

## Can I rebuild the binary?

No. The source is withheld. Verification is complete; rebuilding is not. See
[VERIFICATION.md](VERIFICATION.md).

## What is the four-valued logic actually for?

Representing contradictions without destroying them. When two valid claims
conflict, the system records `BOTH` and releases nothing, rather than picking a
winner and losing the evidence. See [FOUR-VALUED-LOGIC.md](FOUR-VALUED-LOGIC.md).

## Is that not just a fancy "unknown" state?

No. `NEITHER` is "nothing verifiable". `BOTH` is "two valid claims that
conflict". They are different failures and they need different handling — an
oracle timeout is `NEITHER`; two oracles disagreeing is `BOTH`.

## Why build a chain inside a contract?

Because the alternative is a separate L1, which means a separate validator set,
a separate security budget, and a separate bridge. Running inside NEAR inherits
NEAR's security and its finality without a new consensus layer.

## What is the cost of that choice?

The core cannot be patched. A bug in `unog.near` is permanent — there is no
upgrade path. Every future change is a new satellite contract. That is the
trade: no rug vector, and no rollback.

## Why is there no front-end?

Because one person built the protocol and ran out of time. It is the binding
constraint on adoption and it is stated plainly in every proposal.

## What do you actually want from me?

Read your proposal. If it is wrong about your project, say so — that is the
most useful thing you can do. If something in it is right, the repository is
open.
