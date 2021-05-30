import pytest
from random import choice
from pybitcoin.types import uint160


def test_uint160(generate_uint160):
    trx_hash = generate_uint160
    block_hash = generate_uint160

    assert uint160(trx_hash).to_hex() == trx_hash
    assert uint160(block_hash).to_hex() == block_hash


def test_uint160_invalid_hexstring():
    letters = 'qwerty0'
    badvalue = ''.join(choice(letters) for _ in range(64))
    with pytest.raises(ValueError):
        uint160(badvalue)


def test_uint160_too_long():
    letters = '0123456789abcdef'
    badvalue = ''.join(choice(letters) for _ in range(128))
    with pytest.raises(ValueError):
        uint160(badvalue)


def test_uint160_too_short():
    letters = '0123456789abcdef'
    badvalue = ''.join(choice(letters) for _ in range(32))
    with pytest.raises(ValueError):
        uint160(badvalue)


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
