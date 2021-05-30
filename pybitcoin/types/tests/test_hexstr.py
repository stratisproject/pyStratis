import pytest
from random import choice
from pybitcoin.types import hexstr


def test_hexstr():
    hexstr('adf')
    hexstr('090fd')


def test_hexstr_invalid():
    with pytest.raises(ValueError):
        letters = 'qwerty0'
        badvalue = ''.join(choice(letters) for _ in range(64))
        hexstr(badvalue)
    with pytest.raises(ValueError):
        hexstr(10)
    with pytest.raises(ValueError):
        hexstr([10])
    with pytest.raises(ValueError):
        hexstr(['10'])
    with pytest.raises(ValueError):
        hexstr(b'10')
    with pytest.raises(ValueError):
        hexstr(True)
