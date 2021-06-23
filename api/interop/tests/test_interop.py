import pytest
from pytest_mock import MockerFixture
from api.interop import Interop
from api.interop.responsemodels import *
from pybitcoin.networks import StraxMain, CirrusMain
from pybitcoin import ConversionRequestStatus, ConversionRequestType


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths']]
    for endpoint in paths:
        if Interop.route + '/' in endpoint:
            assert endpoint in Interop.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths']]
    for endpoint in paths:
        if Interop.route + '/' in endpoint:
            assert endpoint in Interop.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths']]
    for endpoint in paths:
        if Interop.route + '/' in endpoint:
            assert endpoint in Interop.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths']]
    for endpoint in paths:
        if Interop.route + '/' in endpoint:
            assert endpoint in Interop.endpoints


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_status(mocker: MockerFixture, network, fakeuri, generate_uint256, generate_compressed_pubkey,
                generate_ethereum_checksum_address, generate_p2pkh_address):
    data = {
        'mintRequests': [
            {
                'requestId': generate_uint256,
                'requestType': ConversionRequestType.Mint,
                'requestStatus': ConversionRequestStatus.Processed,
                'blockHeight': 5,
                'destinationAddress': generate_ethereum_checksum_address,
                'amount': 5000000,
                'processed': True
            }
        ],
        'burnRequests': [
            {
                'requestId': generate_uint256,
                'requestType': ConversionRequestType.Burn,
                'requestStatus': ConversionRequestStatus.Processed,
                'blockHeight': 5,
                'destinationAddress': generate_p2pkh_address(network=network),
                'amount': 500000,
                'processed': True
            }
        ],
        'receivedVotes': {
            generate_uint256: [
                generate_compressed_pubkey,
                generate_compressed_pubkey
            ]
        }
    }
    mocker.patch.object(Interop, 'get', return_value=data)
    interop = Interop(network=network, baseuri=fakeuri)

    response = interop.status()

    assert response == StatusModel(**data)
    # noinspection PyUnresolvedReferences
    interop.get.assert_called_once()
