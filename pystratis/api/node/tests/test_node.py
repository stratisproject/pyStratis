import pytest
import ast
from pytest_mock import MockerFixture
from pystratis.api.node import Node
from pystratis.api.node.responsemodels import *
from pystratis.api import FullNodeState, FeatureInitializationState, LogRule
from pystratis.core.networks import StraxMain, CirrusMain


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_status_no_publish(mocker: MockerFixture, network):
    data = {
        'agent': 'nodeagent',
        'version': 'nodeversion',
        'externalAddress': '[::0.0.0.0]',
        'network': network.name,
        'coin_ticker': 'STRAX' if 'Strax' in network.name else 'CRS',
        'processId': '0',
        'consensusHeight': 10,
        'blockStoreHeight': 10,
        'bestPeerHeight': 10,
        'inboundPeers': [
            {
                'version': 1,
                'remoteSocketEndpoint': '[::0.0.0.0]',
                'tipHeight': 10
            }
        ],
        'outboundPeers': [
            {
                'version': 1,
                'remoteSocketEndpoint': '[::0.0.0.0]',
                'tipHeight': 10
            }
        ],
        'featuresData': [
            {
                'namespace': 'node.feature',
                'state': FeatureInitializationState.Initialized
            }
        ],
        'dataDirectoryPath': '/my/data/dir',
        'runningTime': 'a long time',
        'difficulty': 100000.0000,
        'protocolVersion': 123,
        'testnet': False,
        'relayFee': 0,
        'state': FullNodeState.Initialized,
        'inIbd': False,
        'headerHeight': 1
    }
    mocker.patch.object(Node, 'get', return_value=data)
    node = Node(network=network, baseuri=mocker.MagicMock())

    response = node.status(publish=False)

    assert response == StatusModel(**data)
    # noinspection PyUnresolvedReferences
    node.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_status_publish(mocker: MockerFixture, network):
    data = {
        'agent': 'nodeagent',
        'version': 'nodeversion',
        'externalAddress': '[::0.0.0.0]',
        'network': network.name,
        'coin_ticker': 'STRAX' if 'Strax' in network.name else 'CRS',
        'processId': '0',
        'consensusHeight': 10,
        'blockStoreHeight': 10,
        'bestPeerHeight': 10,
        'inboundPeers': [
            {
                'version': 1,
                'remoteSocketEndpoint': '[::0.0.0.0]',
                'tipHeight': 10
            }
        ],
        'outboundPeers': [
            {
                'version': 1,
                'remoteSocketEndpoint': '[::0.0.0.0]',
                'tipHeight': 10
            }
        ],
        'featuresData': [
            {
                'namespace': 'node.feature',
                'state': FeatureInitializationState.Initialized
            }
        ],
        'dataDirectoryPath': '/my/data/dir',
        'runningTime': 'a long time',
        'difficulty': 100000.0000,
        'protocolVersion': 123,
        'testnet': False,
        'relayFee': 0,
        'state': FullNodeState.Initialized,
        'inIbd': False,
        'headerHeight': 1
    }
    mocker.patch.object(Node, 'get', return_value=data)
    node = Node(network=network, baseuri=mocker.MagicMock())

    response = node.status(publish=True)

    assert response == StatusModel(**data)
    # noinspection PyUnresolvedReferences
    node.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_blockheader(mocker: MockerFixture, network, generate_uint256):
    data = {
        'version': 1,
        'merkleroot': generate_uint256,
        'nonce': 0,
        'bits': 'bits',
        'previousblockhash': generate_uint256,
        'time': 1,
    }
    mocker.patch.object(Node, 'get', return_value=data)
    node = Node(network=network, baseuri=mocker.MagicMock())
    response = node.get_blockheader(
        block_hash=generate_uint256,
        is_json_format=True
    )

    assert response == BlockHeaderModel(**data)
    # noinspection PyUnresolvedReferences
    node.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_raw_transaction_verbose(mocker: MockerFixture, network, generate_coinbase_transaction, generate_uint256):
    trxid = generate_uint256
    data = generate_coinbase_transaction(trxid)
    mocker.patch.object(Node, 'get', return_value=data)
    node = Node(network=network, baseuri=mocker.MagicMock())

    response = node.get_raw_transaction(trxid=trxid, verbose=True)

    assert response == TransactionModel(**data)
    # noinspection PyUnresolvedReferences
    node.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_raw_transaction_nonverbose(mocker: MockerFixture, network, generate_coinbase_transaction, generate_uint256):
    trxid = generate_uint256
    data = generate_coinbase_transaction(trxid)
    hexified_data = bytes(str(data), 'ascii').hex()
    mocker.patch.object(Node, 'get', return_value=hexified_data)
    node = Node(network=network, baseuri=mocker.MagicMock())

    response = node.get_raw_transaction(trxid=trxid, verbose=False)

    assert response == hexified_data
    unserialized_response = ast.literal_eval(bytes.fromhex(hexified_data).decode('ascii'))
    assert data == unserialized_response
    # noinspection PyUnresolvedReferences
    node.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_decode_raw_transaction(mocker: MockerFixture, network, generate_uint256, generate_coinbase_transaction):
    trxid = generate_uint256
    data = generate_coinbase_transaction(trxid)
    hexified_data = bytes(str(data), 'ascii').hex()
    mocker.patch.object(Node, 'post', return_value=data)
    node = Node(network=network, baseuri=mocker.MagicMock())

    response = node.decode_raw_transaction(raw_hex=hexified_data)

    assert response == TransactionModel(**data)
    # noinspection PyUnresolvedReferences
    node.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_validate_address(mocker: MockerFixture, network, generate_p2pkh_address):
    address = generate_p2pkh_address(network=network)
    data = {
        'isvalid': True,
        'address': address,
        'scriptPubKey': 'a scriptPubKey',
        'isscript': False,
        'iswitness': False
    }
    mocker.patch.object(Node, 'get', return_value=data)
    node = Node(network=network, baseuri=mocker.MagicMock())

    response = node.validate_address(address=address)

    assert response == ValidateAddressModel(**data)
    # noinspection PyUnresolvedReferences
    node.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_txout(mocker: MockerFixture, network, generate_uint256, generate_hexstring, generate_p2pkh_address):
    data = {
        'bestblock': generate_uint256,
        'confirmations': 1,
        'value': 5,
        'scriptPubKey': {
            'asm': generate_hexstring(128),
            'hex': generate_hexstring(128),
            'type': 'pubkey',
            'reqSigs': 1,
            "addresses": [
                generate_p2pkh_address(network=network)
            ]
        },
        'coinbase': False
    }
    mocker.patch.object(Node, 'get', return_value=data)
    node = Node(network=network, baseuri=mocker.MagicMock())

    response = node.get_txout(trxid=generate_uint256, vout=0, include_mempool=False)

    assert response == GetTxOutModel(**data)
    # noinspection PyUnresolvedReferences
    node.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_get_txout_proof(mocker: MockerFixture, network, generate_uint256, generate_hexstring):
    data = generate_hexstring(128)
    mocker.patch.object(Node, 'get', return_value=data)
    node = Node(network=network, baseuri=mocker.MagicMock())
    response = node.get_txout_proof(
        txids=[
            generate_uint256,
            generate_uint256
        ],
        block_hash=generate_uint256
    )

    assert response == data
    # noinspection PyUnresolvedReferences
    node.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_shutdown(mocker: MockerFixture, network):
    data = None
    mocker.patch.object(Node, 'post', return_value=data)
    node = Node(network=network, baseuri=mocker.MagicMock())

    node.shutdown()

    # noinspection PyUnresolvedReferences
    node.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_stop(mocker: MockerFixture, network):
    data = None
    mocker.patch.object(Node, 'post', return_value=data)
    node = Node(network=network, baseuri=mocker.MagicMock())

    node.stop()

    # noinspection PyUnresolvedReferences
    node.post.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_log_levels(mocker: MockerFixture, network):
    data = None
    mocker.patch.object(Node, 'put', return_value=data)
    node = Node(network=network, baseuri=mocker.MagicMock())

    node.log_levels(log_rules=[LogRule(rule_name='TestRule', log_level='Debug', filename='filename')])

    # noinspection PyUnresolvedReferences
    node.put.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_log_rules(mocker: MockerFixture, network):
    data = [
        {
            'ruleName': 'TestRule',
            'logLevel': 'Debug',
            'filename': 'filename'
        }
    ]

    mocker.patch.object(Node, 'get', return_value=data)
    node = Node(network=network, baseuri=mocker.MagicMock())

    response = node.log_rules()

    assert response == [LogRule(**x) for x in data]
    # noinspection PyUnresolvedReferences
    node.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_async_loops(mocker: MockerFixture, network):
    data = [
        {
            'loopName': 'Loop1',
            'status': 'Running'
        }
    ]
    mocker.patch.object(Node, 'get', return_value=data)
    node = Node(network=network, baseuri=mocker.MagicMock())

    response = node.async_loops()

    assert response == [AsyncLoopsModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    node.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_rewind(mocker: MockerFixture, network):
    data = "Rewind flag set, please restart the node."
    mocker.patch.object(Node, 'put', return_value=data)
    node = Node(network=network, baseuri=mocker.MagicMock())

    response = node.rewind(height=2)

    assert isinstance(response, str)
    # noinspection PyUnresolvedReferences
    node.put.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_delete_datafolder_chain(mocker: MockerFixture, network):
    data = None
    mocker.patch.object(Node, 'delete', return_value=data)
    node = Node(network=network, baseuri=mocker.MagicMock())

    node.delete_datafolder_chain()

    # noinspection PyUnresolvedReferences
    node.delete.assert_called_once()
