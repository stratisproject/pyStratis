import pytest
import json
from api.smartcontracts.requestmodels import *
from pybitcoin import Outpoint, Recipient, SmartContractParameter, SmartContractParameterType
from pybitcoin.types import Address, Money, uint32, uint64, uint128, uint256, int32, int64
from pybitcoin.networks import StraxMain, CirrusMain


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_balancerequest(network, generate_p2pkh_address):
    data = {
        'address': generate_p2pkh_address(network=network)
    }
    request_model = BalanceRequest(
        address=Address(address=data['address'], network=network)
    )
    assert json.dumps(data) == request_model.json()


def test_balancesrequest():
    data = {
        'walletName': 'Test'
    }
    request_model = BalancesRequest(
        wallet_name='Test'
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_buildandsendcallrequest(network, generate_p2pkh_address, generate_uint256):
    parameter_address = generate_p2pkh_address(network=network)
    data = {
        'walletName': 'Test',
        'accountName': 'account 0',
        'outpoints': [
            {
                'transactionId': generate_uint256,
                'index': 0
            }
        ],
        'contractAddress': generate_p2pkh_address(network=network),
        'methodName': 'method',
        'amount': '5.00000000',
        'feeAmount': '0.00010000',
        'password': 'password',
        'gasPrice': 1000,
        'gasLimit': 250000,
        'sender': generate_p2pkh_address(network=network),
        'parameters': ['1#true', '2#255', '3#c', '4#Stratis', '5#123', '6#-123',
                       '7#456', '8#-456', f'9#{parameter_address}', '10#04A6B9', '11#789', '12#987']
    }
    request_model = BuildAndSendCallContractTransactionRequest(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=data['outpoints'][0]['transactionId'], index=0)],
        contract_address=Address(address=data['contractAddress'], network=network),
        method_name='method',
        amount=Money(5),
        fee_amount=Money(0.0001),
        password='password',
        gas_price=1000,
        gas_limit=250000,
        sender=Address(address=data['sender'], network=network),
        parameters=[
            SmartContractParameter(value_type=SmartContractParameterType.Boolean, value=True),
            SmartContractParameter(value_type=SmartContractParameterType.Byte, value=b'\xff'),
            SmartContractParameter(value_type=SmartContractParameterType.Char, value='c'),
            SmartContractParameter(value_type=SmartContractParameterType.String, value='Stratis'),
            SmartContractParameter(value_type=SmartContractParameterType.UInt32, value=uint32(123)),
            SmartContractParameter(value_type=SmartContractParameterType.Int32, value=int32(-123)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt64, value=uint64(456)),
            SmartContractParameter(value_type=SmartContractParameterType.Int64, value=int64(-456)),
            SmartContractParameter(value_type=SmartContractParameterType.Address, value=Address(address=parameter_address, network=network)),
            SmartContractParameter(value_type=SmartContractParameterType.ByteArray, value=bytearray(b'\x04\xa6\xb9')),
            SmartContractParameter(value_type=SmartContractParameterType.UInt128, value=uint128(789)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt256, value=uint256(987))
        ]
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_buildandsendcreaterequest(network, generate_p2pkh_address, generate_uint256, generate_hexstring):
    parameter_address = generate_p2pkh_address(network=network)
    mock_code = generate_hexstring(128)
    data = {
        'walletName': 'Test',
        'accountName': 'account 0',
        'outpoints': [
            {
                'transactionId': generate_uint256,
                'index': 0
            }
        ],
        'amount': '5.00000000',
        'feeAmount': '0.00010000',
        'password': 'password',
        'contractCode': mock_code,
        'gasPrice': 1000,
        'gasLimit': 250000,
        'sender': generate_p2pkh_address(network=network),
        'parameters': ['1#true', '2#255', '3#c', '4#Stratis', '5#123', '6#-123',
                       '7#456', '8#-456', f'9#{parameter_address}', '10#04A6B9', '11#789', '12#987']
    }
    request_model = BuildAndSendCreateContractTransactionRequest(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=data['outpoints'][0]['transactionId'], index=0)],
        amount=Money(5),
        fee_amount=Money(0.0001),
        password='password',
        contract_code=mock_code,
        gas_price=1000,
        gas_limit=250000,
        sender=Address(address=data['sender'], network=network),
        parameters=[
            SmartContractParameter(value_type=SmartContractParameterType.Boolean, value=True),
            SmartContractParameter(value_type=SmartContractParameterType.Byte, value=b'\xff'),
            SmartContractParameter(value_type=SmartContractParameterType.Char, value='c'),
            SmartContractParameter(value_type=SmartContractParameterType.String, value='Stratis'),
            SmartContractParameter(value_type=SmartContractParameterType.UInt32, value=uint32(123)),
            SmartContractParameter(value_type=SmartContractParameterType.Int32, value=int32(-123)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt64, value=uint64(456)),
            SmartContractParameter(value_type=SmartContractParameterType.Int64, value=int64(-456)),
            SmartContractParameter(value_type=SmartContractParameterType.Address, value=Address(address=parameter_address, network=network)),
            SmartContractParameter(value_type=SmartContractParameterType.ByteArray, value=bytearray(b'\x04\xa6\xb9')),
            SmartContractParameter(value_type=SmartContractParameterType.UInt128, value=uint128(789)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt256, value=uint256(987))
        ]
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_buildcallcontracttransactionrequest(network, generate_p2pkh_address, generate_uint256):
    parameter_address = generate_p2pkh_address(network=network)
    contract_address = generate_p2pkh_address(network=network)
    data = {
        'walletName': 'Test',
        'accountName': 'account 0',
        'outpoints': [
            {
                'transactionId': generate_uint256,
                'index': 0
            }
        ],
        'contractAddress': contract_address,
        'methodName': 'method',
        'amount': '5.00000000',
        'feeAmount': '0.00010000',
        'password': 'password',
        'gasPrice': 1000,
        'gasLimit': 250000,
        'sender': generate_p2pkh_address(network=network),
        'parameters': ['1#true', '2#255', '3#c', '4#Stratis', '5#123', '6#-123',
                       '7#456', '8#-456', f'9#{parameter_address}', '10#04A6B9', '11#789', '12#987']
    }
    request_model = BuildCallContractTransactionRequest(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=data['outpoints'][0]['transactionId'], index=0)],
        contract_address=Address(address=contract_address, network=network),
        method_name='method',
        amount=Money(5),
        fee_amount=Money(0.0001),
        password='password',
        gas_price=1000,
        gas_limit=250000,
        sender=Address(address=data['sender'], network=network),
        parameters=[
            SmartContractParameter(value_type=SmartContractParameterType.Boolean, value=True),
            SmartContractParameter(value_type=SmartContractParameterType.Byte, value=b'\xff'),
            SmartContractParameter(value_type=SmartContractParameterType.Char, value='c'),
            SmartContractParameter(value_type=SmartContractParameterType.String, value='Stratis'),
            SmartContractParameter(value_type=SmartContractParameterType.UInt32, value=uint32(123)),
            SmartContractParameter(value_type=SmartContractParameterType.Int32, value=int32(-123)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt64, value=uint64(456)),
            SmartContractParameter(value_type=SmartContractParameterType.Int64, value=int64(-456)),
            SmartContractParameter(value_type=SmartContractParameterType.Address, value=Address(address=parameter_address, network=network)),
            SmartContractParameter(value_type=SmartContractParameterType.ByteArray, value=bytearray(b'\x04\xa6\xb9')),
            SmartContractParameter(value_type=SmartContractParameterType.UInt128, value=uint128(789)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt256, value=uint256(987))
        ]
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_buildcreatecontracttransactionrequest(network, generate_p2pkh_address, generate_uint256, generate_hexstring):
    parameter_address = generate_p2pkh_address(network=network)
    byte_code = generate_hexstring(128)
    data = {
        'walletName': 'Test',
        'accountName': 'account 0',
        'outpoints': [
            {
                'transactionId': generate_uint256,
                'index': 0
            }
        ],
        'amount': '5.00000000',
        'feeAmount': '0.00010000',
        'password': 'password',
        'contractCode': byte_code,
        'gasPrice': 1000,
        'gasLimit': 250000,
        'sender': generate_p2pkh_address(network=network),
        'parameters': ['1#true', '2#255', '3#c', '4#Stratis', '5#123', '6#-123',
                       '7#456', '8#-456', f'9#{parameter_address}', '10#04A6B9', '11#789', '12#987']
    }
    request_model = BuildCreateContractTransactionRequest(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=data['outpoints'][0]['transactionId'], index=0)],
        amount=Money(5),
        fee_amount=Money(0.0001),
        password='password',
        contract_code=byte_code,
        gas_price=1000,
        gas_limit=250000,
        sender=Address(address=data['sender'], network=network),
        parameters=[
            SmartContractParameter(value_type=SmartContractParameterType.Boolean, value=True),
            SmartContractParameter(value_type=SmartContractParameterType.Byte, value=b'\xff'),
            SmartContractParameter(value_type=SmartContractParameterType.Char, value='c'),
            SmartContractParameter(value_type=SmartContractParameterType.String, value='Stratis'),
            SmartContractParameter(value_type=SmartContractParameterType.UInt32, value=uint32(123)),
            SmartContractParameter(value_type=SmartContractParameterType.Int32, value=int32(-123)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt64, value=uint64(456)),
            SmartContractParameter(value_type=SmartContractParameterType.Int64, value=int64(-456)),
            SmartContractParameter(value_type=SmartContractParameterType.Address, value=Address(address=parameter_address, network=network)),
            SmartContractParameter(value_type=SmartContractParameterType.ByteArray, value=bytearray(b'\x04\xa6\xb9')),
            SmartContractParameter(value_type=SmartContractParameterType.UInt128, value=uint128(789)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt256, value=uint256(987))
        ]
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_buildtransactionrequest(network, generate_p2pkh_address, generate_p2sh_address, generate_uint256):
    data = {
        'sender': generate_p2pkh_address(network=network),
        'feeAmount': '0.00010000',
        'password': 'password',
        'segwitChangeAddress': False,
        'walletName': 'Test',
        'accountName': 'account 0',
        'outpoints': [
            {
                'transactionId': generate_uint256,
                'index': 0
            }
        ],
        'recipients': [
            {
                'destinationAddress': generate_p2pkh_address(network=network),
                'destinationScript': generate_p2sh_address(network=network),
                'subtractFeeFromAmount': True,
                'amount': '10.00000000'
            }
        ],
        'opReturnData': 'opreturn',
        'opReturnAmount': '0.00000001',
        'allowUnconfirmed': True,
        'shuffleOutputs': True,
        'changeAddress': generate_p2pkh_address(network=network)
    }
    request_model = BuildTransactionRequest(
        sender=Address(address=data['sender'], network=network),
        fee_amount=Money(0.0001),
        password='password',
        segwit_change_address=False,
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=data['outpoints'][0]['transactionId'], index=0)],
        recipients=[
            Recipient(
                destination_address=Address(address=data['recipients'][0]['destinationAddress'], network=network),
                destination_script=Address(address=data['recipients'][0]['destinationScript'], network=network),
                subtraction_fee_from_amount=True,
                amount=Money(10)
            )
        ],
        op_return_data='opreturn',
        op_return_amount=Money(0.00000001),
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=Address(address=data['changeAddress'], network=network)
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_coderequest(network, generate_p2pkh_address):
    data = {
        'address': generate_p2pkh_address(network=network)
    }
    request_model = CodeRequest(
        address=Address(address=data['address'], network=network)
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_estimatefeerequest(network, generate_p2pkh_address, generate_p2sh_address, generate_uint256):
    data = {
        'sender': generate_p2pkh_address(network=network),
        'walletName': 'Test',
        'accountName': 'account 0',
        'outpoints': [
            {
                'transactionId': generate_uint256,
                'index': 0
            }
        ],
        'recipients': [
            {
                'destinationAddress': generate_p2pkh_address(network=network),
                'destinationScript': generate_p2sh_address(network=network),
                'subtractFeeFromAmount': True,
                'amount': '10.00000000'
            }
        ],
        'opReturnData': 'opreturn',
        'opReturnAmount': '0.00000001',
        'feeType': 'low',
        'allowUnconfirmed': True,
        'shuffleOutputs': True,
        'changeAddress': generate_p2pkh_address(network=network)
    }
    request_model = EstimateFeeRequest(
        sender=Address(address=data['sender'], network=network),
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=data['outpoints'][0]['transactionId'], index=0)],
        recipients=[
            Recipient(
                destination_address=Address(address=data['recipients'][0]['destinationAddress'], network=network),
                destination_script=Address(address=data['recipients'][0]['destinationScript'], network=network),
                subtraction_fee_from_amount=True,
                amount=Money(10)
            )
        ],
        op_return_data='opreturn',
        op_return_amount=Money(0.00000001),
        fee_type='low',
        allow_unconfirmed=True,
        shuffle_outputs=True,
        change_address=Address(address=data['changeAddress'], network=network)
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_localcallrequest(network, generate_p2pkh_address):
    parameter_address = generate_p2pkh_address(network=network)
    data = {
        'contractAddress': generate_p2pkh_address(network=network),
        'methodName': 'method',
        'amount': '10.00000000',
        'gasPrice': 1000,
        'gasLimit': 250000,
        'sender': generate_p2pkh_address(network=network),
        'parameters': ['1#true', '2#255', '3#c', '4#Stratis', '5#123', '6#-123',
                       '7#456', '8#-456', f'9#{parameter_address}', '10#04A6B9', '11#789', '12#987']
    }
    request_model = LocalCallContractTransactionRequest(
        contract_address=Address(address=data['contractAddress'], network=network),
        method_name='method',
        amount=Money(10),
        gas_price=1000,
        gas_limit=250000,
        sender=Address(address=data['sender'], network=network),
        parameters=[
            SmartContractParameter(value_type=SmartContractParameterType.Boolean, value=True),
            SmartContractParameter(value_type=SmartContractParameterType.Byte, value=b'\xff'),
            SmartContractParameter(value_type=SmartContractParameterType.Char, value='c'),
            SmartContractParameter(value_type=SmartContractParameterType.String, value='Stratis'),
            SmartContractParameter(value_type=SmartContractParameterType.UInt32, value=uint32(123)),
            SmartContractParameter(value_type=SmartContractParameterType.Int32, value=int32(-123)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt64, value=uint64(456)),
            SmartContractParameter(value_type=SmartContractParameterType.Int64, value=int64(-456)),
            SmartContractParameter(value_type=SmartContractParameterType.Address, value=Address(address=parameter_address, network=network)),
            SmartContractParameter(value_type=SmartContractParameterType.ByteArray, value=bytearray(b'\x04\xa6\xb9')),
            SmartContractParameter(value_type=SmartContractParameterType.UInt128, value=uint128(789)),
            SmartContractParameter(value_type=SmartContractParameterType.UInt256, value=uint256(987))
        ]
    )
    assert json.dumps(data) == request_model.json()


def test_receiptrequest(generate_uint256):
    data = {
        'txHash': generate_uint256
    }
    request_model = ReceiptRequest(
        tx_hash=data['txHash']
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_receiptsearchrequest(network, generate_p2pkh_address):
    data = {
        'ContractAddress': generate_p2pkh_address(network=network),
        'eventName': 'event',
        'topics': ['topic0', 'topic1'],
        'fromBlock': 10,
        'toBlock': 15
    }
    request_model = ReceiptSearchRequest(
        contract_address=Address(address=data['ContractAddress'], network=network),
        event_name='event',
        topics=['topic0', 'topic1'],
        from_block=10,
        to_block=15
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_storagerequest(network, generate_p2pkh_address):
    data = {
        'ContractAddress': generate_p2pkh_address(network=network),
        'StorageKey': 'key',
        'DataType': 1
    }
    request_model = StorageRequest(
        contract_address=Address(address=data['ContractAddress'], network=network),
        storage_key='key',
        data_type=1
    )
    assert json.dumps(data) == request_model.json()
