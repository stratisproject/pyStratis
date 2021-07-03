import pytest
from pystratis.nodes import StraxNode
from pystratis.core import WalletSecret
from pystratis.api.staking.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_staking_info(strax_hot_node: StraxNode):
    response = strax_hot_node.staking.get_staking_info()
    assert isinstance(response, GetStakingInfoModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_start_staking(strax_hot_node: StraxNode):
    strax_hot_node.staking.start_staking(name='Test', password='password')


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_start_multistaking(strax_hot_node: StraxNode):
    strax_hot_node.staking.start_multistaking(
        wallet_credentials=[WalletSecret(wallet_name='Test', wallet_password='password')]
    )


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_stop_staking(strax_hot_node: StraxNode):
    strax_hot_node.staking.stop_staking()
