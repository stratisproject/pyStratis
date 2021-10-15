import pytest
from pystratis.nodes import CirrusMinerNode
from pystratis.api.dynamic_contract.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_property(cirrusminer_node: CirrusMinerNode, get_smart_contract_address, get_node_address_with_balance):
    sc_address = get_smart_contract_address
    default_sender = get_node_address_with_balance(cirrusminer_node)
    response = cirrusminer_node.dynamic_contract.property(
        address=sc_address,
        property='Owner',
        wallet_name='Test',
        wallet_password='password',
        sender=default_sender
    )
    assert isinstance(response, LocalExecutionResultModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_method(cirrusminer_node: CirrusMinerNode, get_smart_contract_address, get_node_address_with_balance):
    sc_address = get_smart_contract_address
    default_sender = get_node_address_with_balance(cirrusminer_node)
    response = cirrusminer_node.dynamic_contract.method(
        address=sc_address,
        method='TestMethod',
        data={
            "messageIndex": 0,
            "message": "TestMessage"
        },
        wallet_name='Test',
        wallet_password='password',
        sender=default_sender
    )
    assert isinstance(response, BuildContractTransactionModel)
