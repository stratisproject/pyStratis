import pytest
from random import choice
from pybitcoin.types import uint256


def test_uint256(generate_uint256):
    trx_hash = generate_uint256
    block_hash = generate_uint256

    assert uint256(trx_hash).to_hex() == trx_hash
    assert uint256(block_hash).to_hex() == block_hash


def test_uint256_invalid_hexstring():
    letters = 'qwerty0'
    badvalue = ''.join(choice(letters) for _ in range(64))
    with pytest.raises(ValueError):
        uint256(badvalue)


def test_uint256_too_long():
    letters = '0123456789abcdef'
    badvalue = ''.join(choice(letters) for _ in range(128))
    with pytest.raises(ValueError):
        uint256(badvalue)


def test_uint256_too_short():
    letters = '0123456789abcdef'
    badvalue = ''.join(choice(letters) for _ in range(32))
    with pytest.raises(ValueError):
        uint256(badvalue)


def test_uint256_try_init_nonstr(generate_uint256):
    with pytest.raises(ValueError):
        uint256(1.5)
    with pytest.raises(ValueError):
        uint256(True)
    with pytest.raises(ValueError):
        uint256([generate_uint256])
    with pytest.raises(ValueError):
        uint256({'hash': generate_uint256})
    with pytest.raises(ValueError):
        uint256(bytes(generate_uint256, 'utf-8'))


def test_uint256_add():
    a = uint256(2)
    b = uint256(5)
    assert a + b == uint256(7)
    a += b
    assert a == uint256(7)


def test_uint256_sub():
    a = uint256(9)
    b = uint256(5)
    assert a - b == uint256(4)
    a -= b
    assert a == uint256(4)


def test_uint256_mul():
    a = uint256(2)
    b = uint256(5)
    assert a * b == uint256(2*5)
    a *= b
    assert a == uint256(2*5)


def test_uint256_floordiv():
    a = uint256(20)
    b = uint256(5)
    assert a // b == uint256(20 // 5)
    a //= b
    assert a == uint256(20 // 5)


def test_uint256_pow():
    a = uint256(20)
    b = 5
    assert a ** b == uint256(20 ** 5)
    a //= b
    assert a == uint256(20 // 5)


def test_uint256_test_underflow():
    a = uint256(2)
    b = uint256(5)
    with pytest.raises(ValueError):
        a - b
    with pytest.raises(ValueError):
        uint256(-1)


def test_uint256_test_overflow():
    numbits = 256
    with pytest.raises(ValueError):
        uint256(2**numbits)
    with pytest.raises(ValueError):
        uint256(2**numbits-1) + uint256(1)
    with pytest.raises(ValueError):
        uint256(2**numbits) * uint256(2)
