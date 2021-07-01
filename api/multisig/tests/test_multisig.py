import pytest
from pytest_mock import MockerFixture
from api.multisig import Multisig
from api.multisig.requestmodels import *
from api.multisig.responsemodels import *
from pybitcoin.networks import StraxMain, CirrusMain
from pybitcoin import MultisigSecret, Recipient
from pybitcoin.types import Address, Money


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths']]
    for endpoint in paths:
        if Multisig.route + '/' in endpoint:
            assert endpoint in Multisig.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths']]
    for endpoint in paths:
        if Multisig.route + '/' in endpoint:
            assert endpoint in Multisig.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths']]
    for endpoint in paths:
        if Multisig.route + '/' in endpoint:
            assert endpoint in Multisig.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths']]
    for endpoint in paths:
        if Multisig.route + '/' in endpoint:
            assert endpoint in Multisig.endpoints


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_build_transaction(mocker: MockerFixture, network, generate_p2pkh_address, generate_p2sh_address, generate_hexstring, generate_uint256):
    data = {
        'fee': 1,
        'hex': generate_hexstring(128),
        'transactionId': generate_uint256
    }
    mocker.patch.object(Multisig, 'post', return_value=data)
    multisig = Multisig(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())
    response = multisig.build_transaction(
        recipients=[
            Recipient(
                destination_address=Address(address=generate_p2pkh_address(network=network), network=network),
                destination_script=Address(address=generate_p2sh_address(network=network), network=network),
                subtraction_fee_from_amount=True,
                amount=Money(5)
            )
        ],
        secrets=[MultisigSecret(mnemonic='mnemonic', passphrase='passphrase')]
    )

    assert response == BuildTransactionModel(**data)
    # noinspection PyUnresolvedReferences
    multisig.post.assert_called_once()
