from typing import List
from api import APIRequest, EndpointRegister, endpoint
from api.wallet.requestmodels import *
from api.wallet.responsemodels import *
from pybitcoin import PubKey, ExtPubKey, AddressDescriptor, UtxoDescriptor, Key
from pybitcoin.types import Address, Money, hexstr, uint256


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
    def create(self, request_model: CreateRequest, **kwargs) -> List[str]:
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
    def pubkey(self, request_model: PubKeyRequest, **kwargs) -> PubKey:
        """Gets the public key for an address.

        Args:
            request_model: PubKeyRequest model
            **kwargs:

        Returns:
            PubKey
        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return PubKey(data)

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

    @endpoint(f'{route}/transactioncount')
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

        return data['transactionCount']

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

        for i in range(len(data['history'])):
            for j in range(len(data['history'][i]['transactionsHistory'])):
                data['history'][i]['transactionsHistory'][j]['toAddress'] = Address(
                    address=data['history'][i]['transactionsHistory'][j]['toAddress'],
                    network=self._network
                )
                data['history'][i]['transactionsHistory'][j]['amount'] = Money.from_satoshi_units(data['history'][i]['transactionsHistory'][j]['amount'])
                if 'fee' in data['history'][i]['transactionsHistory'][j]:
                    data['history'][i]['transactionsHistory'][j]['fee'] = Money.from_satoshi_units(data['history'][i]['transactionsHistory'][j]['fee'])
                if 'payments' in data['history'][i]['transactionsHistory'][j]:
                    for k in range(len(data['history'][i]['transactionsHistory'][j]['payments'])):
                        data['history'][i]['transactionsHistory'][j]['payments'][k]['amount'] = Money.from_satoshi_units(data['history'][i]['transactionsHistory'][j]['payments'][k]['amount'])
                        if 'fee' in data['history'][i]['transactionsHistory'][j]['payments'][k]:
                            data['history'][i]['transactionsHistory'][j]['payments'][k]['fee'] = Money.from_satoshi_units(data['history'][i]['transactionsHistory'][j]['payments'][k]['fee'])
                        data['history'][i]['transactionsHistory'][j]['payments'][k]['destinationAddress'] = Address(
                            address=data['history'][i]['transactionsHistory'][j]['payments'][k]['destinationAddress'],
                            network=self._network
                        )

        return WalletHistoryModel(**data)

    @endpoint(f'{route}/balance')
    def balance(self, request_model: BalanceRequest, **kwargs) -> WalletBalanceModel:
        """Gets the balance of a wallet in STRAX (or sidechain coin).
        Both the confirmed and unconfirmed balance are returned.

        Args:
            request_model: BalanceRequest model
            **kwargs:

        Returns:
            WalletBalanceModel
        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        for i in range(len(data['balances'])):
            data['balances'][i]['amountConfirmed'] = Money.from_satoshi_units(data['balances'][i]['amountConfirmed'])
            data['balances'][i]['amountUnconfirmed'] = Money.from_satoshi_units(data['balances'][i]['amountUnconfirmed'])
            data['balances'][i]['spendableAmount'] = Money.from_satoshi_units(data['balances'][i]['spendableAmount'])
            if data['balances'][i]['addresses'] is not None:
                for j in range(len(data['balances'][i]['addresses'])):
                    data['balances'][i]['addresses'][j]['amountConfirmed'] = Money.from_satoshi_units(data['balances'][i]['addresses'][j]['amountConfirmed'])
                    data['balances'][i]['addresses'][j]['amountUnconfirmed'] = Money.from_satoshi_units(data['balances'][i]['addresses'][j]['amountUnconfirmed'])
                    data['balances'][i]['addresses'][j]['address'] = Address(
                        address=data['balances'][i]['addresses'][j]['address'], network=self._network
                    )

        return WalletBalanceModel(**data)

    @endpoint(f'{route}/received-by-address')
    def received_by_address(self, request_model: ReceivedByAddressRequest, **kwargs) -> AddressBalanceModel:
        """Retrieves transactions received by the specified address.

        Args:
            request_model: ReceivedByAddressRequest model
            **kwargs:

        Returns:
            AddressBalanceModel
        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        data['address'] = Address(address=data['address'], network=self._network)
        data['amountConfirmed'] = Money.from_satoshi_units(data['amountConfirmed'])
        data['amountUnconfirmed'] = Money.from_satoshi_units(data['amountUnconfirmed'])
        data['spendableAmount'] = Money.from_satoshi_units(data['spendableAmount'])

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
        data['maxSpendableAmount'] = Money.from_satoshi_units(data['maxSpendableAmount'])
        data['fee'] = Money.from_satoshi_units(data['fee'])

        return MaxSpendableAmountModel(**data)

    @endpoint(f'{route}/spendable-transactions')
    def spendable_transactions(self,
                               request_model: SpendableTransactionsRequest,
                               **kwargs) -> SpendableTransactionsModel:
        """Gets the spendable transactions for an account with the option to specify how many
        confirmations a transaction needs to be included.

        Args:
            request_model: SpendableTransactionsRequest model
            **kwargs:

        Returns:
            SpendableTransactionsModel
        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        for i in range(len(data['transactions'])):
            data['transactions'][i]['amount'] = Money.from_satoshi_units(data['transactions'][i]['amount'])
            data['transactions'][i]['address'] = Address(
                address=data['transactions'][i]['address'],
                network=self._network
            )

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

        return Money.from_satoshi_units(data)

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
        data['fee'] = Money.from_satoshi_units(data['fee'])

        return BuildTransactionModel(**data)

    @endpoint(f'{route}/build-interflux-transaction')
    def build_interflux_transaction(self,
                                    request_model: BuildInterfluxTransactionRequest,
                                    **kwargs) -> BuildTransactionModel:
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
        data['fee'] = Money.from_satoshi_units(data['fee'])

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

        for i in range(len(data['outputs'])):
            if 'address' in data['outputs'][i]:
                data['outputs'][i]['address'] = Address(address=data['outputs'][i]['address'], network=self._network)
                data['outputs'][i]['amount'] = Money.from_satoshi_units(data['outputs'][i]['amount'])
            else:
                # No address in coldstaking transactions.
                pass
            data['outputs'][i] = TransactionOutputModel(**data['outputs'][i])

        return WalletSendTransactionModel(**data)

    @endpoint(f'{route}/list-wallets')
    def list_wallets(self, **kwargs) -> dict:
        """Lists all the files found in the database

        Args:
            **kwargs:

        Returns:
            dict

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

        return Address(address=data, network=self._network)

    @endpoint(f'{route}/unusedaddresses')
    def unused_addresses(self, request_model: GetUnusedAddressesRequest, **kwargs) -> List[Address]:
        """Gets a specified number of unused addresses (in the Base58 format) for a wallet account.

        Args:
            request_model: GetUnusedAddressesRequest model
            **kwargs:

        Returns:
            List[Address]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return [Address(address=x, network=self._network) for x in data]

    @endpoint(f'{route}/newaddresses')
    def new_addresses(self, request_model: GetNewAddressesRequest, **kwargs) -> List[Address]:
        """Gets a specified number of new addresses (in the Base58 format) for a wallet account.

        Args:
            request_model: GetNewAddressesRequest model
            **kwargs:

        Returns:
            List[Address]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return [Address(address=x, network=self._network) for x in data]

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

        for i in range(len(data['addresses'])):
            data['addresses'][i]['address'] = Address(address=data['addresses'][i]['address'], network=self._network)
            data['addresses'][i]['amountConfirmed'] = Money.from_satoshi_units(data['addresses'][i]['amountConfirmed'])
            data['addresses'][i]['amountUnconfirmed'] = Money.from_satoshi_units(data['addresses'][i]['amountUnconfirmed'])

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
    def extpubkey(self, request_model: ExtPubKeyRequest, **kwargs) -> ExtPubKey:
        """Gets the extended public key of a specified wallet account.

        Args:
            request_model: ExtPubKeyRequest model
            **kwargs:

        Returns:
            ExtPubKey

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return ExtPubKey(data)

    @endpoint(f'{route}/privatekey')
    def private_key(self, request_model: PrivateKeyRequest, **kwargs) -> Key:
        """Gets the private key of a specified wallet address.

        Args:
            request_model: PrivateKeyRequest model
            **kwargs:

        Returns:
            Key

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return Key(data)

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
        for i in range(len(data['utxoAmounts'])):
            data['utxoAmounts'][i]['amount'] = Money.from_satoshi_units(data['utxoAmounts'][i]['amount'])

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
        for i in range(len(data['outputs'])):
            data['outputs'][i]['address'] = Address(address=data['outputs'][i]['address'], network=self._network)
            data['outputs'][i]['amount'] = Money.from_satoshi_units(data['outputs'][i]['amount'])
            data['outputs'][i] = TransactionOutputModel(**data['outputs'][i])

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

        for i in range(len(data['walletSendTransaction'])):
            for j in range(len(data['walletSendTransaction'][i]['outputs'])):
                data['walletSendTransaction'][i]['outputs'][j]['amount'] = Money.from_satoshi_units(data['walletSendTransaction'][i]['outputs'][j]['amount'])
                data['walletSendTransaction'][i]['outputs'][j]['address'] = Address(
                    address=data['walletSendTransaction'][i]['outputs'][j]['address'],
                    network=self._network
                )

        return DistributeUtxoModel(**data)

    @endpoint(f'{route}/sweep')
    def sweep(self, request_model: SweepRequest, **kwargs) -> List[uint256]:
        """Sweeps a wallet to specified address.

        Args:
            request_model: SweepRequest model
            **kwargs:

        Returns:
            List[uint256]
        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return [uint256(x) for x in data]

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
        data['fee'] = Money(data['fee'])

        # Build the UtxoDescriptors
        for i in range(len(data['utxos'])):
            data['utxos'][i]['amount'] = Money(data['utxos'][i]['amount'])
        data['utxos'] = [UtxoDescriptor(**x) for x in data['utxos']]

        # Build the AddressDescriptors
        address_descriptors = []
        for address_descriptor in data['addresses']:
            address_descriptor['address'] = Address(address=address_descriptor['address'], network=self._network)
            address_descriptors.append(address_descriptor)
        data['addresses'] = [AddressDescriptor(**x) for x in address_descriptors]

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
        data['fee'] = Money.from_satoshi_units(data['fee'])

        return BuildTransactionModel(**data)

    @endpoint(f'{route}/consolidate')
    def consolidate(self, request_model: ConsolidateRequest, **kwargs) -> hexstr:
        """Consolidate a wallet.

        utxo_value_threshold looks to consolidate any utxo amount below the threshold.

        Args:
            request_model: ConsolidateRequest model
            **kwargs:

        Returns:
            hexstr

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return hexstr(data)
