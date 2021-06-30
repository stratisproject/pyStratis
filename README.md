# pystratis
Python package for interacting with Stratis (STRAX) full node and Cirrus/Interflux sidechain.

## Basic models example

### Private key

```python
from pyStratis import Key

private_key = Key('5HwoXVkHoRM8sL2KmNRS217n1g8mPPBomrY7yehCuXC1115WWsh')
same_private_key = Key(private_key.get_bytes())

assert private_key == same_private_key
assert private_key.generate_wif_key() == same_private_key.generate_wif_key()
assert str(private_key_from_str) == str(private_key_from_bytes)
```

### Public key

```python
from pyStratis import PubKey

pubkey_compressed = PubKey('034f355bdcb7cc0af728ef3cceb9615d90684bb5b2ca5f859ab0f0b704075871aa')
pubkey_uncompressed = PubKey(pubkey_compressed.uncompressed())

assert pubkey_compressed.x == pubkey_uncompressed.x
assert pubkey_compressed.y == pubkey_uncompressed.y
```

### Extended private key

```python
from pyStratis import ExtKey

extended_private_key = ExtKey('4Qzpnt5o8msy6thbuFEHTr4yFqp8yvywYBhrtHLJNKEHDhidjbCVvdjuXA2V9k6Bg39FJjfbqpasUmnNYBfZZY27')
another_extended_private_key = ExtKey(extended_private_key.get_bytes())

assert extended_private_key.generate_private_key_bytes() == another_extended_private_key.generate_private_key_bytes()
assert extended_private_key.generate_chain_code_bytes() == another_extended_private_key.generate_chain_code_bytes()
```

### Extended public key

```python
from pyStratis import ExtPubKey

extended_public_key = ExtPubKey('6FHa3pjLCk84BayeJxFW2SP4XRrFd1JYnxeLeU8EqN3vDfZmbqBqaGJAyiLjTAwm6ZLRQUMv1ZACTj37sR62cfN7fe5JnJ7dh8zL4fiyLHV')
another_extended_public_key = ExtPubKey(str(extended_public_key))

assert extended_public_key == another_extended_public_key
```

## Testing guide

- Unit tests: `pytest -m "not integration_test"`
- Strax integration tests: `pytest -m "strax_integration_test"`
- Cirrus integration tests: `pytest -m "cirrus_integration_test"`
- Interflux integration tests: `pytest -m "interflux_integration_test"`
- Integration tests: `pytest -m "integration_test"`
- Everything: `pytest`
- Coverage: `coverage run -m pytest`
- Coverage report: `coverage report -m`

# Credit

Thanks goes to [@TjadenFroyda](https://github.com/tjadenfroyda) for his contributions in kickstarting this repositoriy.
