import pytest
from pystratis.nodes import CirrusMinerNode
from pystratis.core.types import uint256, hexstr
from pystratis.api.contract_swagger.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_address(cirrusminer_node: CirrusMinerNode, get_smart_contract_address):
    sc_address = get_smart_contract_address
    response = cirrusminer_node.contract_swagger.address(address=sc_address)
    assert isinstance(response, OpenAPISchemaModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_call(cirrusminer_node: CirrusMinerNode, get_smart_contract_address):
    sc_address = get_smart_contract_address
    cirrusminer_node.contract_swagger(address=sc_address)

