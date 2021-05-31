import pytest
from random import choice
from pybitcoin.types import int32


def test_int32(generate_int32):
    trx_hash = generate_int32
    block_hash = generate_int32

    assert int32(trx_hash).to_hex() == trx_hash
    assert int32(block_hash).to_hex() == block_hash


def test_int32_invalid_hexstring():
    letters = 'qwerty0'
    badvalue = ''.join(choice(letters) for _ in range(64))
    with pytest.raises(ValueError):
        int32(badvalue)


def test_int32_long_hex_overflow():
    letters = '0123456789abcdef'
    long_value = ''.join(choice(letters) for _ in range(128))
    with pytest.raises(ValueError):
        int32(long_value)


def test_int32_short_hex_ok():
    letters = '0123456789abcdef'
    short_value = ''.join(choice(letters) for _ in range(6))
    assert short_value in int32(short_value).to_hex()


def test_int32_try_init_nonstr(generate_int32):
    with pytest.raises(ValueError):
        int32(1.5)
    with pytest.raises(ValueError):
        int32(True)
    with pytest.raises(ValueError):
        int32([generate_int32])
    with pytest.raises(ValueError):
        int32({'hash': generate_int32})
    with pytest.raises(ValueError):
        int32(bytes(generate_int32, 'utf-8'))


def test_int32_add():
    a = int32(2)
    b = int32(5)
    assert a + b == int32(7)
    a += b
    assert a == int32(7)


def test_int32_sub():
    a = int32(9)
    b = int32(5)
    assert a - b == int32(4)
    a -= b
    assert a == int32(4)


def test_int32_mul():
    a = int32(2)
    b = int32(5)
    assert a * b == int32(2*5)
    a *= b
    assert a == int32(2*5)


def test_int32_floordiv():
    a = int32(20)
    b = int32(5)
    assert a // b == int32(20 // 5)
    a //= b
    assert a == int32(20 // 5)


def test_int32_pow():
    a = int32(20)
    b = 5
    assert a ** b == int32(20 ** 5)
    a //= b
    assert a == int32(20 // 5)


def test_int32_test_underflow():
    numbits = 32
    a = int32(2**numbits // -2)
    b = int32(5)
    with pytest.raises(ValueError):
        a - b
    with pytest.raises(ValueError):
        int32(2**numbits // -2 - 1)


def test_int32_test_overflow():
    numbits = 32
    with pytest.raises(ValueError):
        int32(2**numbits)
    with pytest.raises(ValueError):
        int32(2**numbits-1) + int32(1)
    with pytest.raises(ValueError):
        int32(2**numbits) * int32(2)
