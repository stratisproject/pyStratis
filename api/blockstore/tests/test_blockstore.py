import pytest
from random import randint
import pickle
from pytest_mock import MockerFixture
from api.blockstore import BlockStore
from api.blockstore.requestmodels import *
from api.blockstore.responsemodels import *
from pybitcoin import Address, BlockModel, BlockTransactionDetailsModel
from pybitcoin.networks import StraxMain, CirrusMain


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if BlockStore.route in endpoint:
            assert endpoint in BlockStore.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if BlockStore.route in endpoint:
            assert endpoint in BlockStore.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if BlockStore.route in endpoint:
            assert endpoint in BlockStore.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if BlockStore.route in endpoint:
            assert endpoint in BlockStore.endpoints


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_addressindexertip(mocker: MockerFixture, network, fakeuri, generate_uint256):
    data = {
        'TipHash': generate_uint256,
        'TipHeight': randint(0, 300)
    }

    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=fakeuri)
    response = blockstore.addressindexer_tip()

    assert response.tip_hash.to_hex() == data['TipHash']
    assert response.tip_height == data['TipHeight']
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_addressindexertip_no_tipheight(mocker: MockerFixture, network, fakeuri, generate_uint256):
    data = {
        'TipHash': generate_uint256
    }

    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=fakeuri)
    response = blockstore.addressindexer_tip()

    assert response.tip_hash.to_hex() == data['TipHash']
    assert response.tip_height is None
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_addressindexertip_no_tiphash_raises_error(mocker: MockerFixture, network, fakeuri, generate_uint256):
    data = {
        'TipHeight': randint(0, 300)
    }

    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=fakeuri)
    with pytest.raises(ValueError):
        blockstore.addressindexer_tip()
        # noinspection PyUnresolvedReferences
        blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_block_output_hexstr_no_details(mocker: MockerFixture, network, fakeuri, generate_uint256, create_block_no_tx_data):
    request = BlockRequest(
        hash=generate_uint256,
        show_transaction_details=True,
        output_json=False
    )
    data = pickle.dumps(create_block_no_tx_data).hex()

    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=fakeuri)
    response = blockstore.block(request_model=request)

    assert response == data
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_block_output_hexstr_include_details(mocker: MockerFixture, network, fakeuri, generate_uint256, create_block_with_tx_data):
    request = BlockRequest(
        hash=generate_uint256,
        show_transaction_details=True,
        output_json=False
    )
    data = pickle.dumps(create_block_with_tx_data(network=network)).hex()

    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=fakeuri)
    response = blockstore.block(request_model=request)

    assert response == data
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_block_output_json_no_details(mocker: MockerFixture, network, fakeuri, generate_uint256, create_block_no_tx_data):
    request = BlockRequest(
        hash=generate_uint256,
        show_transaction_details=False,
        output_json=True
    )
    data = create_block_no_tx_data

    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=fakeuri)
    response = blockstore.block(request_model=request)

    assert response == BlockModel(**data)
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_block_output_json_include_details(mocker: MockerFixture, network, fakeuri, generate_uint256, create_block_with_tx_data):
    request = BlockRequest(
        hash=generate_uint256,
        show_transaction_details=True,
        output_json=True
    )
    data = create_block_with_tx_data(network=network)

    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=fakeuri)
    response = blockstore.block(request_model=request)

    assert response == BlockTransactionDetailsModel(**data)
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_block_no_found(mocker: MockerFixture, network, fakeuri, generate_uint256):
    request = BlockRequest(
        hash=generate_uint256,
        show_transaction_details=True,
        output_json=True
    )
    data = 'Block not found'

    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=fakeuri)
    response = blockstore.block(request_model=request)

    assert response == data
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getblockcount(mocker: MockerFixture, network, fakeuri, ):
    data = 10

    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=fakeuri)
    response = blockstore.get_blockcount()

    assert response == data
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getaddressbalances_single_address(mocker: MockerFixture, network, fakeuri, create_p2pkh_address):
    address = Address(address=create_p2pkh_address(network=network), network=network)
    request = GetAddressesBalancesRequest(addresses=address)
    data = {
        'balances': [
            {'address': address, 'balance': 5}
        ],
        'reason': None
    }

    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=fakeuri)
    response = blockstore.get_addresses_balances(request_model=request)

    assert response == GetAddressesBalancesModel(**data)
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getaddressbalances_multiple_addresses(mocker: MockerFixture, network, fakeuri, create_p2pkh_address, create_p2sh_address, create_p2wpkh_address, create_p2wsh_address):
    addresses = [
        Address(address=create_p2pkh_address(network=network), network=network),
        Address(address=create_p2sh_address(network=network), network=network),
        Address(address=create_p2wpkh_address(network=network), network=network),
        Address(address=create_p2wsh_address(network=network), network=network)
    ]
    request = GetAddressesBalancesRequest(addresses=addresses)
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
    blockstore = BlockStore(network=network, baseuri=fakeuri)
    response = blockstore.get_addresses_balances(request_model=request)

    assert response == GetAddressesBalancesModel(**data)
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getverboseaddressbalances_single_address(mocker: MockerFixture, network, fakeuri, create_p2pkh_address):
    address = Address(address=create_p2pkh_address(network=network), network=network)
    request = GetVerboseAddressesBalancesRequest(addresses=address)

    data = {
        'balancesData': [
            {'address': address, 'balanceChanges': [{"deposited": True, "satoshi": 5, "balanceChangedHeight": 0}]}
        ],
        'consensusTipHeight': 10,
        'reason': None
    }

    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=fakeuri)
    response = blockstore.get_verbose_addresses_balances(request_model=request)

    assert response == GetVerboseAddressesBalancesModel(**data)
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getverboseaddressbalances_multiple_addresses(mocker: MockerFixture, network, fakeuri, create_p2pkh_address, create_p2sh_address, create_p2wpkh_address, create_p2wsh_address):
    addresses = [
        Address(address=create_p2pkh_address(network=network), network=network),
        Address(address=create_p2sh_address(network=network), network=network),
        Address(address=create_p2wpkh_address(network=network), network=network),
        Address(address=create_p2wsh_address(network=network), network=network)
    ]
    request = GetVerboseAddressesBalancesRequest(addresses=addresses)
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
    blockstore = BlockStore(network=network, baseuri=fakeuri)
    response = blockstore.get_verbose_addresses_balances(request_model=request)

    assert response == GetVerboseAddressesBalancesModel(**data)
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getverboseaddressbalances_single_address_no_changes(mocker: MockerFixture, network, fakeuri, create_p2pkh_address):
    address = Address(address=create_p2pkh_address(network=network), network=network)
    request = GetVerboseAddressesBalancesRequest(addresses=address)
    data = {
        'balancesData': [
            {'address': address, 'balanceChanges': []}
        ],
        'consensusTipHeight': 10,
        'reason': None
    }

    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=fakeuri)
    response = blockstore.get_verbose_addresses_balances(request_model=request)

    assert response == GetVerboseAddressesBalancesModel(**data)
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getutxoset(mocker: MockerFixture, network, fakeuri, generate_uint256, generate_hexstring):
    request = GetUTXOSetRequest(at_block_height=2)
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
    blockstore = BlockStore(network=network, baseuri=fakeuri)
    response = blockstore.get_utxo_set(request_model=request)

    assert response == [UTXOModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getutxoset_empty(mocker: MockerFixture, network, fakeuri, generate_uint256, generate_hexstring):
    request = GetUTXOSetRequest(at_block_height=2)
    data = []

    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=fakeuri)
    response = blockstore.get_utxo_set(request_model=request)

    assert response == [UTXOModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_getlastbalanceupdatetransaction(mocker: MockerFixture, network, fakeuri, create_p2pkh_address, generate_uint256, generate_transaction):
    address = Address(address=create_p2pkh_address(network=network), network=network)
    request = GetLastBalanceUpdateTransactionRequest(address=address)
    data = {
        'transaction': generate_transaction(trxid=generate_uint256, network=network),
        'blockHeight': 1
    }

    mocker.patch.object(BlockStore, 'get', return_value=data)
    blockstore = BlockStore(network=network, baseuri=fakeuri)
    response = blockstore.get_last_balance_update_transaction(request_model=request)

    assert response == GetLastBalanceUpdateTransactionModel(**data)
    # noinspection PyUnresolvedReferences
    blockstore.get.assert_called_once()
