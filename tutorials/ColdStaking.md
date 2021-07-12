Cold-staking setup with pyStratis
=================================
This tutorial will give an example of setting up cold-staking using pystratis. 

This guide follows [the official cold-staking instructions from the Stratis Academy](https://academy.stratisplatform.com/Operation%20Guides/Cold-Staking/coldstaking-introduction.html).

Disclaimer: __DO NOT__ install pystratis on your cold-staking node. Installing __ANY__ unnecessary software on this device could potentially become an attack vector and defeats the purpose.

## Setting up a hot wallet
### Create an account for coldstaking
This setup assumes you are running a fully synced node with a wallet called 'ExampleWallet'
```python
from pystratis.nodes import StraxNode
strax_hot_node = StraxNode()

# First setup a coldstaking account in your online wallet
hot_account = strax_hot_node.coldstaking.account(
    wallet_name='ExampleWallet',
    wallet_password='abc123',
    is_cold_wallet_account=False
)
```
You will now see an account in your node dashboard: `ExampleWallet/coldStakingHotAddresses`

### Generate an hot staking address for your cold staking wallet
```python
coldstaking_address_model = strax_hot_node.coldstaking.address(
    wallet_name=hot_wallet_name,
    is_cold_wallet_address=False,
    segwit=False
)
coldstaking_hot_address = coldstaking_address_model.address
```
Save the value of `coldstaking_hot_address` as you'll need it to setup on your offline device.

Official documentation recommends keeping a text file with the data on a thumb drive. 

### Setting up and funding your offline wallet 
[Please follow the official documentation to setup your cold wallet on the offline node](https://academy.stratisplatform.com/Operation%20Guides/Cold-Staking/STRAX%20Wallet/Cold-Staking-Guide.html#setting-up-your-cold-wallet).

Things you'll need from this cold wallet (see official documention for details)
- An address to fund (from receive tab). 
  - Send funds to this address (see [sending a transaction](https://github.com/stratisproject/pyStratis/blob/master/tutorials/SendingTransaction.md) tutorial for details on doing this with pystratis)
    - Fund with 10.0002 Strax for this example (enough extra to cover the fee).
- Your coldstaking address. We'll call this `coldstaking_cold_address` for usage below.
- The extended public key of the cold wallet.

### Coldstaking setup on online node
First we need to import the cold wallet's extended public key on the online node.
```python
strax_hot_node.wallet.recover_via_extpubkey(
    extpubkey='<offline_wallet_default_extpubkey>',
    name='<The name for the cold wallet on the online node>',
    account_index=0
)
```
Next, build a template transaction on the online node.
```python
offline_template = strax_hot_node.coldstaking.setup_offline(
    wallet_name='<The name for the cold wallet on the online node>',
    wallet_account='account 0',
    cold_wallet_address=coldstaking_cold_address,
    hot_wallet_address=coldstaking_hot_address,
    amount=Money(10), # The amount you want to cold stake
    fees=Money(0.0002) # The fee. 
)
```
Transfer the value from `offline_template.unsigned_transaction` to your thumb drive for signing on your offline wallet.

See the [official documentation for obtaining the signed transaction hex from the offline wallet](https://academy.stratisplatform.com/Operation%20Guides/Cold-Staking/STRAX%20Wallet/Cold-Staking-Guide.html#setting-up-your-cold-wallet).

### Broadcasting the signed transaction
Bring the thumb drive back to the online node, retrieve the signed transaction hex value from your thumb drive, and send the transaction.
```python
strax_hot_node.wallet.send_transaction('<signed hex transaction from offline node>')
```
__That's it!__

__Note:__ Per official documentation, you will only get rewards if your hot staking node is online and has staking enabled.