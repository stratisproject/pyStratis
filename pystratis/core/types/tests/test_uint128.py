import pytest
from random import choice
from pystratis.core.types import *


def test_uint128(generate_uint128):
    hex_int = generate_uint128
    uint128(hex_int)


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
    uint128(short_value)


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


def test_addition_with_other_customints():
    a = int32(2**32//2-1)
    b = int64(2**64//2-1)
    c = uint32(2**32-1)
    d = uint64(2**64-1)
    e = uint128(2**128-1)
    f = uint160(2**160-1)
    g = uint256(2**256-1)
    with pytest.raises(ValueError):
        e + a
    with pytest.raises(ValueError):
        e + b
    with pytest.raises(ValueError):
        e + c
    with pytest.raises(ValueError):
        e + d
    with pytest.raises(ValueError):
        e + f
    with pytest.raises(ValueError):
        e + g


def test_subtracting_from_larger_customints_is_ok():
    a = int32(2**32//2-1)
    b = int64(2**64//2-1)
    c = uint32(2**32-1)
    d = uint64(2**64-1)
    e = uint128(2**128-1)
    f = uint160(2**160-1)
    g = uint256(2**256-1)
    e - a
    e - b
    e - c
    e - d
    f - e
    g - e
