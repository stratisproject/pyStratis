import pytest
from nodes import CirrusMinerNode, CirrusNode
from api.smartcontracts.requestmodels import *
from api.smartcontracts.responsemodels import *
from pybitcoin import Outpoint, SmartContractParameter, SmartContractParameterType, Recipient
from pybitcoin.types import Address, Money, uint32, uint64, uint128, uint256, int32, int64, hexstr
from pybitcoin.networks import CirrusRegTest


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_code(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = CodeRequest(
    )

    response = cirrusminer_node.smart_contracts.code(request_model)
    assert isinstance(response, GetCodeModel)
    response = cirrus_syncing_node.smart_contracts.code(request_model)
    assert isinstance(response, GetCodeModel)


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_balance(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = BalanceRequest(

    )

    response = cirrusminer_node.smart_contracts.balance(request_model)
    assert isinstance(response, Money)

    response = cirrus_syncing_node.smart_contracts.balance(request_model)
    assert isinstance(response, Money)


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_storage(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = StorageRequest(
        contract_address=Address(),
        storage_key='key',
        data_type=1
    )

    response = cirrusminer_node.smart_contracts.storage(request_model)
    assert isinstance(response, hexstr)
    response = cirrus_syncing_node.smart_contracts.storage(request_model)
    assert isinstance(response, hexstr)


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_receipt(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = ReceiptRequest(tx_hash=trxid)

    response = cirrusminer_node.smart_contracts.receipt(request_model)
    assert isinstance(response, ReceiptModel)

    response = cirrus_syncing_node.smart_contracts.receipt(request_model)
    assert isinstance(response, ReceiptModel)


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_receipt_search(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = ReceiptSearchRequest(
        contract_address=Address(),
        event_name='event',
        topics=['topic0', 'topic1'],
        from_block=10,
        to_block=15
    )

    response = cirrusminer_node.smart_contracts.receipt_search(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, ReceiptModel)

    response = cirrus_syncing_node.smart_contracts.receipt_search(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, ReceiptModel)


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_build_create(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = BuildCreateContractTransactionRequest(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=generate_uint256, index=0)],
        amount=Money(5),
        fee_amount=Money(0.0001),
        password='password',
        contract_code='codegoeshere',
        gas_price=Money(0.00001),
        gas_limit=Money(0.0001),
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

    response = cirrusminer_node.smart_contracts.build_create(request_model)
    assert isinstance(response, BuildContractTransactionModel)
    response = cirrus_syncing_node.smart_contracts.build_create(request_model)
    assert isinstance(response, BuildContractTransactionModel)


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_build_call(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = BuildCallContractTransactionRequest(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=generate_uint256, index=0)],
        contract_address=Address(address=generate_p2pkh_address(network=network), network=network),
        method_name='method',
        amount=Money(5),
        fee_amount=Money(0.0001),
        password='password',
        gas_price=Money(0.00001),
        gas_limit=Money(0.0001),
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

    response = cirrusminer_node.smart_contracts.build_call(request_model)
    assert isinstance(response, BuildContractTransactionModel)
    response = cirrus_syncing_node.smart_contracts.build_call(request_model)
    assert isinstance(response, BuildContractTransactionModel)


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_build_transaction(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = BuildTransactionRequest(
        sender=Address(address=generate_p2pkh_address(network=network), network=network),
        fee_amount=Money(0.0001),
        password='password',
        segwit_change_address=False,
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=generate_uint256, index=0)],
        recipients=[
            Recipient(
                destination_address=Address(address=generate_p2pkh_address(network=network), network=network),
                destination_script=Address(address=generate_p2pkh_address(network=network), network=network),
                subtraction_fee_from_amount=True,
                amount=Money(10)
            )
        ],
        op_return_data='opreturn',
        op_return_amount=Money(0.00000001),
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=Address(address=generate_p2pkh_address(network=network), network=network)
    )

    response = cirrusminer_node.smart_contracts.build_transaction(request_model)
    assert isinstance(response, BuildContractTransactionModel)
    response = cirrus_syncing_node.smart_contracts.build_transaction(request_model)
    assert isinstance(response, BuildContractTransactionModel)


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_estimate_fee(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = EstimateFeeRequest(
        sender=Address(address=generate_p2pkh_address(network=network), network=network),
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=generate_uint256, index=0)],
        recipients=[
            Recipient(
                destination_address=Address(address=generate_p2pkh_address(network=network), network=network),
                destination_script=Address(address=generate_p2pkh_address(network=network), network=network),
                subtraction_fee_from_amount=True,
                amount=Money(10)
            )
        ],
        op_return_data='opreturn',
        op_return_amount=Money(0.00000001),
        fee_type='low',
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=Address(address=generate_p2pkh_address(network=network), network=network)
    )

    response = cirrusminer_node.smart_contracts.estimate_fee(request_model)
    assert isinstance(response, Money)
    response = cirrus_syncing_node.smart_contracts.estimate_fee(request_model)
    assert isinstance(response, Money)


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_build_and_send_create(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = BuildAndSendCreateContractTransactionRequest(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=generate_uint256, index=0)],
        amount=Money(5),
        fee_amount=Money(0.0001),
        password='password',
        contract_code='codegoeshere',
        gas_price=Money(0.0001),
        gas_limit=Money(0.01),
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

    response = cirrusminer_node.smart_contracts.build_and_send_create(request_model)
    assert isinstance(response, BuildContractTransactionModel)
    response = cirrus_syncing_node.smart_contracts.build_and_send_create(request_model)
    assert isinstance(response, BuildContractTransactionModel)


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_build_and_send_call(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = BuildAndSendCallContractTransactionRequest(
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

    response = cirrusminer_node.smart_contracts.build_and_send_call(request_model)
    assert isinstance(response, BuildContractTransactionModel)
    response = cirrus_syncing_node.smart_contracts.build_and_send_call(request_model)
    assert isinstance(response, BuildContractTransactionModel)


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_local_call(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = LocalCallContractTransactionRequest(
        contract_address=Address(address=generate_p2pkh_address(network=network), network=network),
        method_name='method',
        amount=Money(10),
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

    response = cirrusminer_node.smart_contracts.local_call(request_model)
    assert isinstance(response, LocalExecutionResultModel)

    response = cirrus_syncing_node.smart_contracts.local_call(request_model)
    assert isinstance(response, LocalExecutionResultModel)


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_address_balances(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = BalancesRequest(wallet_name='Test')
    response = cirrusminer_node.smart_contracts.address_balances(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, AddressBalanceModel)

    request_model = BalancesRequest(wallet_name='Test')
    response = cirrus_syncing_node.smart_contracts.address_balances(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, AddressBalanceModel)
