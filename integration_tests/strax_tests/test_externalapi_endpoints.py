import pytest
from pystratis.nodes import StraxNode
from pystratis.core.types import Money


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_estimate_conversion_gas(strax_hot_node: StraxNode):
    response = strax_hot_node.externalapi.estimate_conversion_gas()
    assert isinstance(response, int)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_estimate_conversion_fee(strax_hot_node: StraxNode):
    response = strax_hot_node.externalapi.estimate_conversion_fee()
    assert isinstance(response, Money)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_gasprice(strax_hot_node: StraxNode):
    response = strax_hot_node.externalapi.gas_price()
    assert isinstance(response, int)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_stratis_price(strax_hot_node: StraxNode):
    response = strax_hot_node.externalapi.stratis_price()
    assert isinstance(response, Money)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_ethereum_price(strax_hot_node: StraxNode):
    response = strax_hot_node.externalapi.ethereum_price()
    assert isinstance(response, Money)
