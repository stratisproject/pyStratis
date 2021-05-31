import pytest
from random import choice
from pybitcoin.types import uint128


def test_uint128(generate_uint128):
    trx_hash = generate_uint128
    block_hash = generate_uint128

    assert uint128(trx_hash).to_hex() == trx_hash
    assert uint128(block_hash).to_hex() == block_hash


def test_uint128_invalid_hexstring():
    letters = 'qwerty0'
    badvalue = ''.join(choice(letters) for _ in range(64))
    with pytest.raises(ValueError):
        uint128(badvalue)


def test_uint128_long_hex_overflow():
    letters = '0123456789abcdef'
    long_value = ''.join(choice(letters) for _ in range(128))
    with pytest.raises(ValueError):
        uint128(long_value)


def test_uint128_short_hex_ok():
    first_digit = '01234567'
    letters = '0123456789abcdef'
    short_value = choice(first_digit) + ''.join(choice(letters) for _ in range(16))
    assert short_value in uint128(short_value).to_hex()


def test_uint128_try_init_nonstr(generate_uint128):
    with pytest.raises(ValueError):
        uint128(1.5)
    with pytest.raises(ValueError):
        uint128(True)
    with pytest.raises(ValueError):
        uint128([generate_uint128])
    with pytest.raises(ValueError):
        uint128({'hash': generate_uint128})
    with pytest.raises(ValueError):
        uint128(bytes(generate_uint128, 'utf-8'))


def test_uint128_add():
    a = uint128(2)
    b = uint128(5)
    assert a + b == uint128(7)
    a += b
    assert a == uint128(7)


def test_uint128_sub():
    a = uint128(9)
    b = uint128(5)
    assert a - b == uint128(4)
    a -= b
    assert a == uint128(4)


def test_uint128_mul():
    a = uint128(2)
    b = uint128(5)
    assert a * b == uint128(2*5)
    a *= b
    assert a == uint128(2*5)


def test_uint128_floordiv():
    a = uint128(20)
    b = uint128(5)
    assert a // b == uint128(20 // 5)
    a //= b
    assert a == uint128(20 // 5)


def test_uint128_pow():
    a = uint128(20)
    b = 5
    assert a ** b == uint128(20 ** 5)
    a //= b
    assert a == uint128(20 // 5)


def test_uint128_test_underflow():
    a = uint128(2)
    b = uint128(5)
    with pytest.raises(ValueError):
        a - b
    with pytest.raises(ValueError):
        uint128(-1)


def test_uint128_test_overflow():
    numbits = 128
    with pytest.raises(ValueError):
        uint128(2**numbits)
    with pytest.raises(ValueError):
        uint128(2**numbits-1) + uint128(1)
    with pytest.raises(ValueError):
        uint128(2**numbits) * uint128(2)
