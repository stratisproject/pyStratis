import pytest
from pytest_mock import MockerFixture
from pystratis.api.multisig import Multisig
from pystratis.api.multisig.responsemodels import *
from pystratis.core.networks import StraxMain, CirrusMain
from pystratis.core import MultisigSecret, Recipient
from pystratis.core.types import Address, Money


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_build_transaction(mocker: MockerFixture, network, generate_p2pkh_address, generate_p2sh_address, generate_hexstring, generate_uint256):
    data = {
        'fee': 1,
        'hex': generate_hexstring(128),
        'transactionId': generate_uint256
    }
    mocker.patch.object(Multisig, 'post', return_value=data)
    multisig = Multisig(network=network, baseuri=mocker.MagicMock())
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
