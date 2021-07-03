import pytest
from pystratis.api.federationwallet.responsemodels import *
from pystratis.api.consensus.requestmodels import GetBlockHashRequest


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_general_info(interflux_strax_node):
    response = interflux_strax_node.federation_wallet.general_info()
    assert isinstance(response, WalletGeneralInfoModel)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_balance(interflux_strax_node):
    response = interflux_strax_node.federation_wallet.balance()
    assert isinstance(response, WalletBalanceModel)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_history(interflux_strax_node):
    response = interflux_strax_node.federation_wallet.history(max_entries_to_return=2)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, WithdrawalModel)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_sync(interflux_strax_node):
    block_hash = interflux_strax_node.consensus.get_blockhash(GetBlockHashRequest(height=2))
    interflux_strax_node.federation_wallet.sync(block_hash=block_hash)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_enable_federation(interflux_strax_node):
    interflux_strax_node.federation_wallet.enable_federation(
        mnemonic='secret mnemonic',
        password='password',
        passphrase='passphrase',
        timeout_seconds=60
    )


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_remove_transactions(interflux_strax_node):
    response = interflux_strax_node.federation_wallet.remove_transactions(resync=True)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, RemovedTransactionModel)
