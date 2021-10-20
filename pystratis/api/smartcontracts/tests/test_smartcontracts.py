import pytest
from pytest_mock import MockerFixture
from pystratis.api.smartcontracts import SmartContracts
from pystratis.api.smartcontracts.responsemodels import *
from pystratis.core import Outpoint, SmartContractParameter, SmartContractParameterType, Recipient
from pystratis.core.types import Address, Money, uint32, uint64, uint128, uint256, int32, int64
from pystratis.core.networks import CirrusMain


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_code(mocker: MockerFixture, network, generate_p2pkh_address):
    data = {
        'type': 'typename',
        'bytecode': 'bytecodestring',
        'csharp': 'csharp code',
        'message': 'message'
    }
    mocker.patch.object(SmartContracts, 'get', return_value=data)
    smart_contracts = SmartContracts(network=network, baseuri=mocker.MagicMock())

    response = smart_contracts.code(address=Address(address=generate_p2pkh_address(network), network=network))

    assert response == GetCodeModel(**data)
    # noinspection PyUnresolvedReferences
    smart_contracts.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_balance(mocker: MockerFixture, network, generate_p2pkh_address):
    data = 1
    mocker.patch.object(SmartContracts, 'get', return_value=data)
    smart_contracts = SmartContracts(network=network, baseuri=mocker.MagicMock())

    response = smart_contracts.balance(address=Address(address=generate_p2pkh_address(network), network=network))

    assert response == Money(data)
    # noinspection PyUnresolvedReferences
    smart_contracts.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_storage(mocker: MockerFixture, network, generate_p2pkh_address, generate_hexstring):
    data = True
    mocker.patch.object(SmartContracts, 'get', return_value=data)
    smart_contracts = SmartContracts(network=network, baseuri=mocker.MagicMock())
    response = smart_contracts.storage(
        contract_address=Address(address=generate_p2pkh_address(network=network), network=network),
        storage_key='key',
        data_type=1
    )

    assert response == data
    # noinspection PyUnresolvedReferences
    smart_contracts.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_receipt(mocker: MockerFixture, network, generate_uint256, generate_hexstring, generate_p2pkh_address):
    trxid = generate_uint256
    data = {
        'transactionHash': trxid,
        'blockHash': generate_uint256,
        'postState': generate_uint256,
        'gasUsed': 10,
        'from': generate_p2pkh_address(network=network),
        'to': generate_p2pkh_address(network=network),
        'newContractAddress': generate_p2pkh_address(network=network),
        'success': True,
        'returnValue': 'result',
        'bloom': generate_hexstring(64),
        'error': '',
        'logs': [
            {
                'address': generate_p2pkh_address(network=network),
                'topics': [
                    generate_hexstring(32)
                ],
                'data': generate_hexstring(32)
            }
        ],
        'blockNumber': 5
    }

    mocker.patch.object(SmartContracts, 'get', return_value=data)
    smart_contracts = SmartContracts(network=network, baseuri=mocker.MagicMock())

    response = smart_contracts.receipt(tx_hash=trxid)

    assert response == ReceiptModel(**data)
    # noinspection PyUnresolvedReferences
    smart_contracts.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_receipt_search(mocker: MockerFixture, network, generate_uint256, generate_p2pkh_address, generate_hexstring):
    data = [{
        'transactionHash': generate_uint256,
        'blockHash': generate_uint256,
        'postState': generate_uint256,
        'gasUsed': 10,
        'from': generate_p2pkh_address(network=network),
        'to': generate_p2pkh_address(network=network),
        'newContractAddress': generate_p2pkh_address(network=network),
        'success': True,
        'returnValue': 'result',
        'bloom': generate_hexstring(64),
        'error': '',
        'logs': [
            {
                'address': generate_p2pkh_address(network=network),
                'topics': [
                    generate_hexstring(32)
                ],
                'data': generate_hexstring(32)
            }
        ],
        'blockNumber': 5
    }]
    mocker.patch.object(SmartContracts, 'get', return_value=data)
    smart_contracts = SmartContracts(network=network, baseuri=mocker.MagicMock())

    response = smart_contracts.receipt_search(
        contract_address=Address(address=generate_p2pkh_address(network=network), network=network),
        event_name='event',
        topics=['topic0', 'topic1'],
        from_block=10,
        to_block=15
    )

    assert response == [ReceiptModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    smart_contracts.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_build_create(mocker: MockerFixture, network, generate_p2pkh_address, generate_hexstring, generate_uint256):
    data = {
        'fee': 10000,
        'hex': generate_hexstring(128),
        'message': 'message',
        'success': True,
        'transactionId': generate_uint256,
        'newContractAddress': generate_p2pkh_address(network=network)
    }
    mocker.patch.object(SmartContracts, 'post', return_value=data)
    smart_contracts = SmartContracts(network=network, baseuri=mocker.MagicMock())

    response = smart_contracts.build_create(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=generate_uint256, index=0)],
        amount=Money(5),
        fee_amount=Money(0.0001),
        password='password',
        contract_code=generate_hexstring(128),
        gas_price=1000,
        gas_limit=250000,
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
            SmartContractParameter(value_type=SmartContractParameterType.UInt256, value=uint256(987))
        ]
    )

    assert response == BuildCreateContractTransactionModel(**data)
    # noinspection PyUnresolvedReferences
    smart_contracts.post.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_build_call(mocker: MockerFixture, network, generate_p2pkh_address, generate_uint256, generate_hexstring):
    data = {
        'fee': 10000,
        'hex': generate_hexstring(128),
        'message': 'message',
        'success': True,
        'transactionId': generate_uint256
    }
    mocker.patch.object(SmartContracts, 'post', return_value=data)
    smart_contracts = SmartContracts(network=network, baseuri=mocker.MagicMock())

    response = smart_contracts.build_call(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=generate_uint256, index=0)],
        contract_address=Address(address=generate_p2pkh_address(network=network), network=network),
        method_name='method',
        amount=Money(5),
        fee_amount=Money(0.0001),
        password='password',
        gas_price=1000,
        gas_limit=250000,
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
            SmartContractParameter(value_type=SmartContractParameterType.UInt256, value=uint256(987))
        ]
    )

    assert response == BuildContractTransactionModel(**data)
    # noinspection PyUnresolvedReferences
    smart_contracts.post.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_build_transaction(mocker: MockerFixture, network, generate_p2pkh_address, generate_hexstring, generate_uint256):
    data = {
        'fee': 10000,
        'hex': generate_hexstring(128),
        'message': 'message',
        'success': True,
        'transactionId': generate_uint256
    }
    mocker.patch.object(SmartContracts, 'post', return_value=data)
    smart_contracts = SmartContracts(network=network, baseuri=mocker.MagicMock())
    response = smart_contracts.build_transaction(
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

    assert response == BuildContractTransactionModel(**data)
    # noinspection PyUnresolvedReferences
    smart_contracts.post.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_estimate_fee(mocker: MockerFixture, network, generate_uint256, generate_p2pkh_address):
    data = 10000
    mocker.patch.object(SmartContracts, 'post', return_value=data)
    smart_contracts = SmartContracts(network=network, baseuri=mocker.MagicMock())

    response = smart_contracts.estimate_fee(
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

    assert response == Money.from_satoshi_units(data)
    # noinspection PyUnresolvedReferences
    smart_contracts.post.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_build_and_send_create(mocker: MockerFixture, network, generate_p2pkh_address, generate_uint256, generate_hexstring):
    data = {
        'fee': 10000,
        'hex': generate_hexstring(128),
        'message': 'message',
        'success': True,
        'transactionId': generate_uint256,
        'newContractAddress': generate_p2pkh_address(network=network)
    }
    mocker.patch.object(SmartContracts, 'post', return_value=data)
    smart_contracts = SmartContracts(network=network, baseuri=mocker.MagicMock())

    response = smart_contracts.build_and_send_create(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=generate_uint256, index=0)],
        amount=Money(5),
        fee_amount=Money(0.0001),
        password='password',
        contract_code=generate_hexstring(128),
        gas_price=1000,
        gas_limit=250000,
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
            SmartContractParameter(value_type=SmartContractParameterType.UInt256, value=uint256(987))
        ]
    )

    assert response == BuildCreateContractTransactionModel(**data)
    # noinspection PyUnresolvedReferences
    smart_contracts.post.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_build_and_send_call(mocker: MockerFixture, network, generate_uint256, generate_p2pkh_address, generate_hexstring):
    data = {
        'fee': 10000,
        'hex': generate_hexstring(128),
        'message': 'message',
        'success': True,
        'transactionId': generate_uint256
    }
    mocker.patch.object(SmartContracts, 'post', return_value=data)
    smart_contracts = SmartContracts(network=network, baseuri=mocker.MagicMock())

    response = smart_contracts.build_and_send_call(
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=generate_uint256, index=0)],
        contract_address=Address(address=generate_p2pkh_address(network=network), network=network),
        method_name='method',
        amount=Money(5),
        fee_amount=Money(0.0001),
        password='password',
        gas_price=1000,
        gas_limit=250000,
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
            SmartContractParameter(value_type=SmartContractParameterType.UInt256, value=uint256(987))
        ]
    )

    assert response == BuildContractTransactionModel(**data)
    # noinspection PyUnresolvedReferences
    smart_contracts.post.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_local_call(mocker: MockerFixture, network, generate_p2pkh_address, generate_hexstring):
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

    mocker.patch.object(SmartContracts, 'post', return_value=data)
    smart_contracts = SmartContracts(network=network, baseuri=mocker.MagicMock())
    response = smart_contracts.local_call(
        contract_address=Address(address=generate_p2pkh_address(network=network), network=network),
        method_name='method',
        amount=Money(10),
        gas_price=1000,
        gas_limit=250000,
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
            SmartContractParameter(value_type=SmartContractParameterType.UInt256, value=uint256(987))
        ]
    )

    assert response == LocalExecutionResultModel(**data)
    # noinspection PyUnresolvedReferences
    smart_contracts.post.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_address_balances(mocker: MockerFixture, network, generate_p2pkh_address):
    data = [
        {
            'address': generate_p2pkh_address(network=network),
            'sum': 5
        },
        {
            'address': generate_p2pkh_address(network=network),
            'sum': 10
        }
    ]
    mocker.patch.object(SmartContracts, 'get', return_value=data)
    smart_contracts = SmartContracts(network=network, baseuri=mocker.MagicMock())

    response = smart_contracts.address_balances(wallet_name='Test')

    assert response == [AddressBalanceModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    smart_contracts.get.assert_called_once()
