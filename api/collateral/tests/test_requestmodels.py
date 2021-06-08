import pytest
import json
from api.collateral.requestmodels import *
from pybitcoin.networks import StraxMain, CirrusMain
from pybitcoin.types import Address


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_joinfederationrequest(network, generate_p2pkh_address):
    data = {
        'collateralAddress': generate_p2pkh_address(network=network),
        'collateralWalletName': 'CollateralTest',
        'collateralWalletPassword': 'password',
        'walletPassword': 'password',
        'walletName': 'Test',
        'walletAccount': 'account 0'
    }
    request_model = JoinFederationRequest(
        collateral_address=Address(address=data['collateralAddress'], network=network),
        collateral_wallet_name='CollateralTest',
        collateral_wallet_password='password',
        wallet_password='password',
        wallet_name='Test',
        wallet_account='account 0'
    )
    assert json.dumps(data) == request_model.json()
