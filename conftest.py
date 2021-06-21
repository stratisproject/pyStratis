import pytest
import hashlib
import mnemonic
import secrets
import os
import json
from hashlib import sha256
import hmac
import base58
import bech32
import ecdsa
from binascii import unhexlify
from random import choice, randint, random
# noinspection PyPackageRequirements
from sha3 import keccak_256
from pybitcoin import Key, ExtKey
from pybitcoin.types import uint256
from pybitcoin.networks import BaseNetwork
from datetime import datetime, timedelta


@pytest.fixture(scope='session')
def fakeuri():
    return 'http://localhost:8888'


@pytest.fixture(scope='session')
def get_datetime():
    def _get_datetime(days_back: int = 365) -> str:
        return (datetime.now() - timedelta(days=days_back)).isoformat().split('.')[0]
    return _get_datetime


@pytest.fixture(scope='session')
def generate_p2pkh_address():
    # noinspection PyUnresolvedReferences
    def _generate_p2pkh_address(network: 'BaseNetwork') -> str:
        private_key = secrets.token_bytes(20)
        payload_bytes = network.PUBKEY_ADDRESS + private_key
        checksum = sha256(sha256(payload_bytes).digest()).digest()
        return base58.b58encode(payload_bytes + checksum[:4]).decode('ascii')
    return _generate_p2pkh_address


@pytest.fixture(scope='session')
def generate_p2sh_address():
    # noinspection PyUnresolvedReferences
    def _generate_p2sh_address(network: 'BaseNetwork') -> str:
        private_key = secrets.token_bytes(20)
        payload_bytes = network.SCRIPT_ADDRESS + private_key
        checksum = sha256(sha256(payload_bytes).digest()).digest()
        return base58.b58encode(payload_bytes + checksum[:4]).decode('ascii')
    return _generate_p2sh_address


@pytest.fixture(scope='session')
def generate_p2wpkh_address():
    # noinspection PyUnresolvedReferences
    def _generate_p2wpkh_address(network: 'BaseNetwork') -> str:
        witprog = secrets.token_bytes(20)
        witver = 0
        return bech32.encode(hrp=network.BECH32_HRP, witver=witver, witprog=witprog)
    return _generate_p2wpkh_address


@pytest.fixture(scope='session')
def generate_p2wsh_address():
    # noinspection PyUnresolvedReferences
    def _generate_p2wsh_address(network: 'BaseNetwork') -> str:
        witprog = secrets.token_bytes(32)
        witver = 0
        return bech32.encode(hrp=network.BECH32_HRP, witver=witver, witprog=witprog)
    return _generate_p2wsh_address


@pytest.fixture(scope='session')
def get_base_keypath() -> str:
    return "m/44'/105'/0'/0/0"


@pytest.fixture(scope='session')
def generate_ethereum_lower_address() -> str:
    return generate_ethereum_address()


@pytest.fixture(scope='session')
def generate_ethereum_upper_address() -> str:
    return f'0x{generate_ethereum_address()[2:].upper()}'


@pytest.fixture(scope='session')
def generate_ethereum_checksum_address() -> str:
    address = generate_ethereum_address()
    address_hash = keccak_256(
        address.replace('0x', '').encode('ascii')
    ).hexdigest()
    checksum_address = ''
    for i, ch in enumerate(address.replace('0x', '')):
        if int(address_hash[i], 16) >= 8:
            checksum_address += ch.upper()
        else:
            checksum_address += ch
    return f'0x{checksum_address}'


@pytest.fixture(scope='session')
def generate_uint256() -> str:
    first_digit = '01234567'
    hex_letters = '0123456789abcdef'
    sign_char = choice(first_digit)
    return f"{sign_char}{''.join(choice(hex_letters) for _ in range(63))}"


@pytest.fixture(scope='session')
def generate_uint128() -> str:
    first_digit = '01234567'
    hex_letters = '0123456789abcdef'
    sign_char = choice(first_digit)
    return f"{sign_char}{''.join(choice(hex_letters) for _ in range(31))}"


@pytest.fixture(scope='session')
def generate_uint64() -> str:
    first_digit = '01234567'
    hex_letters = '0123456789abcdef'
    sign_char = choice(first_digit)
    return f"{sign_char}{''.join(choice(hex_letters) for _ in range(15))}"


@pytest.fixture(scope='session')
def generate_uint32() -> str:
    first_digit = '01234567'
    hex_letters = '0123456789abcdef'
    sign_char = choice(first_digit)
    return f"{sign_char}{''.join(choice(hex_letters) for _ in range(7))}"


@pytest.fixture(scope='session')
def generate_int64() -> str:
    hex_letters = '0123456789abcdef'
    return ''.join(choice(hex_letters) for _ in range(16))


