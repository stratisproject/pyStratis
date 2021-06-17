import pytest
from api.smartcontractwallet.requestmodels import *
from api.smartcontractwallet.responsemodels import *
from pybitcoin.types import Address, Money, uint256
from pybitcoin.networks import CirrusRegTest
from nodes import CirrusMinerNode


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_account_addresses(cirrusminer_node: CirrusMinerNode):
    request_model = AccountAddressesRequest(wallet_name='Test')
    response = cirrusminer_node.smart_contract_wallet.account_addresses(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, Address)


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_address_balance(cirrusminer_node: CirrusMinerNode):
    request_model = AddressBalanceRequest(address=Address(address=generate_p2pkh_address(network=network), network=CirrusRegTest()))
    response = cirrusminer_node.smart_contract_wallet.address_balance(request_model)
    assert isinstance(response, Money)


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_history(cirrusminer_node: CirrusMinerNode):
    request_model = HistoryRequest(
        wallet_name='Test',
        address=Address(address=generate_p2pkh_address(network=network), network=CirrusRegTest()),
        skip=2,
        take=2
    )

    response = cirrusminer_node.smart_contract_wallet.history(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, ContractTransactionItemModel)


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_create(cirrusminer_node: CirrusMinerNode):
    request_model = CreateContractTransactionRequest(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=generate_uint256, index=0)],
        amount=Money(5),
        fee_amount=Money(0.0001),
        password='password',
        contract_code='codegoeshere',
        gas_price=Money(0.0001),
        gas_limit=Money(0.001),
        sender=Address(address=generate_p2pkh_address(network=network), network=network),
        parameters=[
            SmartContractParameter(value_type=SmartContractParameterType.Boolean, value=True),
            SmartContractParameter(value_type=SmartContractParameterType.Byte, value=b'\xff'),
            SmartContractParameter(value_type=SmartContractParameterType.Char, value='c'),
            SmartContractParameter(value_type=SmartContractParameterType.String, value='Stratis'),
            SmartContractParameter(value_type=SmartContractParameterType.UInt32, value=uint32(123)),
            SmartContractParameter(value_type=SmartContractParameterType.Int32, value=int32(-123)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt64, value=uint64(456)),
            SmartContractParameter(value_type=SmartContractParameterType.Int64, value=int64(-456)),
            SmartContractParameter(value_type=SmartContractParameterType.Address,
                                   value=Address(address=generate_p2pkh_address(network=network), network=network)),
            SmartContractParameter(value_type=SmartContractParameterType.ByteArray, value=bytearray(b'\x04\xa6\xb9')),
            SmartContractParameter(value_type=SmartContractParameterType.UInt128, value=uint128(789)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt256, value=uint256(987)),
        ]
    )

    response = cirrusminer_node.smart_contract_wallet.create(request_model)
    assert isinstance(response, uint256)


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_call(cirrusminer_node: CirrusMinerNode):
    request_model = CallContractTransactionRequest(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=generate_uint256, index=0)],
        contract_address=Address(address=generate_p2pkh_address(network=network), network=network),
        method_name='method',
        amount=Money(5),
        fee_amount=Money(0.0001),
        password='password',
        gas_price=Money(0.0001),
        gas_limit=Money(0.001),
        sender=Address(address=generate_p2pkh_address(network=network), network=network),
        parameters=[
            SmartContractParameter(value_type=SmartContractParameterType.Boolean, value=True),
            SmartContractParameter(value_type=SmartContractParameterType.Byte, value=b'\xff'),
            SmartContractParameter(value_type=SmartContractParameterType.Char, value='c'),
            SmartContractParameter(value_type=SmartContractParameterType.String, value='Stratis'),
            SmartContractParameter(value_type=SmartContractParameterType.UInt32, value=uint32(123)),
            SmartContractParameter(value_type=SmartContractParameterType.Int32, value=int32(-123)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt64, value=uint64(456)),
            SmartContractParameter(value_type=SmartContractParameterType.Int64, value=int64(-456)),
            SmartContractParameter(value_type=SmartContractParameterType.Address,
                                   value=Address(address=generate_p2pkh_address(network=network), network=network)),
            SmartContractParameter(value_type=SmartContractParameterType.ByteArray, value=bytearray(b'\x04\xa6\xb9')),
            SmartContractParameter(value_type=SmartContractParameterType.UInt128, value=uint128(789)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt256, value=uint256(987)),
        ]
    )

    response = cirrusminer_node.smart_contract_wallet.call(request_model)
    assert isinstance(response, BuildContractTransactionModel)


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_send_transaction(cirrusminer_node: CirrusMinerNode):
    request_model = SendTransactionRequest()

    response = cirrusminer_node.smart_contract_wallet.send_transaction(request_model)
    assert isinstance(response, WalletSendTransactionModel)
