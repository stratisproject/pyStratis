import pytest
import json
from api.multisig.requestmodels import *
from pybitcoin.networks import StraxMain, CirrusMain
from pybitcoin import MultisigSecret, Recipient
from pybitcoin.types import Address, Money


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_buildtransactionrequest(network, generate_p2pkh_address, generate_p2sh_address):
    data = {
        'recipients': [
            {
                'destinationAddress': generate_p2pkh_address(network=network),
                'destinationScript': generate_p2sh_address(network=network),
                'subtractFeeFromAmount': True,
                'amount': 5
            }
        ],
        'secrets': [
            {
                'mnemonic': 'mnemonic',
                'passphrase': 'passphrase'
            }
        ]
    }
    request_model = BuildTransactionRequest(
        recipients=[
            Recipient(
                destination_address=Address(address=data['recipients'][0]['destinationAddress'], network=network),
                destination_script=Address(address=data['recipients'][0]['destinationScript'], network=network),
                subtraction_fee_from_amount=True,
                amount=Money(5)
            )
        ],
        secrets=[
            MultisigSecret(
                mnemonic='mnemonic',
                passphrase='passphrase'
            )
        ]
    )
    assert json.dumps(data) == request_model.json()
