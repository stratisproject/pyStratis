# pystratis
Python package for interacting with Stratis (STRAX) full node and Cirrus/Interflux sidechain.

## Basic models example

### Private key

```python
from pystratis.core import Key

private_key = Key('5HwoXVkHoRM8sL2KmNRS217n1g8mPPBomrY7yehCuXC1115WWsh')
same_private_key = Key(private_key.get_bytes())

assert private_key == same_private_key
assert private_key.generate_wif_key() == same_private_key.generate_wif_key()
assert str(private_key_from_str) == str(private_key_from_bytes)
```

### Public key

```python
from pystratis.core import PubKey

pubkey_compressed = PubKey('034f355bdcb7cc0af728ef3cceb9615d90684bb5b2ca5f859ab0f0b704075871aa')
pubkey_uncompressed = PubKey(pubkey_compressed.uncompressed())

assert pubkey_compressed.x == pubkey_uncompressed.x
assert pubkey_compressed.y == pubkey_uncompressed.y
```

### Extended private key

```python
from pystratis.core import ExtKey

extended_private_key = ExtKey('4Qzpnt5o8msy6thbuFEHTr4yFqp8yvywYBhrtHLJNKEHDhidjbCVvdjuXA2V9k6Bg39FJjfbqpasUmnNYBfZZY27')
another_extended_private_key = ExtKey(extended_private_key.get_bytes())

assert extended_private_key.generate_private_key_bytes() == another_extended_private_key.generate_private_key_bytes()
assert extended_private_key.generate_chain_code_bytes() == another_extended_private_key.generate_chain_code_bytes()
```

### Extended public key

```python
from pystratis.core import ExtPubKey

extended_public_key = ExtPubKey('6FHa3pjLCk84BayeJxFW2SP4XRrFd1JYnxeLeU8EqN3vDfZmbqBqaGJAyiLjTAwm6ZLRQUMv1ZACTj37sR62cfN7fe5JnJ7dh8zL4fiyLHV')
another_extended_public_key = ExtPubKey(str(extended_public_key))

assert extended_public_key == another_extended_public_key
```

## Examples

### Create wallet

```python
from pystratis.nodes import StraxNode

node = StraxNode()

# back up the mnemonic phrase, that's the only thing that could restore your wallet
mnemonic = node.wallet.create(name='MyWallet', password='qwerty12345', passphrase='')
```

### Send funds

```python
from pystratis.nodes import StraxNode
from pystratis.core.networks import StraxMain
from pystratis.core.types import uint256, Money, Address
from pystratis.core import Outpoint, Recipient

node = StraxNode()

# get first spendable transaction
s_tx = node.wallet.spendable_transactions(wallet_name='MyWallet').transactions[0]

# set our own address as recipient of change, use Money arithmetics for amount calculations
recipient_self = Recipient(destinationAddress=s_tx.address, amount=s_tx.amount - Money(1.0),
                           subtraction_fee_from_amount=True)

recipient_another = Recipient(destinationAddress=Address('<another address>', network=StraxMain()), amount=Money(1.0),
                              subtractFeeFromAmount=False)

# spend utxo from our transaction
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

Thanks goes to [@TjadenFroyda](https://github.com/tjadenfroyda) for his contributions in kickstarting this repositoriy.
