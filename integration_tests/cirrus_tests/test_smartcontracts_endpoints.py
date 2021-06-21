import pytest
from nodes import CirrusMinerNode
from api.smartcontracts.requestmodels import *
from api.smartcontracts.responsemodels import *
from api.smartcontractwallet.requestmodels import SendTransactionRequest
from pybitcoin.networks import CirrusRegTest
from pybitcoin import SmartContractParameter, SmartContractParameterType, Recipient
from pybitcoin.types import Address, Money, uint32, uint64, uint128, uint256, int32, int64


@pytest.mark.order(13)
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_code(cirrusminer_node: CirrusMinerNode, get_smart_contract_address):
    request_model = CodeRequest(address=get_smart_contract_address)
    response = cirrusminer_node.smart_contracts.code(request_model)
    assert isinstance(response, GetCodeModel)


@pytest.mark.order(4)
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_balance(cirrusminer_node: CirrusMinerNode, get_smart_contract_address):
    request_model = BalanceRequest(address=get_smart_contract_address)
    response = cirrusminer_node.smart_contracts.balance(request_model)
    assert isinstance(response, Money)


@pytest.mark.order(12)
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_storage(cirrusminer_node: CirrusMinerNode, get_smart_contract_address, get_node_address_with_balance):
    sending_address = get_node_address_with_balance(cirrusminer_node)
    request_model = StorageRequest(
        contract_address=get_smart_contract_address,
        storage_key='TestBool',
        data_type=1
    )
    response = cirrusminer_node.smart_contracts.storage(request_model)
    assert isinstance(response, bool)
    assert response

    request_model = StorageRequest(
        contract_address=get_smart_contract_address,
        storage_key='TestByte',
        data_type=2
    )
    response = cirrusminer_node.smart_contracts.storage(request_model)
    assert isinstance(response, bytes)
    assert response == b'\xff'

    request_model = StorageRequest(
        contract_address=get_smart_contract_address,
        storage_key='TestChar',
        data_type=3
    )
    response = cirrusminer_node.smart_contracts.storage(request_model)
    assert isinstance(response, str)
    assert response == 'c'

    request_model = StorageRequest(
        contract_address=get_smart_contract_address,
        storage_key='TestString',
        data_type=4
    )
    response = cirrusminer_node.smart_contracts.storage(request_model)
    assert isinstance(response, str)
    assert response == 'Stratis'

    request_model = StorageRequest(
        contract_address=get_smart_contract_address,
        storage_key='TestUInt32',
        data_type=5
    )
    response = cirrusminer_node.smart_contracts.storage(request_model)
    assert isinstance(response, uint32)
    assert response == uint32(123)

    request_model = StorageRequest(
        contract_address=get_smart_contract_address,
        storage_key='TestInt32',
        data_type=6
    )
    response = cirrusminer_node.smart_contracts.storage(request_model)
    assert isinstance(response, int32)
    assert response == int32(-123)

    request_model = StorageRequest(
        contract_address=get_smart_contract_address,
        storage_key='TestUInt64',
        data_type=7
    )
    response = cirrusminer_node.smart_contracts.storage(request_model)
    assert isinstance(response, uint64)
    assert response == uint64(456)

    request_model = StorageRequest(
        contract_address=get_smart_contract_address,
        storage_key='TestInt64',
        data_type=8
    )
    response = cirrusminer_node.smart_contracts.storage(request_model)
    assert isinstance(response, int64)
    assert response == int64(-456)

    request_model = StorageRequest(
        contract_address=get_smart_contract_address,
        storage_key='TestAddress',
        data_type=9
    )
    response = cirrusminer_node.smart_contracts.storage(request_model)
    assert isinstance(response, Address)
    assert response == sending_address

    request_model = StorageRequest(
        contract_address=get_smart_contract_address,
        storage_key='TestByteArray',
        data_type=10
    )
    response = cirrusminer_node.smart_contracts.storage(request_model)
    assert isinstance(response, bytearray)
    assert response == bytearray(b'\x04\xa6\xb9')

    request_model = StorageRequest(
        contract_address=get_smart_contract_address,
        storage_key='TestUInt128',
        data_type=11
    )
    response = cirrusminer_node.smart_contracts.storage(request_model)
    assert isinstance(response, uint128)
    assert response == uint128(789)

    request_model = StorageRequest(
        contract_address=get_smart_contract_address,
        storage_key='TestUInt256',
        data_type=12
    )
    response = cirrusminer_node.smart_contracts.storage(request_model)
    assert isinstance(response, uint256)
    assert response == uint256(987)


