from typing import Union
from nodes import StraxNode, InterfluxStraxNode
from api.staking.requestmodels import *
from pybitcoin import WalletSecret


def check_staking_endpoints(node: Union[StraxNode, InterfluxStraxNode]):
    assert check_get_staking_info(node)
    assert check_start_staking(node)
    assert check_start_multistaking(node)
    assert check_stop_staking(node)


def check_get_staking_info(node: Union[StraxNode, InterfluxStraxNode]) -> bool:
    node.staking.get_staking_info()
    return True


def check_start_staking(node: Union[StraxNode, InterfluxStraxNode]) -> bool:
    request_model = StartStakingRequest(name='Test', password='password')
    node.staking.start_staking(request_model)
    return True


def check_start_multistaking(node: Union[StraxNode, InterfluxStraxNode]) -> bool:
    request_model = StartMultiStakingRequest(
        wallet_credentials=[WalletSecret(wallet_name='Test', wallet_password='password')]
    )
    node.staking.start_multistaking(request_model)
    return True


def check_stop_staking(node: Union[StraxNode, InterfluxStraxNode]):
    request_model = StopStakingRequest()
    node.staking.stop_staking(request_model)
    return True
