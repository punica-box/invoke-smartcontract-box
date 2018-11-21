# invoke-smartcontract-box

this box implements how to invoke another contract in one contract.

smart contract `init_advanced` will invoke smart contract `contract_a`.

## Usage

1. compile contract_a

```
punica compile --contracts ./contracts/contract_a.py
```

2. deploy contract_a

```
punica deploy --avm ./contracts/build/contract_a.avm
```

4. compile init_advanced

```
punica compile
```

5. deploy init_advanced

```
punica deploy
```

6. invoke

```
punica invoke --functions invokeA
```
