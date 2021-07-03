import pytest
from decimal import Decimal
from pystratis.core.types import Money
SATOSHI_CONVERSION = 1e8


def test_money_int():
    ten = 10
    assert Money(10) == ten
    hundred = 100
    assert Money(100) == hundred


def test_money_float():
    assert Money(10.5) == 10.5
    assert Money(0.1) == 0.1


def test_money_base10_string():
    assert Money('10') == 10
    assert Money('100') == 100


def test_money_money():
    assert Money(Money(10)) == Money(10)


def test_money_negative():
    with pytest.raises(ValueError):
        Money(-10)
    with pytest.raises(ValueError):
        Money(-10.5)
    with pytest.raises(ValueError):
        Money('-10.5')
    with pytest.raises(ValueError):
        Money('-10')
    with pytest.raises(ValueError):
        Money(Decimal(-10.5))


# noinspection PyTypeChecker
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


def test_money_to_coin():
    assert Money(1).to_coin_unit() == '1.00000000'
