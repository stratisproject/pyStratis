Sending a Standard Transaction with Pystratis
=============================================
When you used a wallet GUI to send a transaction, several steps to build the transaction are hidden from the user.
These include:
- Retrieving a list of spendable outputs
- Building the transaction
- Signing the transaction
- Broadcasting the transaction. Details about performing these steps will be covered in this tutorial.

## Retrieving spendable utxo
The spendable_transactions method returns a [SpendableTransactionsModel](https://pystratis.readthedocs.io/en/latest/source/pystratis.api.wallet.html?pystratis.api.wallet.responsemodels.spendabletransactionsmodel.SpendableTransactionsModel#pystratis.api.wallet.responsemodels.spendabletransactionsmodel.SpendableTransactionsModel), 
which contains a list of [SpendableTransactionModel](https://pystratis.readthedocs.io/en/latest/source/pystratis.api.wallet.html?pystratis.api.wallet.responsemodels.spendabletransactionsmodel.SpendableTransactionsModel#pystratis.api.wallet.responsemodels.spendabletransactionsmodel.SpendableTransactionModel). 

```python
from pystratis.nodes import StraxNode
from pystratis.api.wallet.responsemodels import SpendableTransactionsModel
node = StraxNode()
s_txs: SpendableTransactionsModel = node.wallet.spendable_transactions(wallet_name='ExampleWallet')

# Re-order the spendable transactions smallest to largest to preferentially use low value utxos.
s_txs = [x for x in s_txs.transactions]
s_txs = sorted(s_txs, key=lambda x: x.amount)
```
## Building and signing a transaction
In this example we are going to send a transaction to an unused address on our node.

See [Recipient](https://pystratis.readthedocs.io/en/latest/source/pystratis.core.html#module-pystratis.core.recipient) and [Outpoint](https://pystratis.readthedocs.io/en/latest/source/pystratis.core.html#module-pystratis.core.outpoint) for details on usage below.

The result of the build_transaction call is a [BuildTransactionModel](https://pystratis.readthedocs.io/en/latest/source/pystratis.api.global_responsemodels.html#pystratis.api.global_responsemodels.buildtransactionmodel.BuildTransactionModel). The transaction hex is then ready for broadcasting. 
```python
from pystratis.core import Outpoint, Recipient
from pystratis.core.types import Money
# First we want to define the destination address.
destination_address = node.wallet.unused_address(wallet_name='ExampleWallet')
# The change address is optional. In this case, we are sending any change back to an adress that has a balance.
change_address = node.wallet.balance(
    wallet_name='ExampleWallet', include_balance_by_address=True
).balances[0].addresses[0].address

# Here we are setting a fee (rather than using the fee estimation API call).
fee_amount = Money(0.0001)
amount_to_send = Money(1)

# After declaring the amount being sent, we need to include enough utxos as transaction 
# inputs such that the sum of the input amounts >= the amount being sent.
# The for loop below is one way to accomplish this. 
transactions = []
trxid_amount = Money(0)
for spendable_transaction in s_txs:
    transactions.append(spendable_transaction)
    trxid_amount += spendable_transaction.amount
    if trxid_amount >= amount_to_send: # Can add fee here if not subtracting from amount below.
        break

# The last elements of the transaction to build are the outpoints and the recipients.
# The outpoints are built from the utxos in the previous step. The list comprehension below does this efficiently.
# The recipient list can be 1 or more recipient, but the sum must be less than the amount contained in included utxos.
response = node.wallet.build_transaction(
    fee_amount=fee_amount,
    password='abc123',
    segwit_change_address=False,
    wallet_name='ExampleWallet',
    account_name='account 0',
    outpoints=[Outpoint(transaction_id=x.transaction_id, index=x.index) for x in transactions],
    recipients=[Recipient(destination_address=destination_address, subtraction_fee_from_amount=True, amount=amount_to_send)],
    allow_unconfirmed=False,
    shuffle_outputs=True,
    change_address=change_address
)

# Broadcast the successfully built transaction
response = node.wallet.send_transaction(transaction_hex=response.hex)
```
### Special case: Offline signing
Using the same `s_txs`, `amount_to_send`, `destination_address`, and `change_address` as the last example, we are going to build a transaction that can be signed offline.
```python
response = node.wallet.build_offline_sign_request(
        fee_amount=fee_amount,
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=x.transaction_id, index=x.index) for x in transactions],
        recipients=[Recipient(destination_address=destination_address, subtraction_fee_from_amount=True, amount=amount_to_send)],
        allow_unconfirmed=False,
        shuffle_outputs=True,
        change_address=change_address
    )
```
Once the offline sign request is built, you'll need to do the next step on your offline device.

Underneath the hood, pystratis uses [pydantic datastructures](https://pydantic-docs.helpmanual.io/). We'll use `pydantic` to help move our data to the offline device for signing.

First, you'll need to serialize the response from the api request (a [BuildOfflineSignModel](https://pystratis.readthedocs.io/en/latest/source/pystratis.api.global_responsemodels.html#pystratis.api.global_responsemodels.buildofflinesignmodel.BuildOfflineSignModel)).
```python
serialized_response = response.json()

# Write the serialized data to a file that can be moved over to the offline device with a thumbdrive.
offline_sign_file = 'offline_sign_model_file'
with open(offline_sign_file, 'w') as f:
    f.write(serialized_response)
```

The next steps assume you are on the offline device (this should be done with swagger or the UI, but including here for completeness).
```python
from pystratis.nodes import StraxNode
from pystratis.api.wallet.responsemodels import BuildOfflineSignModel
import json
offline_node = StraxNode()
with open('offline_sign_model_file', 'r') as f:
    data = json.load(f)
    # Restore the json in to a BuildOfflineSignModel
    offline_sign_model = BuildOfflineSignModel(**data)

response = offline_node.wallet.offline_sign_request(
        wallet_password='password',
        wallet_name='Test',
        wallet_account='account 0',
        unsigned_transaction=offline_sign_model.unsigned_transaction,
        fee=offline_sign_model.fee,
        utxos=offline_sign_model.utxos,
        addresses=offline_sign_model.addresses
    )

# The response of the offline_sign_request is a BuildTransactionModel. 
# We are going to save the hex for importing back to the online computer for broadcasting.
signed_transaction_file = 'signed_transaction_file'
with open(signed_transaction_file, 'w') as f:
    f.write(response.hex)
```

Back on the online node.
```python
from pystratis.core.types import hexstr
with open('signed_transaction_file') as f:
    offline_transaction_hex = hexstr(f.readline())

# Broadcast the successfully built offline transaction
response = node.wallet.send_transaction(transaction_hex=offline_transaction_hex)
```