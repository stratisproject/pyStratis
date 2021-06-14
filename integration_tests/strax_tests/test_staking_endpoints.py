import pytest
from nodes import StraxNode
from api.staking.requestmodels import *
from api.staking.responsemodels import *
from pybitcoin import WalletSecret


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_staking_info(strax_hot_node: StraxNode):
    response = strax_hot_node.staking.get_staking_info()
    assert isinstance(response, GetStakingInfoModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_start_staking(strax_hot_node: StraxNode):
    request_model = StartStakingRequest(name='Test', password='password')
    strax_hot_node.staking.start_staking(request_model)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_start_multistaking(strax_hot_node: StraxNode):
    request_model = StartMultiStakingRequest(
        wallet_credentials=[WalletSecret(wallet_name='Test', wallet_password='password')]
    )
    strax_hot_node.staking.start_multistaking(request_model)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_stop_staking(strax_hot_node: StraxNode):
    request_model = StopStakingRequest()
    strax_hot_node.staking.stop_staking(request_model)
