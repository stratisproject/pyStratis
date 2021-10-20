import pytest
from pytest_mock import MockerFixture
from pystratis.api.collateralvoting import CollateralVoting
from pystratis.core.types import Address
from pystratis.core.networks import StraxMain


@pytest.mark.parametrize('network', [StraxMain()], ids=['Main'])
def test_join_federation(mocker: MockerFixture, network, generate_p2pkh_address, generate_compressed_pubkey):
    mocker.patch.object(CollateralVoting, 'post', return_value=None)
    collateralvoting = CollateralVoting(network=network, baseuri=mocker.MagicMock())
    collateralvoting.schedulevote_kickfedmember(
        pubkey_hex=generate_compressed_pubkey,
        collateral_amount_satoshis=100000,
        collateral_mainchain_address=Address(address=generate_p2pkh_address(network=network), network=network)
    )

    # noinspection PyUnresolvedReferences
    collateralvoting.post.assert_called_once()
