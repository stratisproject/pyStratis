import pytest
from pytest_mock import MockerFixture
from pystratis.core.networks import CirrusMain
from pystratis.api.dynamic_contract import DynamicContract
from pystratis.api.dynamic_contract.responsemodels import *


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_property(mocker: MockerFixture, network, generate_p2pkh_address, generate_hexstring):
    sc_address = generate_p2pkh_address(network=network)
    default_sender = generate_p2pkh_address(network=network)
    data = {
        'internalTransfers': [
            {
                'from': generate_p2pkh_address(network=network),
                'to': generate_p2pkh_address(network=network),
                'value': 5
            }
        ],
        'gasConsumed': {'value': 1500},
        'revert': False,
        'errorMessage': "{'value': 'Error Message.'}",
        'return': "{'key': 'value'}",
        'logs': [
            {
                'address': generate_p2pkh_address(network=network),
                'topics': [
                    generate_hexstring(32)
                ],
                'data': generate_hexstring(32)
            }
        ]
    }
    mocker.patch.object(DynamicContract, 'get', return_value=data)
    dynamic_contract = DynamicContract(network=network, baseuri=mocker.MagicMock())

    response = dynamic_contract.property(
        address=sc_address,
        property='property',
        wallet_name='Test',
        wallet_password='password',
        sender=default_sender
    )

    assert response == LocalExecutionResultModel(**data)
    # noinspection PyUnresolvedReferences
    dynamic_contract.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_method(mocker: MockerFixture, network, generate_p2pkh_address, generate_hexstring, generate_uint256):
    sc_address = generate_p2pkh_address(network=network)
    default_sender = generate_p2pkh_address(network=network)
    data = {
        'fee': 10000,
        'hex': generate_hexstring(128),
        'message': 'message',
        'success': True,
        'transactionId': generate_uint256
    }

    mocker.patch.object(DynamicContract, 'post', return_value=data)
    dynamic_contract = DynamicContract(network=network, baseuri=mocker.MagicMock())

    response = dynamic_contract.method(
        address=sc_address,
        method='TestMethod',
        data={"data": 'fake_data'},
        wallet_name='Test',
        wallet_password='password',
        sender=default_sender
    )

    assert response == BuildContractTransactionModel(**data)
    # noinspection PyUnresolvedReferences
    dynamic_contract.post.assert_called_once()
