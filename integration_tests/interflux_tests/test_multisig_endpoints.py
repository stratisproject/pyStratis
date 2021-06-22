import pytest
from api.multisig.requestmodels import *
from api.multisig.responsemodels import *
from pybitcoin.types import Address, Money
from pybitcoin import Recipient, MultisigSecret


@pytest.mark.skip(reason='WIP')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_build_transaction(interflux_cirrusminer_node):
    request_model = BuildTransactionRequest(
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

    response = interflux_cirrusminer_node.multisig.build_transaction(request_model)
    assert isinstance(response, BuildTransactionModel)
