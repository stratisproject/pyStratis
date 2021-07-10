# pystratis
Python package for interacting with Stratis (STRAX) full node and Cirrus/Interflux sidechain.

## Installation
### From the Python Package Index (PyPi)
`pip install pystratis`

### Most recent (from GitHub)
`pip install git+https://github.com/stratisproject/pystratis.git`

### Install from PyPi with test dependencies
`pip install pystratis[test]`

## Basic model examples

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

### Working with smart contracts

```python
from pystratis.nodes import CirrusNode
from pystratis.core.types import Money

# The smart contracts are available on Cirrus sidechain.
node = CirrusNode()

# Bytecode of our smart contract. 
# Learn how to create and build smart contracts.
# https://smartcontractsdocs.stratisplatform.com/Architecture%20Reference/SmartContracts/working-with-contracts.html#writing-a-contract.
contract_code = 'code = '4D5A90000300000004000000FFFF0000B800000000000000400000000000000000000000000000000000000000000000000000000000000000000000800000000E1FBA0E00B409CD21B8014CCD21546869732070726F6772616D2063616E6E6F742062652072756E20696E20444F53206D6F64652E0D0D0A2400000000000000504500004C0102003875F3B70000000000000000E00022200B013000000400000002000000000000C2230000002000000040000000000010002000000002000004000000000000000400000000000000006000000002000000000000030040850000100000100000000010000010000000000000100000000000000000000000702300004F000000000000000000000000000000000000000000000000000000004000000C000000542300001C0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200000080000000000000000000000082000004800000000000000000000002E74657874000000C8030000002000000004000000020000000000000000000000000000200000602E72656C6F6300000C000000004000000002000000060000000000000000000000000000400000420000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000A42300000000000048000000020005005C200000F80200000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000220203280400000A2A00000042534A4201000100000000000C00000076342E302E33303331390000000005006C00000004010000237E0000700100002401000023537472696E67730000000094020000040000002355530098020000100000002347554944000000A80200005000000023426C6F620000000000000002000001471500000900000000FA01330016000001000000060000000200000001000000010000000400000003000000010000000200000000009A0001000000000006005C00C50006007C00C50006004800B2000F00E50000000A000B01F4000A002100F400000000000100000000000100010001001000190100001500010001005020000000008618AC00100001000000010035000900AC0001001100AC0006001900AC000A002900AC0010002E000B001F002E00130028002E001B0047000480000000000000000000000000000000000B01000004000000000000000000000016000A00000000000200000000000000000000000000F400000000000000003C4D6F64756C653E0053797374656D2E507269766174652E436F72654C69620049536D617274436F6E7472616374537461746500736D617274436F6E747261637453746174650044656275676761626C6541747472696275746500436F6D70696C6174696F6E52656C61786174696F6E734174747269627574650052756E74696D65436F6D7061746962696C69747941747472696275746500536D617274436F6E74726163742E646C6C002E63746F720053797374656D2E446961676E6F73746963730053797374656D2E52756E74696D652E436F6D70696C6572536572766963657300446562756767696E674D6F64657300537472617469732E536D617274436F6E74726163747300536D617274436F6E7472616374004D79436F6E747261637400000000000424F499BA6DB24C99CB869055EC080400042001010803200001052001011111052001011219087CEC85D7BEA7798E0801000800000000001E01000100540216577261704E6F6E457863657074696F6E5468726F77730108010002000000000000000000000000000000000010000000000000000000000000000000982300000000000000000000B2230000002000000000000000000000000000000000000000000000A4230000000000000000000000005F436F72446C6C4D61696E006D73636F7265652E646C6C0000000000FF25002000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002000000C000000C43300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

# An example address of smart contract sender.
my_address = node.wallet.addresses(wallet_name='mywallet').addresses[0].address


# Learn more about gas pricing.
# https://academy.stratisplatform.com/Architecture%20Reference/SmartContracts/appendix-gas-prices.html#gas-pricing
build_transaction = node.smart_contracts.build_create(
    wallet_name='mywallet',
    password='qwerty12345', 
    fee_amount=Money(0.001), 
    contract_code=contract_code,
    gas_price=100, # recommended value
    gas_limit=50000, # recommended value
    sender=my_address,
    amount=Money(0.1)
)

# Now we can test a smart contract's functionality locally without risk of losing any real money.
# If you are looking for a way to test smart contract in fully controlled environment, 
# check out the documentatiom on TestChain.
# https://smartcontractsdocs.stratisplatform.com/Architecture%20Reference/SmartContracts/testing-locally-with-testchain.html
node.smart_contracts.local_call(
    contract_address=build_transaction.new_contract_address, 
    method_name='FooBar',
    amount=Money(0.1),
    gas_price=100,
    gas_limit=50000,
    sender=my_address
)

# When we ready to deploy a smart contract, we send raw bytes of transaction we built.
# If you don't need to test your smart contract with `local_call`, 
# you can just use `node.smart_contract_wallet.create` method to create and deploy your smart contract.
node.smart_contract_wallet.send_transaction(build_transaction.hex)


# Now we can call any methods of the deployed smart contract.
node.smart_contract_wallet.call(
    wallet_name='mywallet', 
    password='qwerty12345', 
    contract_address=build_transaction.new_contract_address,
    method_name='FooBar',
    parameters=['arg1', 'arg2'], # you can pass arguments to a smart contract's method call
    fee_amount=Money(0.001), 
    gas_price=100,
    gas_limit=50000,
    sender=my_address,
    amount=Money(0.1)
)
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
