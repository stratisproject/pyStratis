Sending a Cross-Chain Transaction with Pystratis
================================================
Cross-chain transactions on the Stratis Platform are mediated by the multisig federation. 

The destination address on the destination chain is encoded in the OP_RETURN data of a transaction. 

__WARNING: Mistyped addresses in a transaction's OP_RETURN field could lead to loss of funds on transfer.__ 

__In pystratis, you can prevent this error by validating the destination address in the OP_RETURN field using the [Address type](https://pystratis.readthedocs.io/en/latest/source/pystratis.core.types.html#module-pystratis.core.types.address) while building the transaction.__

For more details on building and sending transactions, please refer to the [sending a transaction tutorial](https://github.com/stratisproject/pyStratis/blob/master/tutorials/SendingTransaction.md). 

## Strax to Cirrus
To send a transaction from Stratis to Cirrus: 
- Use the Strax federation multisig address for destination address in [Recipients](https://pystratis.readthedocs.io/en/latest/source/pystratis.core.html#module-pystratis.core.recipient)
```python
from pystratis.nodes import StraxNode
from pystratis.core import Outpoint, Recipient
from pystratis.core.types import Address
from pystratis.core.networks import StraxMain, CirrusMain
node = StraxNode()

multisig_address = Address(address='yU2jNwiac7XF8rQvSk2bgibmwsNLkkhsHV', network=StraxMain())

# Sending to the cirrus multisig address in this example. You'll want to put your Cirrus address here.
crosschain_address = Address(address='cYTNBJDbgjRgcKARAvi2UCSsDdyHkjUqJ2', network=CirrusMain())
response = node.wallet.build_transaction(
    fee_amount=fee_amount,
    password='abc123',
    segwit_change_address=False,
    wallet_name='ExampleWallet',
    account_name='account 0',
    outpoints=[Outpoint(transaction_id=x.transaction_id, index=x.index) for x in transactions],
    recipients=[Recipient(destination_address=multisig_address, subtraction_fee_from_amount=True, amount=amount_to_send)],
    allow_unconfirmed=False,
    shuffle_outputs=True,
    change_address=change_address,
    op_return_data=crosschain_address
)
```
Once built, use [`node.wallet.send_transaction()`](https://pystratis.readthedocs.io/en/latest/source/pystratis.api.wallet.html#pystratis.api.wallet.Wallet.send_transaction)  as in the [sending a transaction tutorial](https://github.com/stratisproject/pyStratis/blob/master/tutorials/SendingTransaction.md).

## Cirrus to Strax
To send a transaction from Cirrus to Strax: 
- Use the Cirrus federation multisig address for destination address in [Recipients](https://pystratis.readthedocs.io/en/latest/source/pystratis.core.html#module-pystratis.core.recipient)
```python
from pystratis.nodes import CirrusNode
from pystratis.core import Outpoint, Recipient
from pystratis.core.types import Address
from pystratis.core.networks import StraxMain, CirrusMain
node = CirrusNode()

multisig_address = Address(address='cYTNBJDbgjRgcKARAvi2UCSsDdyHkjUqJ2', network=CirrusMain())

# Sending to the strax multisig address in this example, you will want to put your destination Strax address here.
crosschain_address = Address(address='yU2jNwiac7XF8rQvSk2bgibmwsNLkkhsHV', network=StraxMain())

response = node.wallet.build_transaction(
    fee_amount=fee_amount,
    password='abc123',
    segwit_change_address=False,
    wallet_name='ExampleWallet',
    account_name='account 0',
    outpoints=[Outpoint(transaction_id=x.transaction_id, index=x.index) for x in transactions],
    recipients=[Recipient(destination_address=multisig_address, subtraction_fee_from_amount=True, amount=amount_to_send)],
    allow_unconfirmed=False,
    shuffle_outputs=True,
    change_address=change_address,
    op_return_data=crosschain_address
)
```
Once built, use [`node.wallet.send_transaction()`](https://pystratis.readthedocs.io/en/latest/source/pystratis.api.wallet.html#pystratis.api.wallet.Wallet.send_transaction)  as in the [sending a transaction tutorial](https://github.com/stratisproject/pyStratis/blob/master/tutorials/SendingTransaction.md).

## Ethereum Interflux transactions
Interflux transactions also use OP_RETURN for address encoding. For details on how this is done on the C# node, please see [official implementation details here](https://github.com/stratisproject/StratisFullNode/blob/master/src/Stratis.Bitcoin.Features.Wallet/InterFluxOpReturnEncoder.cs).

In summary, the destination address is prefixed with 'INTER' + int + '_', where the integer is an enumeration representing the [destination chain](https://pystratis.readthedocs.io/en/latest/source/pystratis.core.html#module-pystratis.core.destinationchain).

For example, sending to Vitalik's public eth address would be encoded in the OP_RETURN field as `INTER1_0xab5801a7d398351b8be11c439e05c5b3259aec9b`.

The Stratis team has built an API endpoint that handles this functionality under the hood: `/api/wallet/build-interflux-transaction`. 

This endpoint can be called in pystratis using the [`node.wallet.build_interflux_transaction()` method](https://pystratis.readthedocs.io/en/latest/source/pystratis.api.wallet.html#pystratis.api.wallet.Wallet.build_interflux_transaction).

### Strax to Eth via Interflux Gateway
To send a transaction from Stratis to Eth: 
- Use the Strax federation multisig address for destination address in [Recipients](https://pystratis.readthedocs.io/en/latest/source/pystratis.core.html#module-pystratis.core.recipient)
```python
from pystratis.nodes import StraxNode
from pystratis.core import Outpoint, Recipient, DestinationChain
from pystratis.core.types import Address
from pystratis.core.networks import StraxMain, Ethereum
node = StraxNode()

multisig_address = Address(address='yU2jNwiac7XF8rQvSk2bgibmwsNLkkhsHV', network=StraxMain())

# Sending to Vitalik's ethereum address in this example. You'll want to put your Ethereum address here.
eth_address = Address(address='0xab5801a7d398351b8be11c439e05c5b3259aec9b', network=Ethereum())
response = node.wallet.build_interflux_transaction(
    destination_chain=DestinationChain.ETH,
    destination_address=crosschain_address,
    fee_amount=fee_amount,
    password='abc123',
    segwit_change_address=False,
    wallet_name='ExampleWallet',
    account_name='account 0',
    outpoints=[Outpoint(transaction_id=x.transaction_id, index=x.index) for x in transactions],
    recipients=[Recipient(destination_address=multisig_address, subtraction_fee_from_amount=True, amount=amount_to_send)],
    allow_unconfirmed=False,
    shuffle_outputs=True,
    change_address=change_address
)
```
Once built, use [`node.wallet.send_transaction()`](https://pystratis.readthedocs.io/en/latest/source/pystratis.api.wallet.html#pystratis.api.wallet.Wallet.send_transaction) as in the [sending a transaction tutorial](https://github.com/stratisproject/pyStratis/blob/master/tutorials/SendingTransaction.md).
### Cirrus to Eth via Interflux Gateway
To send a transaction from Cirrus to Eth: 
- Use the Cirrus federation multisig address for destination address in [Recipients](https://pystratis.readthedocs.io/en/latest/source/pystratis.core.html#module-pystratis.core.recipient)
```python
from pystratis.nodes import CirrusNode
from pystratis.core import Outpoint, Recipient, DestinationChain
from pystratis.core.types import Address
from pystratis.core.networks import CirrusMain, Ethereum
node = CirrusNode()

multisig_address = Address(address='cYTNBJDbgjRgcKARAvi2UCSsDdyHkjUqJ2', network=CirrusMain())

# Sending to Vitalik's ethereum address in this example. You'll want to put your Ethereum address here.
eth_address = Address(address='0xab5801a7d398351b8be11c439e05c5b3259aec9b', network=Ethereum())

response = node.wallet.build_interflux_transaction(
    destination_chain=DestinationChain.ETH,
    destination_address=eth_address,
    fee_amount=fee_amount,
    password='abc123',
    segwit_change_address=False,
    wallet_name='ExampleWallet',
    account_name='account 0',
    outpoints=[Outpoint(transaction_id=x.transaction_id, index=x.index) for x in transactions],
    recipients=[Recipient(destination_address=multisig_address, subtraction_fee_from_amount=True, amount=amount_to_send)],
    allow_unconfirmed=False,
    shuffle_outputs=True,
    change_address=change_address
)
```
Once built, use [`node.wallet.send_transaction()`](https://pystratis.readthedocs.io/en/latest/source/pystratis.api.wallet.html#pystratis.api.wallet.Wallet.send_transaction)  as in the [sending a transaction tutorial](https://github.com/stratisproject/pyStratis/blob/master/tutorials/SendingTransaction.md).