@pytest.mark.order(10)
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_receipt(cirrusminer_node: CirrusMinerNode, get_contract_create_trxid):
    request_model = ReceiptRequest(tx_hash=get_contract_create_trxid)
    response = cirrusminer_node.smart_contracts.receipt(request_model)
    assert isinstance(response, ReceiptModel)


@pytest.mark.order(11)
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_receipt_search(cirrusminer_node: CirrusMinerNode, get_smart_contract_address):
    request_model = ReceiptSearchRequest(
        contract_address=get_smart_contract_address,
        event_name='TestMessageLog',
        topics=[],
        from_block=10,
        to_block=1000
    )
    response = cirrusminer_node.smart_contracts.receipt_search(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, ReceiptModel)


@pytest.mark.order(5)
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_build_create(cirrusminer_node: CirrusMinerNode, get_node_address_with_balance, apitestcontract_bytecode):
    sending_address = get_node_address_with_balance(cirrusminer_node)
    request_model = BuildCreateContractTransactionRequest(
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
            SmartContractParameter(value_type=SmartContractParameterType.UInt256, value=uint256(987)),
        ]
    )

    response = cirrusminer_node.smart_contracts.build_create(request_model)
    assert isinstance(response, BuildContractTransactionModel)
    # send the transaction to remove the utxo reservation
    request_model = SendTransactionRequest(hex=response.hex)
    cirrusminer_node.smart_contract_wallet.send_transaction(request_model)


@pytest.mark.order(6)
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_build_call(cirrusminer_node: CirrusMinerNode, get_node_address_with_balance, get_smart_contract_address):
    sending_address = get_node_address_with_balance(cirrusminer_node)
    request_model = BuildCallContractTransactionRequest(
        wallet_name='Test',
        account_name='account 0',
        outpoints=None,
        contract_address=get_smart_contract_address,
        method_name='TestMethod',
        amount=Money(0),
        fee_amount=Money(0.0001),
        password='password',
        gas_price=1000,
        gas_limit=250000,
        sender=sending_address,
        parameters=[
            SmartContractParameter(value_type=SmartContractParameterType.Int32, value=int32(0)),
            SmartContractParameter(value_type=SmartContractParameterType.String, value='SmartContracts made easy.'),
        ]
    )
    response = cirrusminer_node.smart_contracts.build_call(request_model)
    assert isinstance(response, BuildContractTransactionModel)
    # send the transaction to remove the utxo reservation
    request_model = SendTransactionRequest(hex=response.hex)
    cirrusminer_node.smart_contract_wallet.send_transaction(request_model)


@pytest.mark.order(3)
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_build_transaction(cirrusminer_node: CirrusMinerNode, get_node_address_with_balance, generate_p2pkh_address):
    sending_address = get_node_address_with_balance(cirrusminer_node)
    request_model = BuildTransactionRequest(
        sender=sending_address,
        fee_amount=Money(0.0001),
        password='password',
        segwit_change_address=False,
        wallet_name='Test',
        account_name='account 0',
        outpoints=None,
        recipients=[
            Recipient(
                destination_address=Address(address=generate_p2pkh_address(network=CirrusRegTest()), network=CirrusRegTest()),
                subtraction_fee_from_amount=True,
                amount=Money(10)
            )
        ],
        op_return_data='opreturn',
        op_return_amount=Money(0.00000001),
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=sending_address
    )
    response = cirrusminer_node.smart_contracts.build_transaction(request_model)
    assert isinstance(response, BuildContractTransactionModel)
    # Send the transaction to remove the utxo reservation
    request_model = SendTransactionRequest(hex=response.hex)
    cirrusminer_node.smart_contract_wallet.send_transaction(request_model)


