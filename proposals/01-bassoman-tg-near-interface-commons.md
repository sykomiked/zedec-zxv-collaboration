# White paper — NEAR Interface Commons

**Recipient:** `bassoman.tg`
**Contact:** https://nearbuilders.org/builders/bassoman.tg
**Their project:** NEAR Interface Commons (`near-interface-commons-a-shared-abi-registry-for-the-contracts-that-ship-without-one-3t22ei`)
**Tier:** 1
**From:** `jollydragonroger.near` — ZEDEC/ZXV

---

## What you are building

An open registry of contract interfaces, keyed by code hash, recovered once from
on-chain call history, confirmed by the contract owner where possible, and reused
by every wallet, explorer and AI agent instead of being re-guessed each time.

It is the correct idea. The reason it has not happened is that the people who
hold the interfaces have no incentive to publish them — publishing costs effort
and returns nothing to the publisher.

We are a counterexample, and we would like to be your first entry.

## What we already have

| | |
|---|---|
| Contracts | **12** on NEAR mainnet |
| ABI descriptors | **214** |
| Operations | **151** across 12 layers |
| Governance kinds | **46** |
| Code hashes | published, one per contract, verified against chain |
| Access keys | **0** on eight of the twelve — sealed |

Every contract is identified by a code hash we publish and can prove:

```
unog.near      Ae5uDVYKhZpwgCBDTcSQGk26azY4ytzBH69kUL2FD8y5   214 descriptors
zedec.near     ATUV46Keb91L32RGU5X858nNtTZ6csH9HARfE86MtMo
scp144.near    DDQ4uJXM26WhRoYfRPgQcUKPpybzhGrBXmCbK7e85dmN9
zedei.near     CRZgm89Yo8JsU6WgFjFmkrU8BRDZfMvieKQ2hozDLwjZ
… 8 more
```

Your registry's hardest problem is **confirmation** — knowing that the interface
a tool recovered actually belongs to the contract. Our contracts are sealed with
zero access keys, so the code hash cannot change. A descriptor keyed to our hash
is correct forever. That is a stronger guarantee than "the owner confirmed it".

## How it integrates

**Step 1 — ingest.** Take our published descriptor set:

```
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/ARCHITECTURE.md          operation and payload layouts
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/CONTRACT_ADDRESSES.md    account → code hash → role
https://github.com/sykomiked/zedec-zxv-deployment/tree/main/build-artifacts          compiled WASM, hash-verified
```

**Step 2 — key by code hash.** Each entry maps
`Ae5uDVYK…` → the 214-descriptor table for `unog.near`. Not by account name —
by hash, so a redeploy invalidates the entry automatically.

**Step 3 — verify.** One command proves the binary:

```bash
git clone https://github.com/sykomiked/zedec-zxv-deployment
cd zedec-zxv-deployment && ./tools/verify.sh
```

It fetches `view_code` from chain, hashes it, compares to the published file and
to the code hash. Twelve contracts, exit 0 means all agree.

**Step 4 — publish.** Your registry lists us as the worked example: a contract
set with a complete interface, a sealed hash, and a reproducible verification
path.

## Why this is worth your time

- **You get a complete, verified first entry** — not a stub. 214 descriptors,
  twelve contracts, one verification command.
- **You get a proof of the confirmation model.** Sealed contracts are the
  strongest case: the hash cannot move, so the interface cannot go stale.
- **You get a template.** If your format can express our 214 descriptors across
  12 layers, it can express anything on NEAR.
- **You get the argument for the next ten entries.** "This is how ZEDEC/ZXV did
  it" is a much easier ask than "please publish your ABI".

## What we are asking

Use us as the reference entry. Tell us what schema you want the descriptors in
and we will emit them in it. If your format needs a field we do not have, say so
and we will add it — we control the source.

We are not asking for promotion or a listing. We are asking to be the example
that makes the registry credible on day one.

## Proof you can check before replying

```
https://github.com/sykomiked/zedec-zxv-deployment
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/CONTRACT_ADDRESSES.md
https://github.com/sykomiked/zedec-zxv-deployment/blob/main/ARCHITECTURE.md
```

---

## Ready-to-send message

```
Hi — I'm the builder behind ZEDEC/ZXV (12 contracts on NEAR mainnet, 214 ABI descriptors, all sealed with zero access keys).

Your Interface Commons idea solves a real problem, and I think I can be your first entry rather than your first request.

What I have: 214 descriptors across 12 contracts, every one keyed to a published code hash. Eight of the twelve have zero access keys, so the hash cannot change — which means a descriptor keyed to it is correct permanently. That is a stronger confirmation than an owner's word.

What I'd want: your schema. Tell me the format and I'll emit our descriptors into it.

Repo with the full detail: https://github.com/sykomiked/zedec-zxv-deployment

Worth a conversation?
```
