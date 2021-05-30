import pytest
from random import choice
from pybitcoin.types import uint64


def test_uint64(generate_uint64):
    trx_hash = generate_uint64
    block_hash = generate_uint64

    assert uint64(trx_hash).to_hex() == trx_hash
    assert uint64(block_hash).to_hex() == block_hash


def test_uint64_invalid_hexstring():
    letters = 'qwerty0'
    badvalue = ''.join(choice(letters) for _ in range(64))
    with pytest.raises(ValueError):
        uint64(badvalue)


def test_uint64_too_long():
    letters = '0123456789abcdef'
    badvalue = ''.join(choice(letters) for _ in range(128))
    with pytest.raises(ValueError):
        uint64(badvalue)


def test_uint64_too_short():
    letters = '0123456789abcdef'
    badvalue = ''.join(choice(letters) for _ in range(7))
    with pytest.raises(ValueError):
        uint64(badvalue)


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
