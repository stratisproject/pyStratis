import pytest
from pytest_mock import MockerFixture
from pystratis.api.federationgateway.responsemodels import *
from pystratis.api.federationgateway import FederationGateway
from pystratis.core import CrossChainTransferStatus, DepositRetrievalType
from pystratis.core.networks import StraxMain, CirrusMain


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_deposits(mocker: MockerFixture, network, generate_uint256, generate_p2pkh_address):
    target_network = StraxMain() if isinstance(network, CirrusMain) else CirrusMain()
    data = {
        'value': [{
            'deposits': [
                {
                    'id': generate_uint256,
                    'amount': 10,
                    'targetAddress': generate_p2pkh_address(network=target_network),
                    'blockNumber': 10,
                    'blockHash': generate_uint256,
                    'retrievalType': DepositRetrievalType.Small.value
                }
            ],
            'blockInfo': {
                'blockHash': generate_uint256,
                'blockHeight': 10,
                'blockTime': 1
            }
        }]
    }
    mocker.patch.object(FederationGateway, 'get', return_value=data)
    federation_gateway = FederationGateway(network=network, baseuri=mocker.MagicMock())
    response = federation_gateway.deposits(block_height=5)
    assert response == [MaturedBlockDepositsModel(**x) for x in data['value']]
    # noinspection PyUnresolvedReferences
    federation_gateway.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_pending_transfer(mocker: MockerFixture, network, generate_uint256, generate_coinbase_transaction):
    txid = generate_uint256
    data = [{
        'depositAmount': 5,
        'depositId': generate_uint256,
        'depositHeight': 5,
        'transferStatus': CrossChainTransferStatus.Partial,
        'tx': generate_coinbase_transaction(txid)
    }]
    mocker.patch.object(FederationGateway, 'get', return_value=data)
    federation_gateway = FederationGateway(network=network, baseuri=mocker.MagicMock())
    response = federation_gateway.pending_transfer(deposit_id=data[0]['depositId'], transaction_id=txid)
    assert response == [CrossChainTransferModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    federation_gateway.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_fullysigned_transfer(mocker: MockerFixture, network, generate_uint256, generate_coinbase_transaction):
    txid = generate_uint256
    data = [{
        'depositAmount': 5,
        'depositId': generate_uint256,
        'depositHeight': 5,
        'transferStatus': CrossChainTransferStatus.FullySigned,
        'tx': generate_coinbase_transaction(txid)
    }]
    mocker.patch.object(FederationGateway, 'get', return_value=data)
    federation_gateway = FederationGateway(network=network, baseuri=mocker.MagicMock())
    response = federation_gateway.fullysigned_transfer(deposit_id=data[0]['depositId'], transaction_id=txid)
    assert response == [CrossChainTransferModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    federation_gateway.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_member_info(mocker: MockerFixture, network, generate_compressed_pubkey):
    data = {
        'asyncLoopState': 'Running: 123 Faulted: 0',
        'consensusHeight': 10,
        'cctsHeight': 10,
        'cctsNextDepositHeight': 110,
        'cctsPartials': 0,
        'cctsSuspended': 0,
        'federationWalletActive': True,
        'federationWalletHeight': 10,
        'nodeVersion': 1,
        'pubKey': generate_compressed_pubkey,
        'federationConnectionState': '1 out of 15',
        'federationMemberConnections': [
            {
                'federationMemberIp': 'http://localhost',
                'isConnected': True,
                'isBanned': False
            }
        ]
    }
    mocker.patch.object(FederationGateway, 'get', return_value=data)
    federation_gateway = FederationGateway(network=network, baseuri=mocker.MagicMock())
    response = federation_gateway.member_info()
    assert response == FederationMemberInfoModel(**data)
    # noinspection PyUnresolvedReferences
    federation_gateway.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_info(mocker: MockerFixture, network, generate_compressed_pubkey, generate_p2sh_address):
    my_pubkey = generate_compressed_pubkey
    data = {
        'active': True,
        'mainchain': True,
        'endpoints': [
            'http://endpoint1',
            'http://endpoint1'
        ],
        'multisigPubKey': my_pubkey,
        'federationMultisigPubKeys': [
            my_pubkey,
            generate_compressed_pubkey,
            generate_compressed_pubkey,
            generate_compressed_pubkey,
            generate_compressed_pubkey,
        ],
        'mining_pubkey': my_pubkey,
        'federationMiningPubKeys': [
            my_pubkey,
            generate_compressed_pubkey,
            generate_compressed_pubkey,
            generate_compressed_pubkey,
            generate_compressed_pubkey,
        ],
        'multisigAddress': generate_p2sh_address(network=network),
        'multisigRedeemScript': 'redeem script here',
        'multisigRedeemScriptPaymentScript': 'redeem script payment script here',
        'minconfsmalldeposits': 5,
        'minconfnormaldeposits': 20,
        'minconflargedeposits': 100,
        'minconfdistributiondeposits': 100
    }
    mocker.patch.object(FederationGateway, 'get', return_value=data)
    federation_gateway = FederationGateway(network=network, baseuri=mocker.MagicMock())
    response = federation_gateway.info()
    assert response == FederationGatewayInfoModel(**data)
    # noinspection PyUnresolvedReferences
    federation_gateway.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_ip_add(mocker: MockerFixture, network):
    data = 'http://localhost has been added.'
    mocker.patch.object(FederationGateway, 'put', return_value=data)
    federation_gateway = FederationGateway(network=network, baseuri=mocker.MagicMock())
    response = federation_gateway.ip_add(ipaddr='http://localhost')
    assert response == data
    # noinspection PyUnresolvedReferences
    federation_gateway.put.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_ip_remove(mocker: MockerFixture, network):
    data = 'http://localhost has been removed.'
    mocker.patch.object(FederationGateway, 'put', return_value=data)
    federation_gateway = FederationGateway(network=network, baseuri=mocker.MagicMock())
    response = federation_gateway.ip_remove(ipaddr='http://localhost')
    assert response == data
    # noinspection PyUnresolvedReferences
    federation_gateway.put.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_ip_replace(mocker: MockerFixture, network):
    data = 'http://localhost has been replaced with http://newhost.'
    mocker.patch.object(FederationGateway, 'put', return_value=data)
    federation_gateway = FederationGateway(network=network, baseuri=mocker.MagicMock())
    response = federation_gateway.ip_replace(ipaddrtouse='http://newhost', ipaddr='http://localhost')
    assert response == data
    # noinspection PyUnresolvedReferences
    federation_gateway.put.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_verify_transfer(mocker: MockerFixture, network, generate_uint256):
    data = {
        'isValid': True,
        'errors': []
    }
    mocker.patch.object(FederationGateway, 'get', return_value=data)
    federation_gateway = FederationGateway(network=network, baseuri=mocker.MagicMock())
    response = federation_gateway.verify_transfer(deposit_id_transaction_id=generate_uint256)
    assert response == ValidateTransactionResultModel(**data)
    # noinspection PyUnresolvedReferences
    federation_gateway.get.assert_called_once()
