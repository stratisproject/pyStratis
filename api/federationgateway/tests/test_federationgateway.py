import pytest
from pytest_mock import MockerFixture
from api.federationgateway import FederationGateway
from api.federationgateway.requestmodels import *
from api.federationgateway.responsemodels import *
from pybitcoin import DestinationChain, DepositRetrievalType
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
    data = {
        'value': [{
            'Deposits': [
                {
                    'id': generate_uint256,
                    'amount': 10,
                    'TargetAddress': generate_p2pkh_address(network=StraxMain()),
                    'TargetChain': DestinationChain.STRAX.value,
                    'BlockNumber': 10,
                    'BlockHash': generate_uint256,
                    'RetrievalType': DepositRetrievalType.Small.value
                }
            ],
            'BlockInfo': {
                'BlockHash': generate_uint256,
                'BlockHeight': 10,
                'BlockTime': 1
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


def test_pending_transfer():
    # TODO
    pass


def test_fullysigned_transfer():
    # TODO
    pass


def test_member_info():
    # TODO
    pass


def test_info():
    # TODO
    pass


def test_ip_add():
    # TODO
    pass


def test_ip_remove():
    # TODO
    pass


def test_ip_replace():
    # TODO
    pass


def test_verify_transfer():
    # TODO
    pass