@pytest.fixture(scope='session')
def generate_int32() -> str:
    hex_letters = '0123456789abcdef'
    return ''.join(choice(hex_letters) for _ in range(8))


@pytest.fixture(scope='session')
def generate_uint160() -> str:
    first_digit = '01234567'
    hex_letters = '0123456789abcdef'
    sign_char = choice(first_digit)
    return f"{sign_char}{''.join(choice(hex_letters) for _ in range(39))}"


@pytest.fixture(scope='session')
def generate_hexstring():
    def _generate_hexstring(length: int = 128) -> str:
        letters = '0123456789abcdef'
        return ''.join(choice(letters) for _ in range(length))
    return _generate_hexstring


@pytest.fixture(scope='session')
def generate_privatekey():
    def _generate_privatekey(words: str = None) -> Key:
        hashkey = b'Bitcoin seed'
        mnemo = mnemonic.Mnemonic(language='english')
        if words is None:
            words = mnemo.generate()
        seed = mnemo.to_seed(words)
        # noinspection PyTypeChecker
        extkey = ExtKey(hmac.digest(hashkey, seed, hashlib.sha512))
        return extkey.generate_private_key()
    return _generate_privatekey


@pytest.fixture(scope='session')
def generate_wif_privatekey(generate_privatekey) -> str:
    return generate_privatekey().generate_wif_key()


@pytest.fixture(scope='session')
def generate_uncompressed_pubkey(generate_privatekey) -> str:
    key = ecdsa.SigningKey.from_string(generate_privatekey().get_bytes(), curve=ecdsa.SECP256k1).verifying_key
    key_int = int.from_bytes(key.to_string(), 'big')
    return f"04{format(key_int, '0>128x')}"


@pytest.fixture(scope='session')
def generate_compressed_pubkey(generate_uncompressed_pubkey) -> str:
    uncompressed_pubkey = generate_uncompressed_pubkey[2:]
    uncompressed_pubkey_bytes = unhexlify(uncompressed_pubkey)
    x = int.from_bytes(uncompressed_pubkey_bytes[:32], 'big')
    prefix = '02' if x % 2 == 0 else '03'
    return f"{prefix}{format(x, '0>64x')}"


@pytest.fixture(scope='session')
def generate_extpubkey() -> str:
    version = unhexlify('0488b21e')
    depth = secrets.token_bytes(1)
    parent_fingerprint = secrets.token_bytes(4)
    index = secrets.token_bytes(4)
    chain_code = secrets.token_bytes(32)
    key = secrets.token_bytes(33)
    payload_bytes = version + depth + parent_fingerprint + index + chain_code + key
    checksum = sha256(sha256(payload_bytes).digest()).digest()
    return base58.b58encode(payload_bytes + checksum[:4]).decode('ascii')


@pytest.fixture(scope='session')
def generate_extprvkey() -> str:
    version = unhexlify('0488ade4')
    depth = secrets.token_bytes(1)
    parent_fingerprint = secrets.token_bytes(4)
    index = secrets.token_bytes(4)
    chain_code = secrets.token_bytes(32)
    key = secrets.token_bytes(33)
    payload_bytes = version + depth + parent_fingerprint + index + chain_code + key
    checksum = sha256(sha256(payload_bytes).digest()).digest()
    return base58.b58encode(payload_bytes + checksum[:4]).decode('ascii')


@pytest.fixture(scope='session')
def strax_swagger_json() -> dict:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(root_dir, 'api', 'strax-swagger.json')
    with open(file_path, 'r') as f:
        return json.load(f)


@pytest.fixture(scope='session')
def cirrus_swagger_json() -> dict:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(root_dir, 'api', 'cirrus-swagger.json')
    with open(file_path, 'r') as f:
        return json.load(f)


@pytest.fixture(scope='session')
def interfluxstrax_swagger_json() -> dict:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(root_dir, 'api', 'interfluxstrax-swagger.json')
    with open(file_path, 'r') as f:
        return json.load(f)


@pytest.fixture(scope='session')
def interfluxcirrus_swagger_json() -> dict:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(root_dir, 'api', 'interfluxcirrus-swagger.json')
    with open(file_path, 'r') as f:
        return json.load(f)


def generate_ethereum_address() -> str:
    privatekey = keccak_256(secrets.token_bytes(32)).digest()
    privatekey = ecdsa.SigningKey.from_string(privatekey, curve=ecdsa.SECP256k1)
    publickey = privatekey.get_verifying_key().to_string()
    address = keccak_256(publickey).hexdigest()[24:]
    return f'0x{address}'


