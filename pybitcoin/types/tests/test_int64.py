import pytest
from random import choice
from pybitcoin.types import *


def test_int64(generate_int64):
    hex_int = generate_int64
    int64(hex_int)


def test_int64_invalid_hexstring():
    letters = 'qwerty0'
    badvalue = ''.join(choice(letters) for _ in range(64))
    with pytest.raises(ValueError):
        int64(badvalue)


def test_int64_long_hex_overflow():
    letters = '0123456789abcdef'
    long_value = ''.join(choice(letters) for _ in range(128))
    with pytest.raises(ValueError):
        int64(long_value)


def test_int64_short_hex_ok():
    letters = '0123456789abcdef'
    short_value = ''.join(choice(letters) for _ in range(12))
    assert short_value in int64(short_value).to_hex()


def test_int64_try_init_nonstr(generate_int64):
    with pytest.raises(ValueError):
        int64(1.5)
    with pytest.raises(ValueError):
        int64(True)
    with pytest.raises(ValueError):
        int64([generate_int64])
    with pytest.raises(ValueError):
        int64({'hash': generate_int64})
    with pytest.raises(ValueError):
        int64(bytes(generate_int64, 'utf-8'))


def test_int64_add():
    a = int64(2)
    b = int64(5)
    assert a + b == int64(7)
    a += b
    assert a == int64(7)


def test_int64_sub():
    a = int64(9)
    b = int64(5)
    assert a - b == int64(4)
    a -= b
    assert a == int64(4)


def test_int64_mul():
    a = int64(2)
    b = int64(5)
    assert a * b == int64(2*5)
    a *= b
    assert a == int64(2*5)


def test_int64_floordiv():
    a = int64(20)
    b = int64(5)
    assert a // b == int64(20 // 5)
    a //= b
    assert a == int64(20 // 5)


def test_int64_pow():
    a = int64(20)
    b = 5
    assert a ** b == int64(20 ** 5)
    a //= b
    assert a == int64(20 // 5)


def test_int64_test_underflow():
    numbits = 64
    a = int64(2**numbits // -2)
    b = int64(5)
    with pytest.raises(ValueError):
        a - b
    with pytest.raises(ValueError):
        int64(2**numbits // -2 - 1)


def test_int64_test_overflow():
    numbits = 64
    with pytest.raises(ValueError):
        int64(2**numbits)
    with pytest.raises(ValueError):
        int64(2**numbits-1) + int64(1)
    with pytest.raises(ValueError):
        int64(2**numbits) * int64(2)


def test_addition_with_other_customints():
    a = int32(2**32//2-1)
    b = int64(2**64//2-1)
    c = uint32(2**32-1)
    d = uint64(2**64-1)
    e = uint128(2**128-1)
    f = uint160(2**160-1)
    g = uint256(2**256-1)
    with pytest.raises(ValueError):
        b + a
    with pytest.raises(ValueError):
        b + c
    with pytest.raises(ValueError):
        b + d
    with pytest.raises(ValueError):
        b + e
    with pytest.raises(ValueError):
        b + f
    with pytest.raises(ValueError):
        b + g


def test_subtracting_from_larger_customints_is_ok():
    a = int32(2**32//2-1)
    b = int64(2**64//2-1)
    c = uint32(2**32-1)
    d = uint64(2**64-1)
    e = uint128(2**128-1)
    f = uint160(2**160-1)
    g = uint256(2**256-1)
    b - a
    b - c
    d - b
    e - b
    f - b
    g - b
