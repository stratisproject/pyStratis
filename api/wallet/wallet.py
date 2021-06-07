from typing import List
from api import APIRequest, EndpointRegister, endpoint
from api.wallet.requestmodels import *
from api.wallet.responsemodels import *
from pybitcoin import Address, AddressesModel, AddressBalanceModel, BuildTransactionModel, \
    BuildOfflineSignModel, RemovedTransactionModel, WalletGeneralInfoModel, \
    WalletBalanceModel, WalletSendTransactionModel, SendTransactionRequest
from pybitcoin.types import Money, hexstr, uint256


class Wallet(APIRequest, metaclass=EndpointRegister):
    route = '/api/wallet'

    def __init__(self, **kwargs):
        super(Wallet, self).__init__(**kwargs)

    @endpoint(f'{route}/mnemonic')
    def mnemonic(self, request_model: MnemonicRequest, **kwargs) -> List[str]:
        """Generates a mnemonic to use for an HD wallet.

        Args:
            request_model: MnemonicRequest model
            **kwargs:

        Returns:
            List[str]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return data.split(' ')

    @endpoint(f'{route}/create')
    def create(self, request_model: CreateRequest, **kwargs) -> str:
        """Creates a new wallet on this full node.

        Args:
            request_model: CreateRequest model
            **kwargs:

        Returns:
            List[str]
        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return data.split(' ')

    @endpoint(f'{route}/signmessage')
    def sign_message(self, request_model: SignMessageRequest, **kwargs) -> str:
        """Signs a message and returns the signature.

        Args:
            request_model: SignMessageRequest model
            **kwargs:

        Returns:
            str
        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return data

    @endpoint(f'{route}/pubkey')
    def pubkey(self, request_model: PubKeyRequest, **kwargs) -> hexstr:
        """Gets the public key for an address.

        Args:
            request_model: PubKeyRequest model
            **kwargs:

        Returns:
            hexstr
        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return data

    @endpoint(f'{route}/verifymessage')
    def verify_message(self, request_model: VerifyMessageRequest, **kwargs) -> bool:
        """Verifies the signature of a message.

        Args:
            request_model: VerifyMessageRequest model
            **kwargs:

        Returns:
            bool
        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return data

    @endpoint(f'{route}/load')
    def load(self, request_model: LoadRequest, **kwargs) -> None:
        """Loads a previously created wallet.

        Args:
            request_model: LoadRequest model
            **kwargs:

        Returns:
            None
        Raises:
            APIError
        """
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/recover')
    def recover(self, request_model: RecoverRequest, **kwargs) -> None:
        """Recovers an existing wallet.

        Args:
            request_model: RecoverRequest model
            **kwargs:

        Returns:
            None
        Raises:
            APIError
        """
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/recover-via-extpubkey')
    def recover_via_extpubkey(self, request_model: ExtPubRecoveryRequest, **kwargs) -> None:
        """Recovers a wallet using its extended public key.

        Args:
            request_model: ExtPubRecoveryRequest model
            **kwargs:

        Returns:
            None
        Raises:
            APIError
        """
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/general-info')
    def general_info(self, request_model: GeneralInfoRequest, **kwargs) -> WalletGeneralInfoModel:
        """Gets some general information about a wallet.

        Args:
            request_model: GeneralInfoRequest model
            **kwargs:

        Returns:
            WalletGeneralInfoModel
        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return WalletGeneralInfoModel(**data)

    @endpoint(f'{route}/transactionCount')
    def transaction_count(self, request_model: AccountRequest, **kwargs) -> int:
        """Get the transaction count for the specified Wallet and Account.

        Args:
            request_model: AccountRequest model
            **kwargs:

        Returns:
            int
        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return data

    @endpoint(f'{route}/history')
    def history(self, request_model: HistoryRequest, **kwargs) -> WalletHistoryModel:
        """Gets the history of a wallet.

        Args:
            request_model: HistoryRequest model
            **kwargs:

        Returns:
            WalletHistoryModel
        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return WalletHistoryModel(**data)

    @endpoint(f'{route}/balance')
    def balance(self, request_model: BalanceRequest, **kwargs) -> WalletBalanceModel:
        """Gets the balance of a wallet in STRAx (or sidechain coin). Both the confirmed and unconfirmed balance are returned.

        Args:
            request_model: BalanceRequest model
            **kwargs:

        Returns:
            WalletBalanceModel
        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return WalletBalanceModel(**data)

    @endpoint(f'{route}/received-by-address')
    def received_by_address(self, request_model: ReceivedByAddressRequest, **kwargs) -> AddressBalanceModel:
        """

        Args:
            request_model: ReceivedByAddressRequest model
            **kwargs:

        Returns:
            AddressBalanceModel
        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return AddressBalanceModel(**data)

    @endpoint(f'{route}/maxbalance')
    def max_balance(self, request_model: MaxBalanceRequest, **kwargs) -> MaxSpendableAmountModel:
        """Gets the maximum spendable balance for an account along with the fee required to spend it.

        Args:
            request_model: MaxBalanceRequest model
            **kwargs:

        Returns:
            MaxSpendableAmountModel
        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return MaxSpendableAmountModel(**data)

    @endpoint(f'{route}/spendable-transactions')
    def spendable_transactions(self, request_model: SpendableTransactionsRequest, **kwargs) -> SpendableTransactionsModel:
        """Gets the spendable transactions for an account with the option to specify how many confirmations a transaction needs to be included.

        Args:
            request_model: SpendableTransactionsRequest model
            **kwargs:

        Returns:
            SpendableTransactionsModel
        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return SpendableTransactionsModel(**data)

    @endpoint(f'{route}/estimate-txfee')
    def estimate_txfee(self, request_model: EstimateTxFeeRequest, **kwargs) -> Money:
        """Gets a fee estimate for a specific transaction.

        Args:
            request_model: EstimateTxFeeRequest model
            **kwargs:

        Returns:
            Money

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return data

    @endpoint(f'{route}/build-transaction')
    def build_transaction(self, request_model: BuildTransactionRequest, **kwargs) -> BuildTransactionModel:
        """Builds a transaction and returns the hex to use when executing the transaction.

        Args:
            request_model: BuildTransactionRequest model
            **kwargs:

        Returns:
            BuildTransactionModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return BuildTransactionModel(**data)

    @endpoint(f'{route}/build-interflux-transaction')
    def build_interflux_transaction(self, request_model: BuildInterfluxTransactionRequest, **kwargs) -> BuildTransactionModel:
        """Builds a transaction and returns the hex to use when executing the transaction.

        Args:
            request_model: BuildInterfluxTransactionRequest model
            **kwargs:

        Returns:
            BuildTransactionModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return BuildTransactionModel(**data)

    @endpoint(f'{route}/send-transaction')
    def send_transaction(self, request_model: SendTransactionRequest, **kwargs) -> WalletSendTransactionModel:
        """Sends a transaction that has already been built.

        Args:
            request_model: SendTransactionRequest model
            **kwargs:

        Returns:
            WalletSendTransactionModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return WalletSendTransactionModel(**data)

    @endpoint(f'{route}/list-wallets')
    def list_wallets(self, **kwargs) -> List[str]:
        """Lists all the files found in the database

        Args:
            **kwargs:

        Returns:
            List[str]

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return data

    @endpoint(f'{route}/account')
    def account(self, request_model: GetUnusedAccountRequest, **kwargs) -> str:
        """Creates a new account for a wallet.

        Args:
            request_model: GetUnusedAccountRequest model
            **kwargs:

        Returns:
            str

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return data

    @endpoint(f'{route}/accounts')
    def accounts(self, request_model: GetAccountsRequest, **kwargs) -> List[str]:
        """Gets a list of accounts for the specified wallet.

        Args:
            request_model: GetAccountsRequest model
            **kwargs:

        Returns:
            List[str]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return data

    @endpoint(f'{route}/unusedaddress')
    def unused_address(self, request_model: GetUnusedAddressRequest, **kwargs) -> Address:
        """Gets an unused address (in the Base58 format) for a wallet account.

        Args:
            request_model: GetUnusedAddressRequest model
            **kwargs:

        Returns:
            Address

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return data

    @endpoint(f'{route}/unusedaddresses')
    def unused_addresses(self, request_model: GetUnusedAddressesRequest, **kwargs) -> List[str]:
        """Gets a specified number of unused addresses (in the Base58 format) for a wallet account.

        Args:
            request_model: GetUnusedAddressesRequest model
            **kwargs:

        Returns:
            List[str]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return data

    @endpoint(f'{route}/newaddresses')
    def new_addresses(self, request_model: GetNewAddressesRequest, **kwargs) -> List[str]:
        """Gets a specified number of new addresses (in the Base58 format) for a wallet account.

        Args:
            request_model: GetNewAddressesRequest model
            **kwargs:

        Returns:
            List[str]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return data

    @endpoint(f'{route}/addresses')
    def addresses(self, request_model: GetAddressesRequest, **kwargs) -> AddressesModel:
        """Gets all addresses for a wallet account.

        Args:
            request_model: GetAddressesRequest model
            **kwargs:

        Returns:
            AddressesModel

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return AddressesModel(**data)

    @endpoint(f'{route}/remove-transactions')
    def remove_transactions(self, request_model: RemoveTransactionsRequest, **kwargs) -> List[RemovedTransactionModel]:
        """Removes transactions from the wallet.

        Args:
            request_model: RemoveTransactionsRequest model
            **kwargs:

        Returns:
            List[RemovedTransactionModel]

        Raises:
            APIError
        """
        data = self.delete(request_model, **kwargs)

        return [RemovedTransactionModel(**x) for x in data]

    @endpoint(f'{route}/remove-wallet')
    def remove_wallet(self, request_model: RemoveWalletRequest, **kwargs) -> None:
        """Remove a wallet

        Args:
            request_model: RemoveWalletRequest model
            **kwargs:

        Returns:
            None
        Raises:
            APIError
        """
        self.delete(request_model, **kwargs)

    @endpoint(f'{route}/extpubkey')
    def extpubkey(self, request_model: ExtPubKeyRequest, **kwargs) -> hexstr:
        """Gets the extended public key of a specified wallet account.

        Args:
            request_model: ExtPubKeyRequest model
            **kwargs:

        Returns:
            hexstr

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return data

    @endpoint(f'{route}/privatekey')
    def private_key(self, request_model: PrivateKeyRequest, **kwargs) -> hexstr:
        """Gets the private key of a specified wallet address.

        Args:
            request_model: PrivateKeyRequest model
            **kwargs:

        Returns:
            hexstr

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return data

    @endpoint(f'{route}/sync')
    def sync(self, request_model: SyncRequest, **kwargs) -> None:
        """Requests the node resyncs from a block specified by its block hash.

        Args:
            request_model: SyncRequest model
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/sync-from-date')
    def sync_from_date(self, request_model: SyncFromDateRequest, **kwargs) -> None:
        """Request the node resyncs starting from a given date and time.

        Args:
            request_model: SyncFromDateRequest model
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/wallet-stats')
    def wallet_stats(self, request_model: StatsRequest, **kwargs) -> WalletStatsModel:
        """Retrieves information about the wallet.

        Args:
            request_model: StatsRequest model
            **kwargs:

        Returns:
            WalletStatsModel
        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return WalletStatsModel(**data)

    @endpoint(f'{route}/splitcoins')
    def split_coins(self, request_model: SplitCoinsRequest, **kwargs) -> WalletSendTransactionModel:
        """Creates requested amount of UTXOs each of equal value.

        Args:
            request_model: SplitCoinsRequest model
            **kwargs:

        Returns:
            WalletSendTransactionModel
        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return WalletSendTransactionModel(**data)

    @endpoint(f'{route}/distribute-utxos')
    def distribute_utxos(self, request_model: DistributeUTXOsRequest, **kwargs) -> DistributeUtxoModel:
        """Splits and distributes UTXOs across wallet addresses

        Args:
            request_model: DistributeUTXOsRequest model
            **kwargs:

        Returns:
            DistributeUtxoModel
        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return DistributeUtxoModel(**data)

    @endpoint(f'{route}/sweep')
    def sweep(self, request_model: SweepRequest, **kwargs) -> List[str]:
        """Sweeps a wallet to specified address.

        Args:
            request_model: SweepRequest model
            **kwargs:

        Returns:
            List[str]
        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return data

    @endpoint(f'{route}/build-offline-sign-request')
    def build_offline_sign_request(self, request_model: BuildOfflineSignRequest, **kwargs) -> BuildOfflineSignModel:
        """Builds an offline sign request for a transaction.

        Args:
            request_model: BuildOfflineSignRequest model
            **kwargs:

        Returns:
            BuildOfflineSignModel
        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return BuildOfflineSignModel(**data)

    @endpoint(f'{route}/offline-sign-request')
    def offline_sign_request(self, request_model: OfflineSignRequest, **kwargs) -> BuildTransactionModel:
        """Build an offline sign request for a transaction. The resulting transaction hex can be broadcast.

        Args:
            request_model: OfflineSignRequest model
            **kwargs:

        Returns:
            BuildTransactionModel
        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return BuildTransactionModel(**data)

    @endpoint(f'{route}/consolidate')
    def consolidate(self, request_model: ConsolidateRequest, **kwargs) -> uint256:
        """Consolidate a wallet.

        Args:
            request_model: ConsolidateRequest model
            **kwargs:

        Returns:
            uint256

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return data