@pytest.mark.order(2)
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_estimate_fee(cirrusminer_node: CirrusMinerNode, get_node_address_with_balance, generate_p2pkh_address):
    sending_address = get_node_address_with_balance(cirrusminer_node)
    request_model = EstimateFeeRequest(
        sender=sending_address,
        wallet_name='Test',
        account_name='account 0',
        outpoints=None,
        recipients=[
            Recipient(
                destination_address=Address(address=generate_p2pkh_address(network=CirrusRegTest()), network=CirrusRegTest()),
                subtraction_fee_from_amount=True,
                amount=Money(10)
            )
        ],
        op_return_data='opreturn',
        op_return_amount=Money(0.00000001),
        fee_type='low',
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=sending_address
    )

    response = cirrusminer_node.smart_contracts.estimate_fee(request_model)
    assert isinstance(response, Money)


@pytest.mark.order(7)
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_build_and_send_create(cirrusminer_node: CirrusMinerNode, get_node_address_with_balance,
                               apitestcontract_bytecode):
    sending_address = get_node_address_with_balance(cirrusminer_node)
    request_model = BuildAndSendCreateContractTransactionRequest(
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

    response = cirrusminer_node.smart_contracts.build_and_send_create(request_model)
    assert isinstance(response, BuildContractTransactionModel)
    # Send the transaction to remove the utxo reservation
    request_model = SendTransactionRequest(hex=response.hex)
    cirrusminer_node.smart_contract_wallet.send_transaction(request_model)


@pytest.mark.order(9)
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_build_and_send_call(cirrusminer_node: CirrusMinerNode, get_node_address_with_balance, get_smart_contract_address):
    sending_address = get_node_address_with_balance(cirrusminer_node)
    request_model = BuildAndSendCallContractTransactionRequest(
        wallet_name='Test',
        account_name='account 0',
        outpoints=None,
        contract_address=get_smart_contract_address,
        method_name='TestMethod',
        amount=Money(0),
        fee_amount=Money(0.0001),
        password='password',
        gas_price=1000,
        gas_limit=250000,
        sender=sending_address,
        parameters=[
            SmartContractParameter(value_type=SmartContractParameterType.Int32, value=int32(0)),
            SmartContractParameter(value_type=SmartContractParameterType.String, value='SmartContracts made easy.')
        ]
    )

    response = cirrusminer_node.smart_contracts.build_and_send_call(request_model)
    assert isinstance(response, BuildContractTransactionModel)
    # send the transaction to remove the utxo reservation
    request_model = SendTransactionRequest(hex=response.hex)
    cirrusminer_node.smart_contract_wallet.send_transaction(request_model)


@pytest.mark.order(8)
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_local_call(cirrusminer_node: CirrusMinerNode, get_node_address_with_balance, get_smart_contract_address):
    sending_address = get_node_address_with_balance(cirrusminer_node)
    request_model = LocalCallContractTransactionRequest(
        contract_address=get_smart_contract_address,
        method_name='TestMethod',
        amount=Money(0),
        gas_price=100,
        gas_limit=250000,
        sender=sending_address,
        parameters=[
            SmartContractParameter(value_type=SmartContractParameterType.Int32, value=int32(0)),
            SmartContractParameter(value_type=SmartContractParameterType.String, value='SmartContracts made easy.')
        ]
    )

    response = cirrusminer_node.smart_contracts.local_call(request_model)
    assert isinstance(response, LocalExecutionResultModel)


@pytest.mark.order(1)
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_address_balances(cirrusminer_node: CirrusMinerNode):
    request_model = BalancesRequest(wallet_name='Test')
    response = cirrusminer_node.smart_contracts.address_balances(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, AddressBalanceModel)
