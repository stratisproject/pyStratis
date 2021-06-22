import pytest
from api.multisig.requestmodels import *
from api.multisig.responsemodels import *
from pybitcoin.types import Address, Money
from pybitcoin import Recipient, MultisigSecret
from pybitcoin.networks import StraxRegTest


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_build_transaction(interflux_strax_node, generate_p2pkh_address):
    request_model = BuildTransactionRequest(
        recipients=[
            Recipient(
                destination_address=Address(address=generate_p2pkh_address(network=StraxRegTest()), network=StraxRegTest()),
                subtraction_fee_from_amount=True,
                amount=Money(5)
            )
        ],
        secrets=[MultisigSecret(mnemonic='mnemonic', passphrase='passphrase')]
    )

    response = interflux_strax_node.multisig.build_transaction(request_model)
    assert isinstance(response, BuildTransactionModel)