@pytest.fixture(scope='session')
def generate_block_no_tx_data(generate_hexstring, generate_uint256) -> dict:
    data = {
        "hash": generate_hexstring(128),
        "confirmations": randint(0, 200),
        "size": randint(0, 200),
        "weight": randint(0, 200),
        "height": randint(0, 200),
        "version": randint(0, 200),
        "versionHex": generate_hexstring(8),
        "merkleroot": generate_uint256,
        "tx": [
            generate_uint256,
            generate_uint256,
            generate_uint256
        ],
        "time": 1600000000,
        "mediantime": 1600000005,
        "nonce": 0,
        "bits": generate_hexstring(8),
        "difficulty": random()*1e6,
        "chainwork": generate_uint256,
        "nTx": 3,
        "previousblockhash": generate_uint256,
        "nextblockhash": generate_uint256,
        "signature": generate_hexstring(128),
        "modifierv2": generate_hexstring(64),
        "flags": "proof-of-stake",
        "hashproof": generate_hexstring(64),
        "blocktrust": generate_hexstring(64),
        "chaintrust": generate_hexstring(64)
    }
    return data


@pytest.fixture(scope='session')
def generate_coinbase_transaction(generate_hexstring, generate_uint256):
    def _generate_transaction(trxid: uint256) -> dict:
        data = {
            "hex": generate_hexstring(128),
            "txid": trxid,
            "hash": trxid,
            "version": 1,
            "size": randint(0, 200),
            "vsize": randint(0, 200),
            "weight": randint(0, 200),
            "locktime": 0,
            "vin": [
                {
                    "coinbase": generate_hexstring(10),
                    "sequence": 4294967295
                }
            ],
            "vout": [
                {
                    "value": 0,
                    "n": 0,
                    "scriptPubKey": {
                        "asm": "",
                        "hex": "",
                        "type": "nonstandard"
                    }
                },
                {
                    "value": 0,
                    "n": 1,
                    "scriptPubKey": {
                        "asm": f"OP_RETURN {generate_hexstring(64)}",
                        "hex": generate_hexstring(64),
                        "type": "nulldata"
                    }
                }
            ]
        }
        return data
    return _generate_transaction


@pytest.fixture(scope='session')
def generate_transaction(generate_hexstring, generate_uint256, generate_p2pkh_address, generate_p2sh_address):
    def _generate_transaction(trxid: uint256, network: BaseNetwork) -> dict:
        data = {
            "hex": generate_hexstring(128),
            "txid": trxid,
            "hash": trxid,
            "version": 1,
            "size": randint(0, 200),
            "vsize": randint(0, 200),
            "weight": randint(0, 200),
            "locktime": 0,
            "vin": [
                {
                    "txid": generate_uint256,
                    "vout": 1,
                    "scriptSig": {
                        "asm": generate_hexstring(128),
                        "hex": generate_hexstring(128)
                    },
                    "sequence": 4294967295
                }
            ],
            "vout": [
                {
                    "value": 0,
                    "n": 0,
                    "scriptPubKey": {
                        "asm": "",
                        "hex": "",
                        "type": "nonstandard"
                    }
                },
                {
                    "value": random()*1e3,
                    "n": 1,
                    "scriptPubKey": {
                        "asm": f"generate_hexstring(64) OP_CHECKSIG",
                        "hex": generate_hexstring(128),
                        "reqSigs": 1,
                        "type": "pubkey",
                        "addresses": [
                            generate_p2pkh_address(network=network)
                        ]
                    }
                },
                {
                    "value": 9.0,
                    "n": 2,
                    "scriptPubKey": {
                        "asm": f"OP_HASH160 generate_hexstring(42) OP_EQUAL",
                        "hex": "generate_hexstring(42)",
                        "reqSigs": 1,
                        "type": "scripthash",
                        "addresses": [
                            generate_p2sh_address(network=network)
                        ]
                    }
                }
            ]
        }
        return data
    return _generate_transaction


@pytest.fixture(scope='session')
def generate_block_with_tx_data(generate_block_no_tx_data, generate_coinbase_transaction, generate_transaction):
    def _generate_block_with_tx_data(network: BaseNetwork) -> dict:
        data = generate_block_no_tx_data
        data['transactions'] = [
            generate_coinbase_transaction(trxid=data['tx'][0]),
            generate_transaction(trxid=data['tx'][1], network=network),
            generate_transaction(trxid=data['tx'][2], network=network),
        ]
        return data
    return _generate_block_with_tx_data


@pytest.fixture(scope='session')
def get_federation_private_key(generate_privatekey):
    def _get_federation_private_key(index: int = 0) -> bytes:
        mnemonics = [
            'ensure feel swift crucial bridge charge cloud tell hobby twenty people mandate',
            'quiz sunset vote alley draw turkey hill scrap lumber game differ fiction',
            'fat chalk grant major hair possible adjust talent magnet lobster retreat siren'
        ]
        assert index < len(mnemonics)
        return generate_privatekey(mnemonics[index]).get_bytes()
    return _get_federation_private_key
