import pytest
from pytest_mock import MockerFixture
from pystratis.api.smartcontractwallet import SmartContractWallet
from pystratis.api.smartcontractwallet.responsemodels import *
from pystratis.core.networks import CirrusMain
from pystratis.core import ContractTransactionItemType, Outpoint, SmartContractParameter, SmartContractParameterType
from pystratis.core.types import Address, Money, uint32, uint64, uint128, uint256, int32, int64


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_account_addresses(mocker: MockerFixture, network, generate_p2pkh_address):
    data = [
        generate_p2pkh_address(network=network),
        generate_p2pkh_address(network=network),
        generate_p2pkh_address(network=network),
        generate_p2pkh_address(network=network)
    ]
    mocker.patch.object(SmartContractWallet, 'get', return_value=data)
    smart_contract_wallet = SmartContractWallet(network=network, baseuri=mocker.MagicMock())

    response = smart_contract_wallet.account_addresses(wallet_name='Test')

    assert response == [Address(address=x, network=network) for x in data]
    # noinspection PyUnresolvedReferences
    smart_contract_wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_address_balance(mocker: MockerFixture, network, generate_p2pkh_address):
    data = 100
    mocker.patch.object(SmartContractWallet, 'get', return_value=data)
    smart_contract_wallet = SmartContractWallet(network=network, baseuri=mocker.MagicMock())
    response = smart_contract_wallet.address_balance(
        address=Address(address=generate_p2pkh_address(network=network), network=network)
    )

    assert response == Money.from_satoshi_units(data)
    # noinspection PyUnresolvedReferences
    smart_contract_wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_history(mocker: MockerFixture, network, generate_p2pkh_address, generate_uint256):
    data = [
        {
            'blockHeight': 1,
            'type': ContractTransactionItemType.ContractCreate,
            'hash': generate_uint256,
            'to': generate_p2pkh_address(network=network),
            'amount': 10,
            'transactionFee': 1,
            'gasFee': 1
        }
    ]
    mocker.patch.object(SmartContractWallet, 'get', return_value=data)
    smart_contract_wallet = SmartContractWallet(network=network, baseuri=mocker.MagicMock())
    response = smart_contract_wallet.history(
        wallet_name='Test',
        address=Address(address=generate_p2pkh_address(network=network), network=network),
        skip=2,
        take=2
    )

    assert response == [ContractTransactionItemModel(**x) for x in data]
    # noinspection PyUnresolvedReferences
    smart_contract_wallet.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_create(mocker: MockerFixture, network, generate_uint256, generate_p2pkh_address, generate_hexstring):
    data = generate_uint256
    mocker.patch.object(SmartContractWallet, 'post', return_value=data)
    smart_contract_wallet = SmartContractWallet(network=network, baseuri=mocker.MagicMock())
    response = smart_contract_wallet.create(
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

    assert response == uint256(data)
    # noinspection PyUnresolvedReferences
    smart_contract_wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_call(mocker: MockerFixture, network, generate_p2pkh_address, generate_hexstring, generate_uint256):
    data = {
        'fee': 1,
        'hex': generate_hexstring(128),
        'message': 'message',
        'success': True,
        'transactionId': generate_uint256
    }
    mocker.patch.object(SmartContractWallet, 'post', return_value=data)
    smart_contract_wallet = SmartContractWallet(network=network, baseuri=mocker.MagicMock())

    response = smart_contract_wallet.call(
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
    smart_contract_wallet.post.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_send_transaction(mocker: MockerFixture, network, generate_hexstring,
                          generate_p2pkh_address, generate_uint256):
    data = {
        'transactionId': generate_uint256,
        'outputs': [
            {
                'address': generate_p2pkh_address(network=network),
                'amount': 10,
                'opReturnData': f'{generate_p2pkh_address(network=network)}'
            }
        ]
    }
    mocker.patch.object(SmartContractWallet, 'post', return_value=data)
    smart_contract_wallet = SmartContractWallet(network=network, baseuri=mocker.MagicMock())
    response = smart_contract_wallet.send_transaction(transaction_hex=generate_hexstring(128))

    assert response == WalletSendTransactionModel(**data)
    # noinspection PyUnresolvedReferences
    smart_contract_wallet.post.assert_called_once()
