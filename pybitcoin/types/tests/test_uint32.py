import pytest
from random import choice
from pybitcoin.types import uint32


def test_uint32(generate_uint32):
    trx_hash = generate_uint32
    block_hash = generate_uint32

    assert uint32(trx_hash).to_hex() == trx_hash
    assert uint32(block_hash).to_hex() == block_hash


def test_uint32_invalid_hexstring():
    letters = 'qwerty0'
    badvalue = ''.join(choice(letters) for _ in range(64))
    with pytest.raises(ValueError):
        uint32(badvalue)


def test_uint32_long_hex_overflow():
    letters = '0123456789abcdef'
    long_value = ''.join(choice(letters) for _ in range(128))
    with pytest.raises(ValueError):
        uint32(long_value)


def test_uint32_short_hex_ok():
    first_digit = '01234567'
    letters = '0123456789abcdef'
    short_value = choice(first_digit) + ''.join(choice(letters) for _ in range(6))
    assert short_value in uint32(short_value).to_hex()


def test_uint32_try_init_nonstr(generate_uint32):
    with pytest.raises(ValueError):
        uint32(1.5)
    with pytest.raises(ValueError):
        uint32(True)
    with pytest.raises(ValueError):
        uint32([generate_uint32])
    with pytest.raises(ValueError):
        uint32({'hash': generate_uint32})
    with pytest.raises(ValueError):
        uint32(bytes(generate_uint32, 'utf-8'))


def test_uint32_add():
    a = uint32(2)
    b = uint32(5)
    assert a + b == uint32(7)
    a += b
    assert a == uint32(7)


def test_uint32_sub():
    a = uint32(9)
    b = uint32(5)
    assert a - b == uint32(4)
    a -= b
    assert a == uint32(4)


def test_uint32_mul():
    a = uint32(2)
    b = uint32(5)
    assert a * b == uint32(2*5)
    a *= b
    assert a == uint32(2*5)


def test_uint32_floordiv():
    a = uint32(20)
    b = uint32(5)
    assert a // b == uint32(20 // 5)
    a //= b
    assert a == uint32(20 // 5)


def test_uint32_pow():
    a = uint32(20)
    b = 5
    assert a ** b == uint32(20 ** 5)
    a //= b
    assert a == uint32(20 // 5)


def test_uint32_test_underflow():
    a = uint32(2)
    b = uint32(5)
    with pytest.raises(ValueError):
        a - b
    with pytest.raises(ValueError):
        uint32(-1)


def test_uint32_test_overflow():
    numbits = 32
    with pytest.raises(ValueError):
        uint32(2**numbits)
    with pytest.raises(ValueError):
        uint32(2**numbits-1) + uint32(1)
    with pytest.raises(ValueError):
        uint32(2**numbits) * uint32(2)
