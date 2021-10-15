import pytest
from pytest_mock import MockerFixture
from pystratis.api.interop import Interop
from pystratis.api.interop.responsemodels import *
from pystratis.core.networks import CirrusMain
from pystratis.core import ConversionRequestStatus, ConversionRequestType


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_status(mocker: MockerFixture, network, generate_uint256, generate_compressed_pubkey,
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
    interop = Interop(network=network, baseuri=mocker.MagicMock())

    response = interop.status()

    assert response == StatusModel(**data)
    # noinspection PyUnresolvedReferences
    interop.get.assert_called_once()
