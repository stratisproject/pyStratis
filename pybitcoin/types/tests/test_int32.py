import pytest
from random import choice
from pybitcoin.types import *


def test_int32(generate_int32):
    hex_int = generate_int32
    int32(hex_int)


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
    int32(short_value)


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


def test_addition_with_other_customints():
    a = int32(2**32//2-1)
    b = int64(2**64//2-1)
    c = uint32(2**32-1)
    d = uint64(2**64-1)
    e = uint128(2**128-1)
    f = uint160(2**160-1)
    g = uint256(2**256-1)
    with pytest.raises(ValueError):
        a + b
    with pytest.raises(ValueError):
        a + c
    with pytest.raises(ValueError):
        a + d
    with pytest.raises(ValueError):
        a + e
    with pytest.raises(ValueError):
        a + f
    with pytest.raises(ValueError):
        a + g


def test_subtracting_from_larger_customints_is_ok():
    a = int32(2**32//2-1)
    b = int64(2**64//2-1)
    c = uint32(2**32-1)
    d = uint64(2**64-1)
    e = uint128(2**128-1)
    f = uint160(2**160-1)
    g = uint256(2**256-1)
    b - a
    c - a
    d - a
    e - a
    f - a
    g - a
