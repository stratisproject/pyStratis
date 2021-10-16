import pytest
from pystratis.nodes import CirrusUnity3DNode, CirrusMinerNode
from pystratis.api.unity3d.responsemodels import *
from pystratis.core import SmartContractParameter, SmartContractParameterType, Recipient, Outpoint
from pystratis.core.types import Address, Money, hexstr, uint256, int32


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_utxos_for_address(cirrusminerunity3d_node: CirrusUnity3DNode, get_smart_contract_address_unity):
    address = get_smart_contract_address_unity
    response = cirrusminerunity3d_node.unity3d.get_utxos_for_address(address=address)
    assert isinstance(response, GetUTXOModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_address_balance(cirrusminerunity3d_node: CirrusUnity3DNode, get_smart_contract_address_unity):
    address = get_smart_contract_address_unity
    response = cirrusminerunity3d_node.unity3d.get_address_balance(address=address)
    assert isinstance(response, Money)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_blockheader(cirrusminerunity3d_node: CirrusUnity3DNode):
    block_hash = cirrusminerunity3d_node.consensus.get_best_blockhash()
    response = cirrusminerunity3d_node.node.get_blockheader(block_hash=block_hash, is_json_format=True)
    assert isinstance(response, BlockHeaderModel)
    if response.previous_blockhash is not None:
        assert isinstance(response.previous_blockhash, uint256)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_raw_transaction(cirrusminerunity3d_node: CirrusUnity3DNode, wait_and_clear_mempool):
    assert wait_and_clear_mempool()
    spendable_transactions = cirrusminerunity3d_node.wallet.spendable_transactions(wallet_name='Test', account_name='account 0', min_confirmations=2)
    spendable_transactions = [x for x in spendable_transactions.transactions]
    for spendable_transaction in spendable_transactions:
        response = cirrusminerunity3d_node.node.get_raw_transaction(trxid=spendable_transaction.transaction_id, verbose=True)
        assert isinstance(response, TransactionModel)

        response = cirrusminerunity3d_node.node.get_raw_transaction(trxid=spendable_transaction.transaction_id, verbose=False)
        assert isinstance(response, hexstr)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_send_transaction(cirrusminer_node: CirrusMinerNode,
                          cirrusminerunity3d_node: CirrusUnity3DNode,
                          get_spendable_transactions,
                          wait_and_clear_mempool,
                          get_node_address_with_balance,
                          get_node_unused_address):
    assert wait_and_clear_mempool()
    destination_address = get_node_unused_address(cirrusminer_node)
    change_address = get_node_address_with_balance(cirrusminerunity3d_node)
    fee_amount = Money(0.0001)
    amount_to_send = Money(10)
    op_return_amount = Money(0.00000001)
    transactions = get_spendable_transactions(
        node=cirrusminerunity3d_node, amount=amount_to_send, op_return_amount=op_return_amount, wallet_name='Test'
    )
    built_transaction = cirrusminerunity3d_node.wallet.build_transaction(
        fee_amount=fee_amount,
        password='password',
        segwit_change_address=False,
        wallet_name='Test',
        account_name='account 0',
        outpoints=[Outpoint(transaction_id=x.transaction_id, index=x.index) for x in transactions],
        recipients=[Recipient(destination_address=destination_address, subtraction_fee_from_amount=True, amount=amount_to_send)],
        op_return_data='opreturn',
        op_return_amount=op_return_amount,
        allow_unconfirmed=False,
        shuffle_outputs=True,
        change_address=change_address
    )
    response = cirrusminerunity3d_node.wallet.send_transaction(transaction_hex=built_transaction.hex)
    assert wait_and_clear_mempool()
    assert isinstance(response, WalletSendTransactionModel)
    assert isinstance(response.transaction_id, uint256)
    for item in response.outputs:
        assert isinstance(item, TransactionOutputModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_validate_address(cirrusminerunity3d_node: CirrusMinerNode, generate_p2pkh_address):
    address = generate_p2pkh_address(network=cirrusminerunity3d_node.blockchainnetwork)
    response = cirrusminerunity3d_node.node.validate_address(address=address)
    assert isinstance(response, ValidateAddressModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_block(cirrusminerunity3d_node: CirrusUnity3DNode):
    # Request json output with maximum details.
    block_hash = cirrusminerunity3d_node.consensus.get_best_blockhash()
    response = cirrusminerunity3d_node.blockstore.block(block_hash=block_hash, show_transaction_details=True, output_json=True)
    assert isinstance(response, BlockModel)

    # Request hex output.
    response = cirrusminerunity3d_node.blockstore.block(block_hash=block_hash, show_transaction_details=True, output_json=False)
    assert isinstance(response, hexstr)

    # Request a hash that doesn't exist.
    bad_block_hash = uint256('fffdf')
    response = cirrusminerunity3d_node.blockstore.block(block_hash=bad_block_hash, show_transaction_details=True, output_json=False)
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_receipt(cirrusminerunity3d_node: CirrusUnity3DNode, get_contract_create_trxid):
    trxid = get_contract_create_trxid
    # noinspection PyTypeChecker
    response = cirrusminerunity3d_node.smart_contracts.receipt(tx_hash=trxid)
    assert isinstance(response, ReceiptModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_local_call(cirrusminerunity3d_node: CirrusUnity3DNode, get_node_address_with_balance, get_smart_contract_address_unity):
    sending_address = get_node_address_with_balance(cirrusminerunity3d_node)
    sc_address = get_smart_contract_address_unity
    response = cirrusminerunity3d_node.smart_contracts.local_call(
        contract_address=sc_address,
        method_name='TestMethod',
        amount=Money(0),
        gas_price=100,
        gas_limit=250000,
        sender=sending_address,
        block_height=None,
        parameters=[
            SmartContractParameter(value_type=SmartContractParameterType.Int32, value=int32(0)),
            SmartContractParameter(value_type=SmartContractParameterType.String, value='SmartContracts made easy.')
        ]
    )
    assert isinstance(response, LocalExecutionResultModel)
