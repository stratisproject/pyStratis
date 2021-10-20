import pytest
from pytest_mock import MockerFixture
from pystratis.api.interop import Interop
from pystratis.api.interop.responsemodels import *
from pystratis.core.networks import CirrusMain, StraxMain
from pystratis.core import ConversionRequestStatus, ConversionRequestType, DestinationChain
from pystratis.core import PubKey
from pystratis.core.types import uint256, hexstr, Money


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_status_burns(mocker: MockerFixture, network, generate_uint256, generate_compressed_pubkey, generate_p2pkh_address):
    data = {
        'burnRequests': [
            {
                'requestId': generate_uint256,
                'requestType': ConversionRequestType.Burn,
                'requestStatus': ConversionRequestStatus.Processed,
                'blockHeight': 5,
                'destinationAddress': generate_p2pkh_address(network=network),
                'destinationChain': DestinationChain.STRAX,
                'amount': 500000,
                'processed': True
            }
        ],
        'mintRequests': None,
        'receivedVotes': None
    }
    mocker.patch.object(Interop, 'get', return_value=data)
    interop = Interop(network=network, baseuri=mocker.MagicMock())

    response = interop.status_burns()

    assert response == [ConversionRequestModel(**x) for x in data['burnRequests']]
    # noinspection PyUnresolvedReferences
    interop.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_status_mints(mocker: MockerFixture, network, generate_uint256, generate_compressed_pubkey,
                      generate_ethereum_checksum_address, generate_p2pkh_address):
    data = {
        'mintRequests': [
            {
                'requestId': generate_uint256,
                'requestType': ConversionRequestType.Mint,
                'requestStatus': ConversionRequestStatus.Processed,
                'blockHeight': 5,
                'destinationAddress': generate_ethereum_checksum_address,
                'destinationChain': DestinationChain.ETH,
                'amount': 5000000,
                'processed': True
            }
        ],
        'burnRequests': None,
        'receivedVotes': None
    }
    mocker.patch.object(Interop, 'get', return_value=data)
    interop = Interop(network=network, baseuri=mocker.MagicMock())

    response = interop.status_mints()

    assert response == [ConversionRequestModel(**x) for x in data['mintRequests']]
    # noinspection PyUnresolvedReferences
    interop.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_status_votes(mocker: MockerFixture, network, generate_uint256, generate_compressed_pubkey):
    data = {
        'burnRequests': None,
        'mintRequests': None,
        'receivedVotes': {
            generate_uint256: [
                generate_compressed_pubkey,
                generate_compressed_pubkey
            ]
        }
    }

    mocker.patch.object(Interop, 'get', return_value=data)
    interop = Interop(network=network, baseuri=mocker.MagicMock())

    response = interop.status_votes()

    assert isinstance(response, dict)
    for k in response:
        for pubkey in response[k]:
            assert isinstance(pubkey, PubKey)
    # noinspection PyUnresolvedReferences
    interop.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_owners(mocker: MockerFixture, network, generate_p2pkh_address):
    data = [
        generate_p2pkh_address(network=network),
        generate_p2pkh_address(network=network),
        generate_p2pkh_address(network=network)
    ]

    mocker.patch.object(Interop, 'get', return_value=data)
    interop = Interop(network=network, baseuri=mocker.MagicMock())

    response = interop.owners(
        destination_chain=DestinationChain.ETH
    )

    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, str)
    # noinspection PyUnresolvedReferences
    interop.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_addowner(mocker: MockerFixture, network, generate_uint256, generate_p2pkh_address):
    data = generate_uint256

    mocker.patch.object(Interop, 'get', return_value=data)
    interop = Interop(network=network, baseuri=mocker.MagicMock())

    response = interop.add_owner(
        destination_chain=DestinationChain.ETH,
        new_owner_address=generate_p2pkh_address(network=network),
        gas_price=100
    )

    assert isinstance(response, uint256)

    # noinspection PyUnresolvedReferences
    interop.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_removeowner(mocker: MockerFixture, network, generate_uint256, generate_p2pkh_address):
    data = generate_uint256

    mocker.patch.object(Interop, 'get', return_value=data)
    interop = Interop(network=network, baseuri=mocker.MagicMock())

    response = interop.remove_owner(
        destination_chain=DestinationChain.ETH,
        existing_owner_address=generate_p2pkh_address(network=network),
        gas_price=100
    )

    assert isinstance(response, uint256)

    # noinspection PyUnresolvedReferences
    interop.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_confirmtransaction(mocker: MockerFixture, network, generate_uint256):
    data = generate_uint256

    mocker.patch.object(Interop, 'get', return_value=data)
    interop = Interop(network=network, baseuri=mocker.MagicMock())

    response = interop.confirm_transaction(
        destination_chain=DestinationChain.ETH,
        transaction_id=1,
        gas_price=100
    )

    assert isinstance(response, uint256)

    # noinspection PyUnresolvedReferences
    interop.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_changerequirement(mocker: MockerFixture, network, generate_uint256):
    data = generate_uint256

    mocker.patch.object(Interop, 'get', return_value=data)
    interop = Interop(network=network, baseuri=mocker.MagicMock())

    response = interop.change_requirement(
        destination_chain=DestinationChain.ETH,
        requirement=1,
        gas_price=100
    )

    assert isinstance(response, uint256)

    # noinspection PyUnresolvedReferences
    interop.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_multisigtransaction(mocker: MockerFixture, network, generate_hexstring):
    data = {
        'data': generate_hexstring(128),
        'destination': 1,
        'value': 350.3,
        'executed': True
    }

    mocker.patch.object(Interop, 'get', return_value=data)
    interop = Interop(network=network, baseuri=mocker.MagicMock())

    response = interop.multisig_transaction(
        destination_chain=DestinationChain.ETH,
        transaction_id=1,
        raw=False
    )

    assert response == TransactionResponseModel(**data)

    # noinspection PyUnresolvedReferences
    interop.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_multisigtransaction_raw(mocker: MockerFixture, network, generate_hexstring):
    data = generate_hexstring(128)

    mocker.patch.object(Interop, 'get', return_value=data)
    interop = Interop(network=network, baseuri=mocker.MagicMock())

    response = interop.multisig_transaction(
        destination_chain=DestinationChain.ETH,
        transaction_id=1,
        raw=True
    )

    assert isinstance(response, hexstr)

    # noinspection PyUnresolvedReferences
    interop.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_multisigconfirmations(mocker: MockerFixture, network, generate_compressed_pubkey):
    data = [
        generate_compressed_pubkey,
        generate_compressed_pubkey
    ]

    mocker.patch.object(Interop, 'get', return_value=data)
    interop = Interop(network=network, baseuri=mocker.MagicMock())

    response = interop.multisig_confirmations(
        destination_chain=DestinationChain.ETH,
        transaction_id=1
    )

    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, str)

    # noinspection PyUnresolvedReferences
    interop.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_balance(mocker: MockerFixture, network, generate_p2pkh_address):
    data = 350.3

    mocker.patch.object(Interop, 'get', return_value=data)
    interop = Interop(network=network, baseuri=mocker.MagicMock())

    response = interop.balance(
        destination_chain=DestinationChain.ETH,
        account=generate_p2pkh_address(network=StraxMain())
    )

    assert isinstance(response, Money)
    assert response == Money(data)

    # noinspection PyUnresolvedReferences
    interop.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_requests_delete(mocker: MockerFixture, network):
    data = "message"

    mocker.patch.object(Interop, 'delete', return_value=data)
    interop = Interop(network=network, baseuri=mocker.MagicMock())

    response = interop.requests_delete()

    assert isinstance(response, str)

    # noinspection PyUnresolvedReferences
    interop.delete.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_requests_setoriginator(mocker: MockerFixture, network):
    data = "message"

    mocker.patch.object(Interop, 'post', return_value=data)
    interop = Interop(network=network, baseuri=mocker.MagicMock())

    response = interop.requests_setoriginator(
        request_id=1
    )

    assert isinstance(response, str)

    # noinspection PyUnresolvedReferences
    interop.post.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_requests_setnotoriginator(mocker: MockerFixture, network):
    data = "message"

    mocker.patch.object(Interop, 'post', return_value=data)
    interop = Interop(network=network, baseuri=mocker.MagicMock())

    response = interop.requests_setnotoriginator(
        request_id=1
    )

    assert isinstance(response, str)

    # noinspection PyUnresolvedReferences
    interop.post.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_requests_reprocess_burn(mocker: MockerFixture, network):
    data = "message"

    mocker.patch.object(Interop, 'post', return_value=data)
    interop = Interop(network=network, baseuri=mocker.MagicMock())

    response = interop.requests_reprocess_burn(
        request_id=1,
        height=1
    )

    assert isinstance(response, str)

    # noinspection PyUnresolvedReferences
    interop.post.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_requests_pushvote(mocker: MockerFixture, network):
    data = "message"

    mocker.patch.object(Interop, 'post', return_value=data)
    interop = Interop(network=network, baseuri=mocker.MagicMock())

    response = interop.requests_pushvote(
        request_id=1,
        vote_id=1
    )

    assert isinstance(response, str)

    # noinspection PyUnresolvedReferences
    interop.post.assert_called_once()
