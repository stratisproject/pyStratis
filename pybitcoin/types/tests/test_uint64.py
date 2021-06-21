import pytest
from random import choice
from pybitcoin.types import *


def test_uint64(generate_uint64):
    hex_int = generate_uint64
    uint64(hex_int)


def test_uint64_invalid_hexstring():
    letters = 'qwerty0'
    badvalue = ''.join(choice(letters) for _ in range(64))
    with pytest.raises(ValueError):
        uint64(badvalue)


def test_uint64_long_hex_overflow():
    letters = '0123456789abcdef'
    long_value = ''.join(choice(letters) for _ in range(128))
    with pytest.raises(ValueError):
        uint64(long_value)


def test_uint64_short_hex_ok():
    first_digit = '01234567'
    letters = '0123456789abcdef'
    short_value = choice(first_digit) + ''.join(choice(letters) for _ in range(7))
    assert short_value in uint64(short_value).to_hex()


def test_uint64_try_init_nonstr(generate_uint64):
    with pytest.raises(ValueError):
        uint64(1.5)
    with pytest.raises(ValueError):
        uint64(True)
    with pytest.raises(ValueError):
        uint64([generate_uint64])
    with pytest.raises(ValueError):
        uint64({'hash': generate_uint64})
    with pytest.raises(ValueError):
        uint64(bytes(generate_uint64, 'utf-8'))


def test_uint64_add():
    a = uint64(2)
    b = uint64(5)
    assert a + b == uint64(7)
    a += b
    assert a == uint64(7)


def test_uint64_sub():
    a = uint64(9)
    b = uint64(5)
    assert a - b == uint64(4)
    a -= b
    assert a == uint64(4)


def test_uint64_mul():
    a = uint64(2)
    b = uint64(5)
    assert a * b == uint64(2*5)
    a *= b
    assert a == uint64(2*5)


def test_uint64_floordiv():
    a = uint64(20)
    b = uint64(5)
    assert a // b == uint64(20 // 5)
    a //= b
    assert a == uint64(20 // 5)


def test_uint64_pow():
    a = uint64(20)
    b = 5
    assert a ** b == uint64(20 ** 5)
    a //= b
    assert a == uint64(20 // 5)


def test_uint64_test_underflow():
    a = uint64(2)
    b = uint64(5)
    with pytest.raises(ValueError):
        a - b
    with pytest.raises(ValueError):
        uint64(-1)


def test_uint64_test_overflow():
    numbits = 64
    with pytest.raises(ValueError):
        uint64(2**numbits)
    with pytest.raises(ValueError):
        uint64(2**numbits-1) + uint64(1)
    with pytest.raises(ValueError):
        uint64(2**numbits) * uint64(2)


def test_addition_with_other_customints():
    a = int32(2**32//2-1)
    b = int64(2**64//2-1)
    c = uint32(2**32-1)
    d = uint64(2**64-1)
    e = uint128(2**128-1)
    f = uint160(2**160-1)
    g = uint256(2**256-1)
    with pytest.raises(ValueError):
        d + a
    with pytest.raises(ValueError):
        d + b
    with pytest.raises(ValueError):
        d + c
    with pytest.raises(ValueError):
        d + e
    with pytest.raises(ValueError):
        d + f
    with pytest.raises(ValueError):
        d + g


def test_subtracting_from_larger_customints_is_ok():
    a = int32(2**32//2-1)
    b = int64(2**64//2-1)
    c = uint32(2**32-1)
    d = uint64(2**64-1)
    e = uint128(2**128-1)
    f = uint160(2**160-1)
    g = uint256(2**256-1)
    b - d
    d - c
    d - a
    e - d
    f - d
    g - d
