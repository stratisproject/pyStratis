import pytest
from pystratis.api.smartcontractwallet.responsemodels import *
from pystratis.core import SmartContractParameter, SmartContractParameterType
from pystratis.core.types import Address, Money, uint32, uint64, uint128, uint256, int32, int64
from pystratis.nodes import CirrusMinerNode


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_account_addresses(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.smart_contract_wallet.account_addresses(wallet_name='Test')
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, Address)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_address_balance(cirrusminer_node: CirrusMinerNode, get_node_smart_contract_address):
    sc_address = get_node_smart_contract_address(cirrusminer_node)
    response = cirrusminer_node.smart_contract_wallet.address_balance(address=sc_address)
    assert isinstance(response, Money)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_history(cirrusminer_node: CirrusMinerNode, get_smart_contract_address):
    sc_address = get_smart_contract_address
    response = cirrusminer_node.smart_contract_wallet.history(
        wallet_name='Test',
        address=sc_address
    )
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, ContractTransactionItemModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_create(cirrusminer_node: CirrusMinerNode, apitestcontract_bytecode, get_node_address_with_balance):
    sending_address = get_node_address_with_balance(cirrusminer_node)
    response = cirrusminer_node.smart_contract_wallet.create(
        wallet_name='Test',
        account_name='account 0',
        outpoints=None,
        amount=Money(0),
        fee_amount=Money(0.0001),
        password='password',
        contract_code=apitestcontract_bytecode,
        gas_price=1000,
        gas_limit=250000,
        sender=sending_address,
        parameters=[
            SmartContractParameter(value_type=SmartContractParameterType.Boolean, value=True),
            SmartContractParameter(value_type=SmartContractParameterType.Byte, value=b'\xff'),
            SmartContractParameter(value_type=SmartContractParameterType.Char, value='c'),
            SmartContractParameter(value_type=SmartContractParameterType.String, value='Stratis'),
            SmartContractParameter(value_type=SmartContractParameterType.UInt32, value=uint32(123)),
            SmartContractParameter(value_type=SmartContractParameterType.Int32, value=int32(-123)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt64, value=uint64(456)),
            SmartContractParameter(value_type=SmartContractParameterType.Int64, value=int64(-456)),
            SmartContractParameter(value_type=SmartContractParameterType.Address, value=sending_address),
            SmartContractParameter(value_type=SmartContractParameterType.ByteArray, value=bytearray(b'\x04\xa6\xb9')),
            SmartContractParameter(value_type=SmartContractParameterType.UInt128, value=uint128(789)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt256, value=uint256(987))
        ]
    )
    assert isinstance(response, uint256)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_call(cirrusminer_node: CirrusMinerNode, get_node_address_with_balance, get_smart_contract_address):
    sending_address = get_node_address_with_balance(cirrusminer_node)
    sc_address = get_smart_contract_address
    response = cirrusminer_node.smart_contract_wallet.call(
        wallet_name='Test',
        account_name='account 0',
        outpoints=None,
        contract_address=sc_address,
        method_name='TestMethod',
        amount=Money(0),
        fee_amount=Money(0.0001),
        password='password',
        gas_price=1000,
        gas_limit=250000,
        sender=sending_address,
        parameters=[
            SmartContractParameter(value_type=SmartContractParameterType.Boolean, value=True),
            SmartContractParameter(value_type=SmartContractParameterType.Byte, value=b'\xff'),
            SmartContractParameter(value_type=SmartContractParameterType.Char, value='c'),
            SmartContractParameter(value_type=SmartContractParameterType.String, value='Stratis'),
            SmartContractParameter(value_type=SmartContractParameterType.UInt32, value=uint32(123)),
            SmartContractParameter(value_type=SmartContractParameterType.Int32, value=int32(-123)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt64, value=uint64(456)),
            SmartContractParameter(value_type=SmartContractParameterType.Int64, value=int64(-456)),
            SmartContractParameter(value_type=SmartContractParameterType.Address, value=sending_address),
            SmartContractParameter(value_type=SmartContractParameterType.ByteArray, value=bytearray(b'\x04\xa6\xb9')),
            SmartContractParameter(value_type=SmartContractParameterType.UInt128, value=uint128(789)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt256, value=uint256(987))
        ]
    )
    assert isinstance(response, BuildContractTransactionModel)
    # send the transaction to remove the utxo reservation
    cirrusminer_node.smart_contract_wallet.send_transaction(transaction_hex=response.hex)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_send_transaction(cirrusminer_node: CirrusMinerNode, get_node_address_with_balance, get_smart_contract_address):
    sending_address = get_node_address_with_balance(cirrusminer_node)
    sc_address = get_smart_contract_address
    response = cirrusminer_node.smart_contract_wallet.call(
        wallet_name='Test',
        account_name='account 0',
        outpoints=None,
        contract_address=sc_address,
        method_name='TestMethod',
        amount=Money(0),
        fee_amount=Money(0.0001),
        password='password',
        gas_price=1000,
        gas_limit=250000,
        sender=sending_address,
        parameters=[
            SmartContractParameter(value_type=SmartContractParameterType.Boolean, value=True),
            SmartContractParameter(value_type=SmartContractParameterType.Byte, value=b'\xff'),
            SmartContractParameter(value_type=SmartContractParameterType.Char, value='c'),
            SmartContractParameter(value_type=SmartContractParameterType.String, value='Stratis'),
            SmartContractParameter(value_type=SmartContractParameterType.UInt32, value=uint32(123)),
            SmartContractParameter(value_type=SmartContractParameterType.Int32, value=int32(-123)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt64, value=uint64(456)),
            SmartContractParameter(value_type=SmartContractParameterType.Int64, value=int64(-456)),
            SmartContractParameter(value_type=SmartContractParameterType.Address, value=sending_address),
            SmartContractParameter(value_type=SmartContractParameterType.ByteArray, value=bytearray(b'\x04\xa6\xb9')),
            SmartContractParameter(value_type=SmartContractParameterType.UInt128, value=uint128(789)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt256, value=uint256(987))
        ]
    )
    response = cirrusminer_node.smart_contract_wallet.send_transaction(transaction_hex=response.hex)
    assert isinstance(response, WalletSendTransactionModel)
