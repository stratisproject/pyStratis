import pytest
from random import choice
from pybitcoin.types import int64


def test_int64(generate_int64):
    trx_hash = generate_int64
    block_hash = generate_int64

    assert int64(trx_hash).to_hex() == trx_hash
    assert int64(block_hash).to_hex() == block_hash


def test_int64_invalid_hexstring():
    letters = 'qwerty0'
    badvalue = ''.join(choice(letters) for _ in range(64))
    with pytest.raises(ValueError):
        int64(badvalue)


def test_int64_too_long():
    letters = '0123456789abcdef'
    badvalue = ''.join(choice(letters) for _ in range(128))
    with pytest.raises(ValueError):
        int64(badvalue)


def test_int64_too_short():
    letters = '0123456789abcdef'
    badvalue = ''.join(choice(letters) for _ in range(12))
    with pytest.raises(ValueError):
        int64(badvalue)


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
