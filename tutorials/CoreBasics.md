pyStratis.core Basics
=====================
pystratis.core provides basic key functionality common among cryptocurrency platforms. 

### Private key
```python
from pystratis.core import Key

private_key_from_str = Key('5HwoXVkHoRM8sL2KmNRS217n1g8mPPBomrY7yehCuXC1115WWsh')
same_private_key_from_bytes = Key(private_key_from_str.get_bytes())

assert private_key_from_str == same_private_key_from_bytes
assert private_key_from_str.generate_wif_key() == same_private_key_from_bytes.generate_wif_key()
assert str(private_key_from_str) == str(same_private_key_from_bytes)
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

## pystratis.core.types
C# integer representations do not exist in Python. pystratis.core.types defines several types to facilitate compatibility with the C# StratisFullNode while ensuring overflow protection.

[pystratis.core.types](https://pystratis.readthedocs.io/en/latest/source/pystratis.core.types.html) include:
- int32, uint32
- int64, uint64
- uint128, uint160, uint256

### Money 
[Money](https://pystratis.readthedocs.io/en/latest/source/pystratis.core.types.html) is represented in pystratis as a custom type and stored under the hood as a decimal.Decimal value in Coin units. 

The classmethod `Money.from_satoshi_units()` handles conversion from satoshi units to Coin units.

Instance method `to_coin_unit()` represents the Money as a string with 8 decimal places.
```python
from pystratis.core.types import Money
my_money_float = Money(1.0)
my_money_str = Money('1.0')
assert my_money_float == my_money_str
assert my_money_float.to_coin_unit() == my_money_str.to_coin_unit()
```
### Address
Misspelling an address is a common cause of lost funds across cryptocurrency networks. 

The `Address` type was created to prevent this error by validating the string representation of the address using the provided network. 

`Address` can validate p2pkh, p2sh, p2wpkh, and p2wsh addresses on Strax and Cirrus networks.

Networks supported:
- StraxMain, StraxTest, StraxRegTest
- CirrusMain, CirrusTest, CirrusRegTest
- Ethereum

More networks will be supported as interoperability functionality is added to the full node.
```python
from pystratis.core.types import Address
from pystratis.core.networks import StraxMain, Ethereum
# The Strax multisig address
multisig_address_str = 'yU2jNwiac7XF8rQvSk2bgibmwsNLkkhsHV'
multisig_address = Address(address=multisig_address_str, network=StraxMain())
assert str(multisig_address) == multisig_address_str

vitalik_public_address_str = '0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B'
vitalik_public_address = Address(address=vitalik_public_address_str, network=Ethereum())
assert str(vitalik_public_address) == vitalik_public_address_str
```
### hexstr
The `hexstr` type is a string subclass that restricts inputs to the `0123456789abcdef` hexadecimal charset.
```python
from pystratis.core.types import hexstr
hex_value = hexstr('abc123')
```