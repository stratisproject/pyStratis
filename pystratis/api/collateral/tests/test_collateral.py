import pytest
from pytest_mock import MockerFixture
from pystratis.api.collateral.responsemodels import *
from pystratis.api.collateral import Collateral
from pystratis.core.networks import StraxMain


@pytest.mark.parametrize('strax_network', [StraxMain()], ids=['Main'])
def test_join_federation(mocker: MockerFixture, strax_network, generate_p2pkh_address, generate_compressed_pubkey):
    data = {'MinerPublicKey': generate_compressed_pubkey}
    mocker.patch.object(Collateral, 'post', return_value=data)
    collateral = Collateral(network=strax_network, baseuri=mocker.MagicMock())
    response = collateral.join_federation(
        collateral_address=generate_p2pkh_address(network=strax_network),
        collateral_wallet_name='Test_InterfluxStrax_Wallet',
        collateral_wallet_password='cirrus_password',
        wallet_name='Test_InterfluxCirrus_Wallet',
        wallet_account='account 0',
        wallet_password='cirrus_password'
    )

    assert response == JoinFederationResponseModel(**data)
    # noinspection PyUnresolvedReferences
    collateral.post.assert_called_once()
