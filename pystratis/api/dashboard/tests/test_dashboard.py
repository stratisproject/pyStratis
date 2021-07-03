import pytest
from pytest_mock import MockerFixture
from pystratis.api.dashboard import Dashboard
from pystratis.core.networks import StraxMain, CirrusMain


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths']]
    for endpoint in paths:
        if Dashboard.route + '/' in endpoint:
            assert endpoint in Dashboard.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths']]
    for endpoint in paths:
        if Dashboard.route + '/' in endpoint:
            assert endpoint in Dashboard.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths']]
    for endpoint in paths:
        if Dashboard.route + '/' in endpoint:
            assert endpoint in Dashboard.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths']]
    for endpoint in paths:
        if Dashboard.route + '/' in endpoint:
            assert endpoint in Dashboard.endpoints


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_asyncloopsstats(mocker: MockerFixture, network):
    data = """Async Loops
    Status                  : x running [0 faulted]
    Name                                                                            Type           Health         
    --------------------------------------------------------------------------------------------------------------
    AddressIndexer.indexingTask                                                     RegisteredTask Running        
    BlockStoreQueue.dequeueLoopTask                                                 RegisteredTask Running        
    BlockStoreSignaled.dequeueLoopTask                                              RegisteredTask Running        
    CallbackMessageListener-IncomingMessage-[::ffff:x.x.x.x]:x                      Dequeuer       Running        
    CoinviewPrefetcher-headersQueue                                                 Dequeuer       Running        
    DiscoverFromDnsSeedsAsync                                                       Loop           Running        
    DiscoverPeersAsync                                                              Loop           Running        
    FederationWalletSyncManager-blocksQueue                                         Dequeuer       Running        
    FinalizedBlockInfoRepository.finalizedBlockInfoPersistingTask                   RegisteredTask Running        
    FlushChain                                                                      Loop           Running        
    InputConsolidator-blockQueue                                                    Dequeuer       Running        
    MaturedBlocksSyncManager.requestDepositsTask                                    Loop           Running        
    MemoryPool.RelayWorker                                                          Loop           Running        
    MempoolCleaner                                                                  Loop           Running        
    NetworkPeer-asyncPayloadsQueue-[::ffff:x.x.x.x]:x                               Dequeuer       Running        
    NetworkPeerDisposer-peersToDispose                                              Dequeuer       Running        
    NetworkPeerDisposer-peersToDispose                                              Dequeuer       Running        
    NetworkPeerDisposer-peersToDispose                                              Dequeuer       Running        
    NetworkPeerDisposer-peersToDispose                                              Dequeuer       Running        
    NetworkPeerDisposer-peersToDispose                                              Dequeuer       Running        
    Notify                                                                          Loop           Running        
    PartialTransactionRequester                                                     Loop           Running        
    PartialValidator                                                                Dequeuer       Running        
    PeerConnectorAddNode.ConnectAsync                                               Loop           Running        
    PeerConnectorDiscovery.ConnectAsync                                             Loop           Running        
    Periodic peer flush                                                             Loop           Running        
    PeriodicBenchmarkLog                                                            Loop           Running        
    PeriodicLog                                                                     Loop           Running        
    PosMining.Stake                                                                 Loop           Running        
    SignedMultisigTransactionBroadcaster.broadcastFullySignedTransfersTask          Loop           Running        
    wallet persist job                                                              Loop           Running        
    WalletSyncManager.OrchestrateWalletSync                                         Loop           Running        
    --------------------------------------------------------------------------------------------------------------
    """
    mocker.patch.object(Dashboard, 'get', return_value=data)
    dashboard = Dashboard(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = dashboard.asyncloops_stats()

    assert response == data
    # noinspection PyUnresolvedReferences
    dashboard.get.assert_called_once()


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_stats(mocker: MockerFixture, network):
    data = """Node Stats
    Agent                   : StratisFullNode:1.0.7.2 (70012)
    Network                 : StraxMain
    Database                : leveldb
    Node Started            : x x
    Current Date            : x x
    
    Headers Height          : 381719  (Hash: bfec06bce44ad0a4e0d8be6ba2c589181bbe9f481e699cf2f0bd4db13c6046b3)
    Consensus Height        : 381719  (Hash: bfec06bce44ad0a4e0d8be6ba2c589181bbe9f481e699cf2f0bd4db13c6046b3)
    BlockStore Height       : 381719  (Hash: bfec06bce44ad0a4e0d8be6ba2c589181bbe9f481e699cf2f0bd4db13c6046b3)
    Fed.Wallet.Height       : 381719     (Hash : bfec06bce44ad0a4e0d8be6ba2c589181bbe9f481e699cf2f0bd4db13c6046b3)
    Wallet Height           : 381719  (Hash: bfec06bce44ad0a4e0d8be6ba2c589181bbe9f481e699cf2f0bd4db13c6046b3)
    AddressIndexer Height   : 381718 AddressCache%: 8.69    OutPointCache%: 42.44   Ms/block: 1028.48
    
    >> Connections (In:x) (Out:x)
    Data Transfer           : Received: x.x MB Sent: x.x MB
    
    >>> AddNode:
    OUT ::ffff:x.x.x.x:17105          (r/s/c):381719/381719/0           R/S MB: 0.21/0.20        agent:StratisFullNode:1.0.8.13 (70012)
    <<<
    OUT ::ffff:x.x.x.x:17105          (r/s/c):381719/381719/0           R/S MB: 2.54/4.12        agent:StratisFullNode:1.0.7.2 (70012)
    
    
    >> Consensus Manager
    Tip Age                 : 00.00:00:11 (maximum is 00.02:00:00)
    Synced with Network     : Yes
    Unconsumed blocks       : 0 -- (0 / 200 MB). Cache filled by: 0%
    Downloading blocks      : 0 queued out of 0 pending
    
    >> Async Loops
    Status                  : x running [0 faulted]
    
    >> Block Puller
    Blocks being downloaded : 0 (0 queued)
    Total Download Speed    : 89.87 KB/sec      Block Download Average  : 7.26 ms
    Average block size      : 0.65 KB           Blocks downloadable in 1 sec: 137.74
    
    >> Block Store
    Batch Size              : 0 MB / 5 MB (0 batched)
    Queue Size              : 0 MB (0 queued)
    
    >> Federation Wallet
    Federation Wallet       : Confirmed balance: x.x          Reserved for withdrawals: 0.00000000               Federation Status: Inactive
    
    >> Cross Chain Transfer Store
    Height                  : 381718 [46db1fa1612cc03656d1dab813d7c8312d4ad9099fe87393d1fbd8bf8b6b25b3]
    NextDepositHeight       : 1608806
    Partial Txs             : 0
    Suspended Txs           : 1
    
    --- Maturing Deposits ---
    500.90000000 (79) => x (Normal)
    900.00010000 (83) => Reward Distribution (Distribution)
    900.00025000 (183) => Reward Distribution (Distribution)
    900.00035930 (283) => Reward Distribution (Distribution)
    900.00087765 (383) => Reward Distribution (Distribution)
    900.00096310 (483) => Reward Distribution (Distribution)
    
    >> Mempool
    Tx Count                : 0 (Dynamic Size: 0 kb) (Orphan Size: 0)
    
    >> Wallets
    x/x          : Confirmed balance: x.x          Unconfirmed balance: 0.00000000
    """
    mocker.patch.object(Dashboard, 'get', return_value=data)
    dashboard = Dashboard(network=network, baseuri=mocker.MagicMock(), session=mocker.MagicMock())

    response = dashboard.stats()

    assert response == data
    # noinspection PyUnresolvedReferences
    dashboard.get.assert_called_once()
