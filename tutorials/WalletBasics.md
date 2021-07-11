Wallet Basics with Pystratis
============================
The Strax/Cirrus wallet is a full-featured HD wallet. This tutorial will cover some basics for setting up a new wallet on a StratisFullNode using pystratis.

Note: The same wallet will be used in all of the examples. The tutorial on [sending transactions can be found here.](https://github.com/stratisproject/pyStratis/blob/master/tutorials/SendingTransaction.md)

## Creating a wallet
```python
from pystratis.nodes import StraxNode
from typing import List

node = StraxNode()
# Returns the mnemonic representing the HD wallet seed.
mnemonic: List[str] = node.wallet.create(name='ExampleWallet', password='abc123')
```
## Loading a wallet
```python
# Loads a known wallet from the data dir with the given name and decrypts the wallet.
node.wallet.load(name='ExampleWallet', password='abc123')
```
## Recovering a wallet
```python
node.wallet.recover(mnemonic=mnemonic, password='abc123', name='RecoveredWallet')
```
## Listing wallets
```python
wallets: dict = node.wallet.list_wallets()
```
## Creating an account
```python
account_name = node.wallet.account(wallet_name='ExampleWallet', password='abc123')
```
## Listing wallet accounts
```python
node.wallet.accounts(wallet_name='ExampleWallet')
```
## Getting an unused address
```python
unused_address = node.wallet.unused_address(wallet_name='ExampleWallet')
```
## Getting all addresses
```python
addresses = node.wallet.addresses(wallet_name='ExampleWallet')
```
## Getting general information about a wallet
```python
node.wallet.general_info(name='ExampleWallet')
```
## Getting a wallet history
```python
history = node.wallet.history(wallet_name='ExampleWallet')
```
## Resyncing wallet
```python
node.wallet.remove_transactions(
    wallet_name='ExampleWallet',
    remove_all=True, 
    resync=True
)
```
## Getting the balance of a wallet
```python
wallet_balance = node.wallet.balance(
    wallet_name='ExampleWallet', 
    include_balance_by_address=False
)
```
## Getting the balance of a specific wallet address
Note: The wallet does not track value in non-owned addresses. If you need to check the balance of a specific address on the blockchain:
- Ensure `addressindex=1` in node configuration.
- Use `blockstore.get_addresses_balances` or `blockstore.get_verbose_addresses_balances` API method.
```python
wallet_balance = node.wallet.balance(
    wallet_name='ExampleWallet', 
    include_balance_by_address=True
)
```
## Signing and verifying a message
```python
signature = node.wallet.sign_message(
    wallet_name='ExampleWallet', 
    password='abc123', 
    external_address=unused_address,
    message='Blockchain made easy.'
)
assert node.wallet.verify_message(
    signature=signature,
    external_address=unused_address,
    message='Blockchain made easy.'
)
```
