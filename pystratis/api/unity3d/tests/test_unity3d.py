import pytest
import ast
import pickle
from random import randint
from pytest_mock import MockerFixture
from pystratis.api.unity3d import Unity3D
from pystratis.core.networks import CirrusMain
from pystratis.api.unity3d.responsemodels import *
from pystratis.core.types import Money, Address, uint32, uint64, uint128, uint256, int32, int64
from pystratis.core import SmartContractParameter, SmartContractParameterType


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_get_utxos_for_address(mocker: MockerFixture, network, generate_p2pkh_address, generate_uint256):
    amount_in_sats = 1000
    data = {
        'balanceSat': amount_in_sats,
        'utxOs': [
            {
                'hash': generate_uint256,
                'n': 0,
                'satoshis': amount_in_sats
            }
        ]
    }
    mocker.patch.object(Unity3D, 'get', return_value=data)
    unity3d = Unity3D(network=network, baseuri=mocker.MagicMock())

    response = unity3d.get_utxos_for_address(address=generate_p2pkh_address(network))

    assert response == GetUTXOModel(**data)
    # noinspection PyUnresolvedReferences
    unity3d.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_get_address_balance(mocker: MockerFixture, network, generate_p2pkh_address):
    amount_in_sats = 1000
    mocker.patch.object(Unity3D, 'get', return_value=amount_in_sats)
    unity3d = Unity3D(network=network, baseuri=mocker.MagicMock())

    response = unity3d.get_address_balance(address=generate_p2pkh_address(network))

    assert response == Money.from_satoshi_units(amount_in_sats)
    # noinspection PyUnresolvedReferences
    unity3d.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_get_blockheader(mocker: MockerFixture, network, generate_uint256):
    data = {
        'version': 1,
        'merkleroot': generate_uint256,
        'nonce': 0,
        'bits': 'bits',
        'previousblockhash': generate_uint256,
        'time': 1,
    }
    mocker.patch.object(Unity3D, 'get', return_value=data)
    unity3d = Unity3D(network=network, baseuri=mocker.MagicMock())
    response = unity3d.get_blockheader(
        block_hash=generate_uint256,
        is_json_format=True
    )

    assert response == BlockHeaderModel(**data)
    # noinspection PyUnresolvedReferences
    unity3d.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_get_raw_transaction_verbose(mocker: MockerFixture, network, generate_coinbase_transaction, generate_uint256):
    trxid = generate_uint256
    data = generate_coinbase_transaction(trxid)
    mocker.patch.object(Unity3D, 'get', return_value=data)
    unity3d = Unity3D(network=network, baseuri=mocker.MagicMock())

    response = unity3d.get_raw_transaction(trxid=trxid, verbose=True)

    assert response == TransactionModel(**data)
    # noinspection PyUnresolvedReferences
    unity3d.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_get_raw_transaction_nonverbose(mocker: MockerFixture, network, generate_coinbase_transaction, generate_uint256):
    trxid = generate_uint256
    data = generate_coinbase_transaction(trxid)
    hexified_data = bytes(str(data), 'ascii').hex()
    mocker.patch.object(Unity3D, 'get', return_value=hexified_data)
    unity3d = Unity3D(network=network, baseuri=mocker.MagicMock())

    response = unity3d.get_raw_transaction(trxid=trxid, verbose=False)

    assert response == hexified_data
    unserialized_response = ast.literal_eval(bytes.fromhex(hexified_data).decode('ascii'))
    assert data == unserialized_response
    # noinspection PyUnresolvedReferences
    unity3d.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_send_transaction(mocker: MockerFixture, network, generate_uint256, generate_p2pkh_address, generate_hexstring):
    data = {
        'transactionId': generate_uint256,
        'outputs': [
            {
                'address': generate_p2pkh_address(network=network),
                'amount': '10',
                'opReturnData': f'{generate_p2pkh_address(network=network)}'
            }
        ]
    }
    mocker.patch.object(Unity3D, 'post', return_value=data)
    unity3d = Unity3D(network=network, baseuri=mocker.MagicMock())

    response = unity3d.send_transaction(transaction_hex=generate_hexstring(128))

    assert response == WalletSendTransactionModel(**data)
    # noinspection PyUnresolvedReferences
    unity3d.post.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_validate_address(mocker: MockerFixture, network, generate_p2pkh_address):
    address = generate_p2pkh_address(network=network)
    data = {
        'isvalid': True,
        'address': address,
        'scriptPubKey': 'a scriptPubKey',
        'isscript': False,
        'iswitness': False
    }
    mocker.patch.object(Unity3D, 'get', return_value=data)
    unity3d = Unity3D(network=network, baseuri=mocker.MagicMock())

    response = unity3d.validate_address(address=address)

    assert response == ValidateAddressModel(**data)
    # noinspection PyUnresolvedReferences
    unity3d.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_block_output_hexstr_no_details(mocker: MockerFixture, network, generate_uint256, generate_block_no_tx_data):
    data = pickle.dumps(generate_block_no_tx_data()).hex()
    mocker.patch.object(Unity3D, 'get', return_value=data)
    unity3d = Unity3D(network=network, baseuri=mocker.MagicMock())

    response = unity3d.block(
        block_hash=generate_uint256,
        show_transaction_details=True,
        output_json=False
    )

    assert response == data
    # noinspection PyUnresolvedReferences
    unity3d.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_block_output_hexstr_include_details(mocker: MockerFixture, network, generate_uint256, generate_block_with_tx_data):
    data = pickle.dumps(generate_block_with_tx_data(network=network)).hex()
    mocker.patch.object(Unity3D, 'get', return_value=data)
    unity3d = Unity3D(network=network, baseuri=mocker.MagicMock())

    response = unity3d.block(
        block_hash=generate_uint256,
        show_transaction_details=True,
        output_json=False
    )

    assert response == data
    # noinspection PyUnresolvedReferences
    unity3d.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_block_output_json_no_details(mocker: MockerFixture, network, generate_uint256, generate_block_no_tx_data):
    data = generate_block_no_tx_data()
    mocker.patch.object(Unity3D, 'get', return_value=data)
    unity3d = Unity3D(network=network, baseuri=mocker.MagicMock())

    response = unity3d.block(
        block_hash=generate_uint256,
        show_transaction_details=False,
        output_json=True
    )
    assert response == BlockModel(**data)
    # noinspection PyUnresolvedReferences
    unity3d.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_block_output_json_include_details(mocker: MockerFixture, network, generate_uint256, generate_block_with_tx_data):
    data = generate_block_with_tx_data(network=network)
    mocker.patch.object(Unity3D, 'get', return_value=data)
    unity3d = Unity3D(network=network, baseuri=mocker.MagicMock())

    response = unity3d.block(
        block_hash=generate_uint256,
        show_transaction_details=True,
        output_json=True
    )

    assert response == BlockTransactionDetailsModel(**data)
    # noinspection PyUnresolvedReferences
    unity3d.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_block_no_found(mocker: MockerFixture, network, generate_uint256):
    data = 'Block not found'
    mocker.patch.object(Unity3D, 'get', return_value=data)
    unity3d = Unity3D(network=network, baseuri=mocker.MagicMock())

    response = unity3d.block(
        block_hash=generate_uint256,
        show_transaction_details=True,
        output_json=True
    )

    assert response == data
    # noinspection PyUnresolvedReferences
    unity3d.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_addressindexertip(mocker: MockerFixture, network, generate_uint256):
    data = {
        'tipHash': generate_uint256,
        'tipHeight': randint(0, 300)
    }
    mocker.patch.object(Unity3D, 'get', return_value=data)
    unity3d = Unity3D(network=network, baseuri=mocker.MagicMock())
    response = unity3d.addressindexer_tip()

    assert response.tip_hash.to_hex() == data['tipHash']
    assert response.tip_height == data['tipHeight']
    # noinspection PyUnresolvedReferences
    unity3d.get.assert_called_once()


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
        ]
    }

    mocker.patch.object(Unity3D, 'get', return_value=data)
    unity3d = Unity3D(network=network, baseuri=mocker.MagicMock())

    response = unity3d.receipt(tx_hash=trxid)

    assert response == ReceiptModel(**data)
    # noinspection PyUnresolvedReferences
    unity3d.get.assert_called_once()


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

    mocker.patch.object(Unity3D, 'post', return_value=data)
    unity3d = Unity3D(network=network, baseuri=mocker.MagicMock())
    response = unity3d.local_call(
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
    unity3d.post.assert_called_once()
