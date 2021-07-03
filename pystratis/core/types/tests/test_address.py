import pytest
from pystratis.core.types import Address
from pystratis.core.networks import StraxMain, StraxTest, StraxRegTest, \
    CirrusMain, CirrusTest, CirrusRegTest, Ethereum


@pytest.mark.parametrize('network',
                         [StraxMain(), StraxTest(), StraxRegTest(), CirrusMain(), CirrusTest(), CirrusRegTest()],
                         ids=['StraxMain', 'StraxTest', 'StraxRegTest', 'CirrusMain', 'CirrusTest', 'CirrusRegTest'])
def test_missing_network_raises_error(generate_p2pkh_address, network):
    address = generate_p2pkh_address(network=network)
    with pytest.raises(TypeError):
        # noinspection PyArgumentList
        Address(address=address)


@pytest.mark.parametrize('network',
                         [StraxMain(), StraxTest(), StraxRegTest(), CirrusMain(), CirrusTest(), CirrusRegTest()],
                         ids=['StraxMain', 'StraxTest', 'StraxRegTest', 'CirrusMain', 'CirrusTest', 'CirrusRegTest'])
def test_valid_p2pkh_address_is_valid(generate_p2pkh_address, network):
    address = generate_p2pkh_address(network=network)
    Address(address=address, network=network)


@pytest.mark.parametrize('network',
                         [StraxMain(), StraxTest(), StraxRegTest(), CirrusMain(), CirrusTest(), CirrusRegTest()],
                         ids=['StraxMain', 'StraxTest', 'StraxRegTest', 'CirrusMain', 'CirrusTest', 'CirrusRegTest'])
def test_invalid_p2pkh_address_is_invalid(generate_p2pkh_address, network):
    address = generate_p2pkh_address(network=network)
    short_bad_address = address[:26]
    with pytest.raises(ValueError):
        Address(address=short_bad_address, network=network)
    long_bad_address = address + 'extra'
    with pytest.raises(ValueError):
        Address(address=long_bad_address, network=network)
    char_replacement = address[:8] + 'l' + address[9:]
    with pytest.raises(ValueError):
        Address(address=char_replacement, network=network)


@pytest.mark.parametrize('network',
                         [StraxMain(), StraxTest(), StraxRegTest(), CirrusMain(), CirrusTest(), CirrusRegTest()],
                         ids=['StraxMain', 'StraxTest', 'StraxRegTest', 'CirrusMain', 'CirrusTest', 'CirrusRegTest'])
def test_valid_p2sh_address_is_valid(generate_p2sh_address, network):
    address = generate_p2sh_address(network=network)
    Address(address=address, network=network)


@pytest.mark.parametrize('network',
                         [StraxMain(), StraxTest(), StraxRegTest(), CirrusMain(), CirrusTest(), CirrusRegTest()],
                         ids=['StraxMain', 'StraxTest', 'StraxRegTest', 'CirrusMain', 'CirrusTest', 'CirrusRegTest'])
def test_invalid_p2sh_address_is_invalid(generate_p2sh_address, network):
    address = generate_p2sh_address(network=network)
    short_bad_address = address[:26]
    with pytest.raises(ValueError):
        Address(address=short_bad_address, network=network)
    long_bad_address = address + 'extra'
    with pytest.raises(ValueError):
        Address(address=long_bad_address, network=network)
    char_replacement = address[:8] + 'l' + address[9:]
    with pytest.raises(ValueError):
        Address(address=char_replacement, network=network)


@pytest.mark.parametrize('network',
                         [StraxMain(), StraxTest(), StraxRegTest(), CirrusMain(), CirrusTest(), CirrusRegTest()],
                         ids=['StraxMain', 'StraxTest', 'StraxRegTest', 'CirrusMain', 'CirrusTest', 'CirrusRegTest'])
def test_valid_p2wpkh_address_is_valid(generate_p2wpkh_address, network):
    address = generate_p2wpkh_address(network=network)
    Address(address=address, network=network)


@pytest.mark.parametrize('network',
                         [StraxMain(), StraxTest(), StraxRegTest(), CirrusMain(), CirrusTest(), CirrusRegTest()],
                         ids=['StraxMain', 'StraxTest', 'StraxRegTest', 'CirrusMain', 'CirrusTest', 'CirrusRegTest'])
def test_invalid_p2wpkh_address_is_invalid(generate_p2wpkh_address, network):
    address = generate_p2wpkh_address(network=network)
    short_bad_address = address[:26]
    with pytest.raises(ValueError):
        Address(address=short_bad_address, network=network)
    long_bad_address = address + 'extra'
    with pytest.raises(ValueError):
        Address(address=long_bad_address, network=network)
    char_replacement = address[:8] + 'i' + address[9:]
    with pytest.raises(ValueError):
        Address(address=char_replacement, network=network)


@pytest.mark.parametrize('network',
                         [StraxMain(), StraxTest(), StraxRegTest(), CirrusMain(), CirrusTest(), CirrusRegTest()],
                         ids=['StraxMain', 'StraxTest', 'StraxRegTest', 'CirrusMain', 'CirrusTest', 'CirrusRegTest'])
def test__valid_p2wsh_address_is_valid(generate_p2wsh_address, network):
    address = generate_p2wsh_address(network=network)
    Address(address=address, network=network)


@pytest.mark.parametrize('network',
                         [StraxMain(), StraxTest(), StraxRegTest(), CirrusMain(), CirrusTest(), CirrusRegTest()],
                         ids=['StraxMain', 'StraxTest', 'StraxRegTest', 'CirrusMain', 'CirrusTest', 'CirrusRegTest'])
def test_invalid_p2wsh_address_is_invalid(generate_p2wsh_address, network):
    address = generate_p2wsh_address(network=network)
    short_bad_address = address[:26]
    with pytest.raises(ValueError):
        Address(address=short_bad_address, network=network)
    long_bad_address = address + 'extra'
    with pytest.raises(ValueError):
        Address(address=long_bad_address, network=network)
    char_replacement = address[:8] + 'i' + address[9:]
    with pytest.raises(ValueError):
        Address(address=char_replacement, network=network)


@pytest.mark.parametrize('network', [Ethereum()], ids=['Ethereum'])
def test_ethereum_lower_address_is_valid(generate_ethereum_lower_address, network):
    Address(address=generate_ethereum_lower_address, network=network)


@pytest.mark.parametrize('network', [Ethereum()], ids=['Ethereum'])
def test_ethereum_upper_address_is_valid(generate_ethereum_upper_address, network):
    Address(address=generate_ethereum_upper_address, network=network)


@pytest.mark.parametrize('network', [Ethereum()], ids=['Ethereum'])
def test_ethereum_checksum_address_is_valid(generate_ethereum_checksum_address, network):
    Address(address=generate_ethereum_checksum_address, network=network)
