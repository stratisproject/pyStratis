import pytest
from pytest_mock import MockerFixture
from api.federationgateway import FederationGateway
from api.federationgateway.requestmodels import *
from api.federationgateway.responsemodels import *
from pybitcoin import CrossChainTransferStatus, DepositRetrievalType
from pybitcoin.networks import StraxMain, CirrusMain


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if FederationGateway.route + '/' in endpoint:
            assert endpoint in FederationGateway.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if FederationGateway.route + '/' in endpoint:
            assert endpoint in FederationGateway.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if FederationGateway.route + '/' in endpoint:
            assert endpoint in FederationGateway.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if FederationGateway.route + '/' in endpoint:
            assert endpoint in FederationGateway.endpoints


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_deposits(mocker: MockerFixture, network, fakeuri, generate_uint256, generate_p2pkh_address):
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
    federation_gateway = FederationGateway(network=network, baseuri=fakeuri)
    request_model = DepositsRequest(
        block_height=5
    )

    response = federation_gateway.deposits(request_model)
    assert response == [MaturedBlockDepositsModel(**x) for x in data['value']]
    # noinspection PyUnresolvedReferences
    federation_gateway.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_pending_transfer(mocker: MockerFixture, network, fakeuri, generate_uint256, generate_coinbase_transaction):
    txid = generate_uint256
    data = [{
        'depositAmount': 5,
        'depositId': generate_uint256,
        'depositHeight': 5,
        'transferStatus': CrossChainTransferStatus.Partial,
        'tx': generate_coinbase_transaction(txid)
    }]
    mocker.patch.object(FederationGateway, 'get', return_value=data)
    federation_gateway = FederationGateway(network=network, baseuri=fakeuri)
    request_model = PendingTransferRequest(
        deposit_id=data[0]['depositId'],
        transaction_id=txid
    )

    response = federation_gateway.pending_transfer(request_model)
    assert response == [CrossChainTransferModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    federation_gateway.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_fullysigned_transfer(mocker: MockerFixture, network, fakeuri, generate_uint256, generate_coinbase_transaction):
    txid = generate_uint256
    data = [{
        'depositAmount': 5,
        'depositId': generate_uint256,
        'depositHeight': 5,
        'transferStatus': CrossChainTransferStatus.FullySigned,
        'tx': generate_coinbase_transaction(txid)
    }]
    mocker.patch.object(FederationGateway, 'get', return_value=data)
    federation_gateway = FederationGateway(network=network, baseuri=fakeuri)
    request_model = FullySignedTransferRequest(
        deposit_id=data[0]['depositId'],
        transaction_id=txid
    )

    response = federation_gateway.fullysigned_transfer(request_model)
    assert response == [CrossChainTransferModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    federation_gateway.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_member_info(mocker: MockerFixture, network, fakeuri, generate_compressed_pubkey):
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
    federation_gateway = FederationGateway(network=network, baseuri=fakeuri)

    response = federation_gateway.member_info()

    assert response == FederationMemberInfoModel(**data)
    # noinspection PyUnresolvedReferences
    federation_gateway.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_info(mocker: MockerFixture, network, fakeuri, generate_compressed_pubkey, generate_p2sh_address):
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
    federation_gateway = FederationGateway(network=network, baseuri=fakeuri)

    response = federation_gateway.info()

    assert response == FederationGatewayInfoModel(**data)
    # noinspection PyUnresolvedReferences
    federation_gateway.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_ip_add(mocker: MockerFixture, network, fakeuri):
    data = 'http://localhost has been added.'
    mocker.patch.object(FederationGateway, 'put', return_value=data)
    federation_gateway = FederationGateway(network=network, baseuri=fakeuri)
    request_model = MemberIPAddRequest(
        endpoint='http://localhost'
    )

    response = federation_gateway.ip_add(request_model)

    assert response == data
    # noinspection PyUnresolvedReferences
    federation_gateway.put.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_ip_remove(mocker: MockerFixture, network, fakeuri):
    data = 'http://localhost has been removed.'
    mocker.patch.object(FederationGateway, 'put', return_value=data)
    federation_gateway = FederationGateway(network=network, baseuri=fakeuri)
    request_model = MemberIPRemoveRequest(
        endpoint='http://localhost'
    )

    response = federation_gateway.ip_remove(request_model)

    assert response == data
    # noinspection PyUnresolvedReferences
    federation_gateway.put.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_ip_replace(mocker: MockerFixture, network, fakeuri):
    data = 'http://localhost has been replaced with http://newhost.'
    mocker.patch.object(FederationGateway, 'put', return_value=data)
    federation_gateway = FederationGateway(network=network, baseuri=fakeuri)
    request_model = MemberIPReplaceRequest(
        endpointtouse='http://newhost',
        endpoint='http://localhost'
    )

    response = federation_gateway.ip_replace(request_model)

    assert response == data
    # noinspection PyUnresolvedReferences
    federation_gateway.put.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_verify_transfer(mocker: MockerFixture, network, fakeuri, generate_uint256):
    data = {
        'isValid': True,
        'errors': []
    }
    mocker.patch.object(FederationGateway, 'get', return_value=data)
    federation_gateway = FederationGateway(network=network, baseuri=fakeuri)
    request_model = VerifyTransferRequest(
        deposit_id_transaction_id=generate_uint256
    )

    response = federation_gateway.verify_transfer(request_model)

    assert response == ValidateTransactionResultModel(**data)
    # noinspection PyUnresolvedReferences
    federation_gateway.get.assert_called_once()
