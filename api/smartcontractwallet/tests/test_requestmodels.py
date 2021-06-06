import pytest
import json
from pybitcoin import Address, Outpoint, SmartContractParameter, SmartContractParameterType
from pybitcoin.types import Money, uint32, uint64, uint128, uint256, int32, int64
from api.smartcontractwallet.requestmodels import *
from pybitcoin.networks import StraxMain, CirrusMain


def test_accountaddressesrequest():
    data = {
        'walletName': 'Test'
    }
    request_model = AccountAddressesRequest(
        wallet_name='Test'
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_addressbalancerequest(network, generate_p2pkh_address):
    data = {
        'address': generate_p2pkh_address(network=network)
    }
    request_model = AddressBalanceRequest(
        address=Address(address=data['address'], network=network)
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_callcontracttransactionrequest(network, generate_uint256, generate_p2pkh_address):
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
        'amount': 5,
        'feeAmount': 1,
        'password': 'password',
        'gasPrice': 1,
        'gasLimit': 10,
        'sender': generate_p2pkh_address(network=network),
        'parameters': ['1#true', '2#255', '3#c', '4#Stratis', '5#123', '6#-123',
                       '7#456', '8#-456', f'9#{parameter_address}', '10#04A6B9', '11#789', '12#987']

    }
    request_model = CallContractTransactionRequest(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=data['outpoints'][0]['transactionId'], index=0)],
        contract_address=Address(address=data['contractAddress'], network=network),
        method_name='method',
        amount=Money(5),
        fee_amount=Money(1),
        password='password',
        gas_price=Money(1),
        gas_limit=Money(10),
        sender=Address(address=data['sender'], network=network),
        parameters=[
            SmartContractParameter(type=SmartContractParameterType.Boolean, value=True),
            SmartContractParameter(type=SmartContractParameterType.Byte, value=b'\xff'),
            SmartContractParameter(type=SmartContractParameterType.Char, value='c'),
            SmartContractParameter(type=SmartContractParameterType.String, value='Stratis'),
            SmartContractParameter(type=SmartContractParameterType.UInt32, value=uint32(123)),
            SmartContractParameter(type=SmartContractParameterType.Int32, value=int32(-123)),
            SmartContractParameter(type=SmartContractParameterType.UInt64, value=uint64(456)),
            SmartContractParameter(type=SmartContractParameterType.Int64, value=int64(-456)),
            SmartContractParameter(type=SmartContractParameterType.Address, value=Address(address=parameter_address, network=network)),
            SmartContractParameter(type=SmartContractParameterType.ByteArray, value=bytearray(b'\x04\xa6\xb9')),
            SmartContractParameter(type=SmartContractParameterType.UInt128, value=uint128(789)),
            SmartContractParameter(type=SmartContractParameterType.UInt256, value=uint256(987)),
        ]
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_createtransactionrequest(network, generate_p2pkh_address, generate_uint256):
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
        'amount': 5,
        'feeAmount': 1,
        'password': 'password',
        'contractCode': 'codegoeshere',
        'gasPrice': 1,
        'gasLimit': 10,
        'sender': generate_p2pkh_address(network=network),
        'parameters': ['1#true', '2#255', '3#c', '4#Stratis', '5#123', '6#-123',
                       '7#456', '8#-456', f'9#{parameter_address}', '10#04A6B9', '11#789', '12#987']

    }
    request_model = CreateContractTransactionRequest(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=data['outpoints'][0]['transactionId'], index=0)],
        amount=Money(5),
        fee_amount=Money(1),
        password='password',
        contract_code='codegoeshere',
        gas_price=Money(1),
        gas_limit=Money(10),
        sender=Address(address=data['sender'], network=network),
        parameters=[
            SmartContractParameter(type=SmartContractParameterType.Boolean, value=True),
            SmartContractParameter(type=SmartContractParameterType.Byte, value=b'\xff'),
            SmartContractParameter(type=SmartContractParameterType.Char, value='c'),
            SmartContractParameter(type=SmartContractParameterType.String, value='Stratis'),
            SmartContractParameter(type=SmartContractParameterType.UInt32, value=uint32(123)),
            SmartContractParameter(type=SmartContractParameterType.Int32, value=int32(-123)),
            SmartContractParameter(type=SmartContractParameterType.UInt64, value=uint64(456)),
            SmartContractParameter(type=SmartContractParameterType.Int64, value=int64(-456)),
            SmartContractParameter(type=SmartContractParameterType.Address, value=Address(address=parameter_address, network=network)),
            SmartContractParameter(type=SmartContractParameterType.ByteArray, value=bytearray(b'\x04\xa6\xb9')),
            SmartContractParameter(type=SmartContractParameterType.UInt128, value=uint128(789)),
            SmartContractParameter(type=SmartContractParameterType.UInt256, value=uint256(987)),
        ]
    )
    assert json.dumps(data) == request_model.json()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_historyrequest(network, generate_p2pkh_address):
    data = {
        'WalletName': 'Test',
        'address': generate_p2pkh_address(network=network),
        'Skip': 2,
        'Take': 2
    }
    request_model = HistoryRequest(
        wallet_name='Test',
        address=Address(address=data['address'], network=network),
        skip=2,
        take=2
    )
    assert json.dumps(data) == request_model.json()
