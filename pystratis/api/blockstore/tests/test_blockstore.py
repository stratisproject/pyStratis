import pytest
from random import randint
import pickle
from pytest_mock import MockerFixture
from pystratis.api.blockstore import BlockStore
from pystratis.api.blockstore.responsemodels import *
from pystratis.core.types import Address
from pystratis.core.networks import StraxMain, CirrusMain


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if BlockStore.route + '/' in endpoint:
            assert endpoint in BlockStore.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if BlockStore.route + '/' in endpoint:
            assert endpoint in BlockStore.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if BlockStore.route + '/' in endpoint:
            assert endpoint in BlockStore.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if BlockStore.route + '/' in endpoint:
            assert endpoint in BlockStore.endpoints


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_addressindexertip(mocker: MockerFixture, network, generate_uint256):
    data = {
        'tipHash': generate_uint256,
        'tipHeight': randint(0, 300)
    }
    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())
    response = blockstore.addressindexer_tip()

    assert response.tip_hash.to_hex() == data['tipHash']
    assert response.tip_height == data['tipHeight']
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_addressindexertip_no_tipheight(mocker: MockerFixture, network, generate_uint256):
    data = {
        'tipHash': generate_uint256
    }
    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())
    response = blockstore.addressindexer_tip()

    assert response.tip_hash.to_hex() == data['tipHash']
    assert response.tip_height is None
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_block_output_hexstr_no_details(mocker: MockerFixture, network, generate_uint256, generate_block_no_tx_data):
    data = pickle.dumps(generate_block_no_tx_data).hex()
    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = blockstore.block(
        block_hash=generate_uint256,
        show_transaction_details=True,
        output_json=False
    )

    assert response == data
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_block_output_hexstr_include_details(mocker: MockerFixture, network, generate_uint256, generate_block_with_tx_data):
    data = pickle.dumps(generate_block_with_tx_data(network=network)).hex()
    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = blockstore.block(
        block_hash=generate_uint256,
        show_transaction_details=True,
        output_json=False
    )

    assert response == data
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_block_output_json_no_details(mocker: MockerFixture, network, generate_uint256, generate_block_no_tx_data):
    data = generate_block_no_tx_data
    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = blockstore.block(
        block_hash=generate_uint256,
        show_transaction_details=False,
        output_json=True
    )

    assert response == BlockModel(**data)
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_block_output_json_include_details(mocker: MockerFixture, network, generate_uint256, generate_block_with_tx_data):
    data = generate_block_with_tx_data(network=network)
    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = blockstore.block(
        block_hash=generate_uint256,
        show_transaction_details=True,
        output_json=True
    )

    assert response == BlockTransactionDetailsModel(**data)
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_block_no_found(mocker: MockerFixture, network, generate_uint256):
    data = 'Block not found'
    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = blockstore.block(
        block_hash=generate_uint256,
        show_transaction_details=True,
        output_json=True
    )

    assert response == data
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getblockcount(mocker: MockerFixture, network):
    data = 10
    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())
    response = blockstore.get_block_count()

    assert response == data
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getaddressbalances_single_address(mocker: MockerFixture, network, generate_p2pkh_address):
    address = generate_p2pkh_address(network=network)
    data = {
        'balances': [
            {'address': address, 'balance': 500000000}
        ],
        'reason': None
    }
    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = blockstore.get_addresses_balances(addresses=address)

    assert response == GetAddressesBalancesModel(**data)
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getaddressbalances_multiple_addresses(mocker: MockerFixture, network, generate_p2pkh_address, generate_p2sh_address, generate_p2wpkh_address, generate_p2wsh_address):
    addresses = [
        generate_p2pkh_address(network=network),
        generate_p2sh_address(network=network),
        generate_p2wpkh_address(network=network),
        generate_p2wsh_address(network=network)
    ]
    data = {
        'balances': [
            {'address': addresses[0], 'balance': 5},
            {'address': addresses[1], 'balance': 5},
            {'address': addresses[2], 'balance': 5},
            {'address': addresses[3], 'balance': 5}
        ],
        'reason': None
    }
    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = blockstore.get_addresses_balances(addresses=addresses)

    assert response == GetAddressesBalancesModel(**data)
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getverboseaddressbalances_single_address(mocker: MockerFixture, network, generate_p2pkh_address):
    address = generate_p2pkh_address(network=network)
    data = {
        'balancesData': [
            {'address': address, 'balanceChanges': [{"deposited": True, "satoshi": 5, "balanceChangedHeight": 0}]}
        ],
        'consensusTipHeight': 10,
        'reason': None
    }
    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = blockstore.get_verbose_addresses_balances(addresses=address)

    assert response == GetVerboseAddressesBalancesModel(**data)
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getverboseaddressbalances_multiple_addresses(mocker: MockerFixture, network, generate_p2pkh_address, generate_p2sh_address, generate_p2wpkh_address, generate_p2wsh_address):
    addresses = [
        generate_p2pkh_address(network=network),
        generate_p2sh_address(network=network),
        generate_p2wpkh_address(network=network),
        generate_p2wsh_address(network=network)
    ]
    data = {
        'balancesData': [
            {'address': addresses[0], 'balanceChanges': [{"deposited": True, "satoshi": 5, "balanceChangedHeight": 0}]},
            {'address': addresses[1], 'balanceChanges': [{"deposited": True, "satoshi": 5, "balanceChangedHeight": 0}]},
            {'address': addresses[2], 'balanceChanges': [{"deposited": True, "satoshi": 5, "balanceChangedHeight": 0}]},
            {'address': addresses[3], 'balanceChanges': [{"deposited": True, "satoshi": 5, "balanceChangedHeight": 0}]}
        ],
        'consensusTipHeight': 10,
        'reason': None
    }

    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = blockstore.get_verbose_addresses_balances(addresses=addresses)

    assert response == GetVerboseAddressesBalancesModel(**data)
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getverboseaddressbalances_single_address_no_changes(mocker: MockerFixture, network, generate_p2pkh_address):
    address = generate_p2pkh_address(network=network)
    data = {
        'balancesData': [
            {'address': address, 'balanceChanges': []}
        ],
        'consensusTipHeight': 10,
        'reason': None
    }

    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = blockstore.get_verbose_addresses_balances(addresses=address)

    assert response == GetVerboseAddressesBalancesModel(**data)
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getutxoset(mocker: MockerFixture, network, generate_uint256, generate_hexstring):
    data = [
        {
            "txId": generate_uint256,
            "index": 0,
            "scriptPubKey": generate_hexstring(64),
            "value": int(randint(1, 100) * 1e8)
        },
        {
            "txId": generate_uint256,
            "index": 0,
            "scriptPubKey": generate_hexstring(64),
            "value": int(randint(1, 100) * 1e8)
        },
    ]
    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = blockstore.get_utxo_set(at_block_height=2)

    assert response == [UTXOModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getutxoset_empty(mocker: MockerFixture, network, generate_uint256, generate_hexstring):
    data = []
    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = blockstore.get_utxo_set(at_block_height=2)

    assert response == [UTXOModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getlastbalanceupdatetransaction(mocker: MockerFixture, network, generate_p2pkh_address, generate_uint256, generate_transaction):
    address = Address(address=generate_p2pkh_address(network=network), network=network)
    data = {
        'transaction': generate_transaction(trxid=generate_uint256, network=network),
        'blockHeight': 1
    }
    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = blockstore.get_last_balance_update_transaction(address=address)

    assert response == GetLastBalanceUpdateTransactionModel(**data)
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()
