import pytest
from random import choice
from pystratis.core.types import *


def test_uint160(generate_uint160):
    hex_int = generate_uint160
    uint160(hex_int)


def test_uint160_invalid_hexstring():
    letters = 'qwerty0'
    badvalue = ''.join(choice(letters) for _ in range(64))
    with pytest.raises(ValueError):
        uint160(badvalue)


def test_uint160_long_hex_overflow():
    letters = '0123456789abcdef'
    badvalue = ''.join(choice(letters) for _ in range(128))
    with pytest.raises(ValueError):
        uint160(badvalue)


def test_uint160_short_hex_ok():
    first_digit = '01234567'
    letters = '0123456789abcdef'
    short_value = choice(first_digit) + ''.join(choice(letters) for _ in range(32))
    uint160(short_value)


def test_uint160_try_init_nonstr(generate_uint160):
    with pytest.raises(ValueError):
        uint160(1.5)
    with pytest.raises(ValueError):
        uint160(True)
    with pytest.raises(ValueError):
        uint160([generate_uint160])
    with pytest.raises(ValueError):
        uint160({'hash': generate_uint160})
    with pytest.raises(ValueError):
        uint160(bytes(generate_uint160, 'utf-8'))


def test_uint160_add():
    a = uint160(2)
    b = uint160(5)
    assert a + b == uint160(7)
    a += b
    assert a == uint160(7)


def test_uint160_sub():
    a = uint160(9)
    b = uint160(5)
    assert a - b == uint160(4)
    a -= b
    assert a == uint160(4)


def test_uint160_mul():
    a = uint160(2)
    b = uint160(5)
    assert a * b == uint160(2*5)
    a *= b
    assert a == uint160(2*5)


def test_uint160_floordiv():
    a = uint160(20)
    b = uint160(5)
    assert a // b == uint160(20 // 5)
    a //= b
    assert a == uint160(20 // 5)


def test_uint160_pow():
    a = uint160(20)
    b = 5
    assert a ** b == uint160(20 ** 5)
    a //= b
    assert a == uint160(20 // 5)


def test_uint160_test_underflow():
    a = uint160(2)
    b = uint160(5)
    with pytest.raises(ValueError):
        a - b
    with pytest.raises(ValueError):
        uint160(-1)


def test_uint160_test_overflow():
    numbits = 160
    with pytest.raises(ValueError):
        uint160(2**numbits)
    with pytest.raises(ValueError):
        uint160(2**numbits-1) + uint160(1)
    with pytest.raises(ValueError):
        uint160(2**numbits) * uint160(2)


def test_addition_with_other_customints():
    a = int32(2**32//2-1)
    b = int64(2**64//2-1)
    c = uint32(2**32-1)
    d = uint64(2**64-1)
    e = uint128(2**128-1)
    f = uint160(2**160-1)
    g = uint256(2**256-1)
    with pytest.raises(ValueError):
        f + a
    with pytest.raises(ValueError):
        f + b
    with pytest.raises(ValueError):
        f + c
    with pytest.raises(ValueError):
        f + d
    with pytest.raises(ValueError):
        f + e
    with pytest.raises(ValueError):
        f + g


def test_subtracting_from_larger_customints_is_ok():
    a = int32(2**32//2-1)
    b = int64(2**64//2-1)
    c = uint32(2**32-1)
    d = uint64(2**64-1)
    e = uint128(2**128-1)
    f = uint160(2**160-1)
    g = uint256(2**256-1)
    f - a
    f - b
    f - c
    f - d
    f - e
    g - f
