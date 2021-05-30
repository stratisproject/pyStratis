import pytest
from decimal import Decimal
from pybitcoin.types import Money
SATOSHI_CONVERSION = 1e8


def test_money_int():
    ten = 10
    assert str(Money(ten)) == str(ten)
    hundred = 100
    assert str(Money(hundred)) == str(hundred)


def test_money_float():
    ten_point_five = 10.5
    assert str(Money(10.5)) == str(int(Decimal(ten_point_five) * Decimal(SATOSHI_CONVERSION)))
    one_hundreth = 0.01
    assert str(Money(one_hundreth)) == str(int(Decimal(one_hundreth) * Decimal(SATOSHI_CONVERSION)))


def test_money_base10_string():
    ten = 10
    assert str(Money(str(ten))) == str(ten)
    hundred = 100
    assert str(Money(str(hundred))) == str(hundred)


def test_money_negative():
    with pytest.raises(ValueError):
        Money(-10)
    with pytest.raises(ValueError):
        Money(-10.5)
    with pytest.raises(ValueError):
        Money(Decimal(-10.5))


def test_money_invalid():
    with pytest.raises(ValueError):
        Money('string')
    with pytest.raises(ValueError):
        Money([10])
    with pytest.raises(ValueError):
        Money([10.5])
    with pytest.raises(ValueError):
        Money([Decimal(10.5)])
    with pytest.raises(ValueError):
        Money(bytes([10]))
