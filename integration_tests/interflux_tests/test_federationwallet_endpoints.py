import pytest
from api.federationwallet.requestmodels import *
from api.federationwallet.responsemodels import *
from api.consensus.requestmodels import GetBlockHashRequest


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_general_info(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.federation_wallet.general_info()
    assert isinstance(response, WalletGeneralInfoModel)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_balance(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.federation_wallet.balance()
    assert isinstance(response, WalletBalanceModel)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_history(interflux_cirrusminer_node):
    request_model = HistoryRequest(max_entries_to_return=2)
    response = interflux_cirrusminer_node.federation_wallet.history(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, WithdrawalModel)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_sync(interflux_cirrusminer_node):
    block_hash = interflux_cirrusminer_node.consensus.get_blockhash(GetBlockHashRequest(height=2))
    request_model = SyncRequest(hash=block_hash)
    interflux_cirrusminer_node.federation_wallet.sync(request_model)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_enable_federation(interflux_cirrusminer_node):
    request_model = EnableFederationRequest(
        mnemonic='secret mnemonic',
        password='password',
        passphrase='passphrase',
        timeout_seconds=60
    )
    interflux_cirrusminer_node.federation_wallet.enable_federation(request_model)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_remove_transactions(interflux_cirrusminer_node):
    request_model = RemoveTransactionsRequest(resync=True)
    response = interflux_cirrusminer_node.federation_wallet.remove_transactions(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, RemovedTransactionModel)
