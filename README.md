# pystratis
Python package for interacting with Stratis (STRAX) full node and Cirrus/Interflux sidechain.

## Installation
### From the Python Package Index (PyPi)
`pip install pystratis`

### Most recent (from GitHub)
`pip install git+https://github.com/stratisproject/pystratis.git`

### Install from PyPi with test dependencies
`pip install pystratis[test]`

## Tutorials
- [Node and network basics](https://github.com/stratisproject/pyStratis/blob/master/tutorials/NodeAndNetworkBasics.md)
- [Using Pystratis.core](https://github.com/stratisproject/pyStratis/blob/master/tutorials/CoreBasics.md)
- [Wallet basics](https://github.com/stratisproject/pyStratis/blob/master/tutorials/WalletBasics.md)
- [Sending a transaction](https://github.com/stratisproject/pyStratis/blob/master/tutorials/SendingTransaction.md)
- [Smart contract basics](https://github.com/stratisproject/pyStratis/blob/master/tutorials/SmartContracts.md)
- [Sending a CrossChain Transaction](https://github.com/stratisproject/pyStratis/blob/master/tutorials/SendingCrossChainTransaction.md)
- [ColdStaking](https://github.com/stratisproject/pyStratis/blob/master/tutorials/ColdStaking.md)

## Basic examples

### Create a wallet

```python
from pystratis.nodes import StraxNode

node = StraxNode()

# Back up the mnemonic phrase, that's the only thing that could restore your wallet.
mnemonic = node.wallet.create(name='MyWallet', password='qwerty12345', passphrase='')
```

### Send funds

```python
from pystratis.nodes import StraxNode
from pystratis.core.networks import StraxMain
from pystratis.core.types import uint256, Money, Address
from pystratis.core import Outpoint, Recipient

node = StraxNode()

# Get first spendable transaction.
s_tx = node.wallet.spendable_transactions(wallet_name='MyWallet').transactions[0]

# Set our own address as recipient of change, use Money arithmetic for amount calculations.
recipient_self = Recipient(destinationAddress=s_tx.address, amount=s_tx.amount - Money(1.0),
                           subtraction_fee_from_amount=True)

recipient_another = Recipient(destinationAddress=Address('<another address>', network=StraxMain()), amount=Money(1.0),
                              subtractFeeFromAmount=False)

# Spend utxo from our transaction.
outpoint = Outpoint(transaction_id=s_tx.transaction_id, index=s_tx.index)

built_transaction = node.wallet.build_transaction(wallet_name='MyWallet', password='qwerty12345', outpoints=[outpoint],
                                                  recipients=[recipient_self, recipient_another], fee_type='high')

node.wallet.send_transaction(built_transaction.hex)
```

## Testing guide

- Unit tests: `pytest -m "not integration_test"`
- Strax integration tests: `pytest -m "strax_integration_test"`
- Cirrus integration tests: `pytest -m "cirrus_integration_test"`
- Interflux integration tests: `pytest -m "interflux_integration_test"`
- Mainnet integration tests: `pytest -m "mainnet_test"`  
- Integration tests: `pytest -m "integration_test"`
- Everything: `pytest`
- Coverage: `coverage run -m pytest`
- Coverage report: `coverage report -m`

## ReadTheDocs documentation
ReadTheDocs API documentation can be found at [http://pystratis.readthedocs.io](http://pystratis.readthedocs.io).

Documentation can be build locally with the following commands: 
```commandline
cd doc_build
make html 
```
- Other output options: `make help`
- After building, documentation for `make html` can be found in [docs/html/index.html](docs/html/index.html), open with your favorite browser. 

# Credit

Thanks goes to [@TjadenFroyda](https://github.com/tjadenfroyda) for his contributions in kickstarting this repository.

# ChangeLog
### Version 1.0.0.x (StratisFullNode release/1.0.9.0)
- Initial pystratis release