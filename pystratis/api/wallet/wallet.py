from typing import List, Optional, Union
from decimal import Decimal
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.wallet.requestmodels import *
from pystratis.api.wallet.responsemodels import *
from pystratis.core import PubKey, ExtPubKey, Key, Outpoint, Recipient
from pystratis.api.global_responsemodels import AddressDescriptor, UtxoDescriptor
from pystratis.core.types import Address, Money, hexstr, uint256
from pydantic import SecretStr
from pystratis.core.networks import CirrusMain, StraxMain, StraxRegTest, Ethereum, StraxTest, CirrusTest


class Wallet(APIRequest, metaclass=EndpointRegister):
    """Implements the wallet api endpoints."""

    route = '/api/wallet'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/mnemonic')
    def mnemonic(self, language: str = 'English', word_count: int = 12, **kwargs) -> List[str]:
        """Generates a mnemonic to use for an HD wallet.
        For more information about mnemonics, see BIP39_.

        Args:
            language (str): The language used to generate mnemonic.
            word_count (int): Count of words needs to be generated.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[str]: The generated mnemonic.

        Raises:
            APIError: Error thrown by node API. See message for details.

        .. _BIP39: https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki
        """
        request_model = MnemonicRequest(
            language=language,
            word_count=word_count
        )
        data = self.get(request_model, **kwargs)
        return data.split(' ')

    @endpoint(f'{route}/create')
    def create(self,
               name: str,
               password: str, 
               passphrase: str, 
               mnemonic: Optional[str] = None,
               **kwargs) -> List[str]:
        """Creates a new wallet on this full node.

        Args:
            mnemonic (str, optional): The mnemonic used to create a HD wallet. If not specified, it will be randomly generated underhood.
            password (str): The password for a wallet to be created.
            passphrase (str): The passphrase used in master key generation.
            name: (str): The name for a wallet to be created.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[str]: The mnemonic used to generate this HD wallet.
        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = CreateRequest(
            mnemonic=mnemonic,
            password=SecretStr(password),
            passphrase=SecretStr(passphrase),
            name=name
        )
        data = self.post(request_model, **kwargs)
        return data.split(' ')

    @endpoint(f'{route}/signmessage')
    def sign_message(self, 
                     wallet_name: str,
                     password: str,
                     external_address: Union[Address, str],
                     message: str,
                     **kwargs) -> str:
        """Signs a message and returns the signature.

        Args:
            wallet_name (str): The name of the wallet to sign message with.
            password (str): The password of the wallet to sign message with.
            external_address (Address, str): The external address of a private key used to sign message.
            message (str): The message to be signed.
            **kwargs: Extra keyword arguments. 

        Returns:
            str: The signature of the message.
        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(external_address, str):
            external_address = Address(address=external_address, network=self._network)
        request_model = SignMessageRequest(
            wallet_name=wallet_name,
            password=SecretStr(password),
            external_address=external_address,
            message=message
        )
        data = self.post(request_model, **kwargs)
        return data

    @endpoint(f'{route}/pubkey')
    def pubkey(self, 
               wallet_name: str,
               external_address: Union[Address, str],
               **kwargs) -> PubKey:
        """Gets the public key for an address.

        Args:
            wallet_name (str): The name of the wallet to search for pubkey in.
            external_address (Address, str): The external address of a wanted pubkey.
            **kwargs: Extra keyword arguments. 

        Returns:
            PubKey: The requested public key.
        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(external_address, str):
            external_address = Address(address=external_address, network=self._network)
        request_model = PubKeyRequest(
            wallet_name=wallet_name,
            external_address=external_address
        )
        data = self.post(request_model, **kwargs)
        return PubKey(data)

    @endpoint(f'{route}/verifymessage')
    def verify_message(self,
                       signature: str,
                       external_address: Union[Address, str],
                       message: str,
                       **kwargs) -> bool:
        """Verifies the signature of a message.

        Args:
            signature (str): The signature to be verified.
            external_address (Address, str): The address of the signer.
            message (str): The message that was signed.
            **kwargs: Extra keyword arguments. 

        Returns:
            bool: True if signature is verified, False otherwise.
        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(external_address, str):
            external_address = Address(address=external_address, network=self._network)
        request_model = VerifyMessageRequest(
            signature=signature,
            external_address=external_address,
            message=message
        )
        data = self.post(request_model, **kwargs)
        return data

    @endpoint(f'{route}/load')
    def load(self,
             name: str,
             password: str,
             **kwargs) -> None:
        """Loads a previously created wallet.

        Args:
            name (str): The wallet name to load.
            password (str): The wallet password.
            **kwargs: Extra keyword arguments. 

        Returns:
            None
        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = LoadRequest(name=name, password=password)
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/recover')
    def recover(self,
                mnemonic: str,
                password: str,
                passphrase: str,
                name: str,
                creation_date: str = None,
                **kwargs) -> None:
        """Recovers an existing wallet.

        Args:
            mnemonic (str): A mnemonic for initializing a wallet.
            password (str): The password for the wallet.
            passphrase (str): The passphrase for the wallet.
            name (str): The name for the wallet.
            creation_date (str, datetime, optional): An estimate of the wallet creation date.
            **kwargs: Extra keyword arguments. 

        Returns:
            None
        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = RecoverRequest(
            mnemonic=mnemonic,
            password=password,
            passphrase=passphrase,
            name=name,
            creation_date=creation_date
        )
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/recover-via-extpubkey')
    def recover_via_extpubkey(self,
                              extpubkey: Union[ExtPubKey, str, hexstr],
                              account_index: int,
                              name: str,
                              creation_date: str,
                              **kwargs) -> None:
        """Recovers a wallet using its extended public key.

        Args:
            extpubkey (ExtPubKey, str, hexstr): The extpubkey for the recovered wallet.
            account_index (int): The account index.
            name (str): The wallet name.
            creation_date (str, datetime, optional): An estimate of the wallet creation date.
            **kwargs: Extra keyword arguments. 

        Returns:
            None
        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(extpubkey, (str, hexstr)):
            extpubkey = ExtPubKey(extpubkey)
        request_model = ExtPubRecoveryRequest(
            extpubkey=extpubkey,
            account_index=account_index,
            name=name,
            creation_date=creation_date
        )
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/general-info')
    def general_info(self, name: str, **kwargs) -> WalletGeneralInfoModel:
        """Gets some general information about a wallet.

        Args:
            name (str): The wallet name.
            **kwargs: Extra keyword arguments. 

        Returns:
            WalletGeneralInfoModel: General information about the wallet.
        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = GeneralInfoRequest(name=name)
        data = self.get(request_model, **kwargs)
        return WalletGeneralInfoModel(**data)

    @endpoint(f'{route}/transactioncount')
    def transaction_count(self,
                          wallet_name: str,
                          account_name: str = 'account 0',
                          **kwargs) -> int:
        """Get the transaction count for the specified Wallet and Account.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            **kwargs: Extra keyword arguments. 

        Returns:
            int: The number of transactions.
        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = AccountRequest(wallet_name=wallet_name, account_name=account_name)
        data = self.get(request_model, **kwargs)
        return data['transactionCount']

    @endpoint(f'{route}/history')
    def history(self,
                wallet_name: str,
                account_name: str = 'account 0',
                address: Union[Address, str] = None,
                skip: int = 0,
                take: int = None,
                prev_output_tx_time: int = None,
                prev_output_index: int = None,
                search_query: str = None,
                **kwargs) -> WalletHistoryModel:
        """Gets the history of a wallet.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            address (Address, str, optional): The address to query the history.
            skip (conint(ge=0), optional): The number of history items to skip.
            take (conint(ge=0), optional): The number of history items to take.
            prev_output_tx_time (conint(ge=0), optional): The previous output transaction time.
            prev_output_index (conint(ge=0), optional): The previous output transaction index.
            search_query (str, optional): A search query.
            **kwargs: Extra keyword arguments. 

        Returns:
            WalletHistoryModel: The wallet history.
        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(address, str):
            address = Address(address=address, network=self._network)
        request_model = HistoryRequest(
            wallet_name=wallet_name,
            account_name=account_name,
            address=address,
            skip=skip,
            take=take,
            prev_output_tx_time=prev_output_tx_time,
            prev_output_index=prev_output_index,
            search_query=search_query
        )
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
    def balance(self,
                wallet_name: str,
                account_name: str = 'account 0',
                include_balance_by_address: bool = False,
                **kwargs) -> WalletBalanceModel:
        """Gets the balance of a wallet in STRAX (or sidechain coin). Both the confirmed and unconfirmed balance are returned.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            include_balance_by_address (bool, optional): If true, includes detailed information about balances by address. Default=False.
            **kwargs: Extra keyword arguments. 

        Returns:
            WalletBalanceModel: The wallet balance.
        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = BalanceRequest(wallet_name=wallet_name, account_name=account_name, include_balance_by_address=include_balance_by_address)
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
    def received_by_address(self,
                            address: Union[Address, str],
                            **kwargs) -> AddressBalanceModel:
        """Retrieves transactions received by the specified address.

        Args:
            address (Address): The address to query.
            **kwargs: Extra keyword arguments. 

        Returns:
            AddressBalanceModel: The transactions associated with the address.
        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(address, str):
            address = Address(address=address, network=self._network)
        request_model = ReceivedByAddressRequest(address=address)
        data = self.get(request_model, **kwargs)
        data['address'] = Address(address=data['address'], network=self._network)
        data['amountConfirmed'] = Money.from_satoshi_units(data['amountConfirmed'])
        data['amountUnconfirmed'] = Money.from_satoshi_units(data['amountUnconfirmed'])
        data['spendableAmount'] = Money.from_satoshi_units(data['spendableAmount'])
        return AddressBalanceModel(**data)

    @endpoint(f'{route}/maxbalance')
    def max_balance(self,
                    wallet_name: str,
                    fee_type: str,
                    account_name: str = 'account 0',
                    allow_unconfirmed: bool = False,
                    **kwargs) -> MaxSpendableAmountModel:
        """Gets the maximum spendable balance for an account along with the fee required to spend it.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            fee_type (str): The fee type. Allowed [low, medium, high]
            allow_unconfirmed (bool, optional): If True, allow unconfirmed utxo in request. Default=False.
            **kwargs: Extra keyword arguments. 

        Returns:
            MaxSpendableAmountModel: Information about the maximum spendable amount and fee to send.
        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = MaxBalanceRequest(
            wallet_name=wallet_name,
            account_name=account_name,
            fee_type=fee_type,
            allow_unconfirmed=allow_unconfirmed
        )
        data = self.get(request_model, **kwargs)
        data['maxSpendableAmount'] = Money.from_satoshi_units(data['maxSpendableAmount'])
        data['fee'] = Money.from_satoshi_units(data['fee'])
        return MaxSpendableAmountModel(**data)

    @endpoint(f'{route}/spendable-transactions')
    def spendable_transactions(self,
                               wallet_name: str,
                               account_name: str = 'account 0',
                               min_confirmations: int = 0,
                               **kwargs) -> SpendableTransactionsModel:
        """Gets the spendable transactions for an account with the option to specify how many confirmations a transaction needs to be included.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            min_confirmations (int, optional): Get spendable transactions less this value from chain tip. Default=0.
            **kwargs: Extra keyword arguments. 

        Returns:
            SpendableTransactionsModel: Spendable transactions.
        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = SpendableTransactionsRequest(
            wallet_name=wallet_name,
            account_name=account_name,
            min_confirmations=min_confirmations
        )
        data = self.get(request_model, **kwargs)
        for i in range(len(data['transactions'])):
            data['transactions'][i]['amount'] = Money.from_satoshi_units(data['transactions'][i]['amount'])
            data['transactions'][i]['address'] = Address(
                address=data['transactions'][i]['address'],
                network=self._network
            )
        return SpendableTransactionsModel(**data)

    @endpoint(f'{route}/estimate-txfee')
    def estimate_txfee(self,
                       wallet_name: str,
                       outpoints: List[Outpoint],
                       recipients: List[Recipient],
                       op_return_data: str = None,
                       op_return_amount: Money = None,
                       fee_type: str = None,
                       allow_unconfirmed: bool = False,
                       shuffle_outputs: bool = False,
                       change_address: Address = None,
                       account_name: str = 'account 0',
                       **kwargs) -> Money:
        """Gets a fee estimate for a specific transaction.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            outpoints (List[Outpoint]): A list of outpoints to include in the transaction.
            recipients (List[Recipient]): A list of recipients with amounts.
            op_return_data (str, optional): The OP_RETURN data.
            op_return_amount (Money, int, float, Decimal, optional): The amount to burn in OP_RETURN.
            fee_type (str, optional): The fee type. Allowed [low, medium, high]
            allow_unconfirmed (bool, optional): If True, includes unconfirmed outputs. Default=False.
            shuffle_outputs (bool, optional): If True, shuffle outputs. Default=False.
            change_address (Address, str, optional): Specify a change address. If not set, a new change address is used.
            **kwargs: Extra keyword arguments. 

        Returns:
            Money: An estimate of the transaction fee.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(change_address, str):
            change_address = Address(address=change_address, network=self._network)
        request_model = EstimateTxFeeRequest(
            wallet_name=wallet_name,
            account_name=account_name,
            outpoints=outpoints,
            recipients=recipients,
            op_return_data=op_return_data,
            op_return_amount=Money(op_return_amount) if op_return_amount is not None else None,
            fee_type=fee_type,
            allow_unconfirmed=allow_unconfirmed,
            shuffle_outputs=shuffle_outputs,
            change_address=change_address
        )
        data = self.post(request_model, **kwargs)
        return Money.from_satoshi_units(data)

    @endpoint(f'{route}/build-transaction')
    def build_transaction(self,
                          wallet_name: str,
                          password: str,
                          outpoints: List[Outpoint],
                          recipients: List[Recipient],
                          fee_amount: Union[Money, int, float, Decimal] = None,
                          segwit_change_address: bool = False,
                          op_return_data: str = None,
                          op_return_amount: Union[Money, int, float, Decimal] = None,
                          fee_type: str = None,
                          allow_unconfirmed: bool = False,
                          shuffle_outputs: bool = False,
                          account_name: str = 'account 0',
                          change_address: Union[Address, str] = None,
                          **kwargs) -> BuildTransactionModel:
        """Builds a transaction and returns the hex to use when executing the transaction.

        Args:
            fee_amount (Money, int, float, Decimal, optional): The fee amount. Cannot be set with fee_type.
            password (str): The password.
            segwit_change_address (bool, optional): If True, the change address is a segwit address. Default=False.
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            outpoints (List[Outpoint]): A list of outpoints to include in the transaction.
            recipients (List[Recipient]): A list of recipients with amounts.
            op_return_data (str, optional): The OP_RETURN data.
            op_return_amount (Money, int, float, Decimal, optional): The amount to burn in OP_RETURN.
            fee_type (str, optional): The fee type. Allowed [low, medium, high]
            allow_unconfirmed (bool, optional): If True, includes unconfirmed outputs. Default=False.
            shuffle_outputs (bool, optional): If True, shuffle outputs. Default=False.
            change_address (Address, str, optional): Specify a change address. If not set, a new change address is used.
            **kwargs: Extra keyword arguments. 

        Returns:
            BuildTransactionModel: A built transaction.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(change_address, str):
            change_address = Address(address=change_address, network=self._network)
        request_model = BuildTransactionRequest(
            fee_amount=Money(fee_amount) if fee_amount is not None else None,
            password=password,
            segwit_change_address=segwit_change_address,
            wallet_name=wallet_name,
            account_name=account_name,
            outpoints=outpoints,
            recipients=recipients,
            op_return_data=op_return_data,
            op_return_amount=Money(op_return_amount) if op_return_amount is not None else None,
            fee_type=fee_type,
            allow_unconfirmed=allow_unconfirmed,
            shuffle_outputs=shuffle_outputs,
            change_address=change_address
        )
        data = self.post(request_model, **kwargs)
        data['fee'] = Money.from_satoshi_units(data['fee'])
        return BuildTransactionModel(**data)

    @endpoint(f'{route}/build-interflux-transaction')
    def build_interflux_transaction(self,
                                    wallet_name: str,
                                    password: str,
                                    destination_chain: int,
                                    destination_address: Union[Address, str],
                                    outpoints: List[Outpoint],
                                    recipients: List[Recipient],
                                    fee_amount: Union[Money, int, float, Decimal] = None,
                                    segwit_change_address: bool = False,
                                    op_return_data: str = None,
                                    op_return_amount: Union[Money, int, float, Decimal] = None,
                                    fee_type: str = None,
                                    allow_unconfirmed: bool = False,
                                    shuffle_outputs: bool = False,
                                    account_name: str = 'account 0',
                                    change_address: Union[Address, str] = None,
                                    **kwargs) -> BuildTransactionModel:
        """Builds a transaction and returns the hex to use when executing the transaction.

        Args:
            destination_chain (int): Enumeration representing the destination chain.
            destination_address (Address, str): The destination address.
            fee_amount (Money, int, float, Decimal, optional): The fee amount. Cannot be set with fee_type.
            password (str): The password.
            segwit_change_address (bool, optional): If True, the change address is a segwit address.
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            outpoints (List[Outpoint]): A list of outpoints to include in the transaction.
            recipients (List[Recipient]): A list of recipients with amounts.
            op_return_data (str, optional): The OP_RETURN data.
            op_return_amount (Money, int, float, Decimal, optional): The amount to burn in OP_RETURN.
            fee_type (str, optional): The fee type. Allowed [low, medium, high]
            allow_unconfirmed (bool, optional): If True, includes unconfirmed outputs. Default=False.
            shuffle_outputs (bool, optional): If True, shuffle outputs. Default=False.
            change_address (Address, str, optional): Specify a change address. If not set, a new change address is used.
            **kwargs: Extra keyword arguments. 

        Returns:
            BuildTransactionModel: A built interflux transaction.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(change_address, str):
            change_address = Address(address=change_address, network=self._network)
        if isinstance(destination_address, str):
            if destination_chain == 0:
                if isinstance(self._network, (StraxMain, CirrusMain)):
                    network = StraxMain()
                elif isinstance(self._network, (StraxTest, CirrusTest)):
                    network = StraxTest()
                else:
                    network = StraxRegTest()
            elif destination_chain == 1:
                network = Ethereum()
            else:
                raise NotImplementedError('Only transfers to Strax and Ethereum are supported currently.')
            destination_address = Address(address=destination_address, network=network)
        request_model = BuildInterfluxTransactionRequest(
            fee_amount=Money(fee_amount) if fee_amount is not None else None,
            password=password,
            destination_chain=destination_chain,
            destination_address=destination_address,
            segwit_change_address=segwit_change_address,
            wallet_name=wallet_name,
            account_name=account_name,
            outpoints=outpoints,
            recipients=recipients,
            op_return_data=op_return_data,
            op_return_amount=Money(op_return_amount) if op_return_amount is not None else None,
            fee_type=fee_type,
            allow_unconfirmed=allow_unconfirmed,
            shuffle_outputs=shuffle_outputs,
            change_address=change_address
        )
        data = self.post(request_model, **kwargs)
        data['fee'] = Money.from_satoshi_units(data['fee'])
        return BuildTransactionModel(**data)

    @endpoint(f'{route}/send-transaction')
    def send_transaction(self,
                         transaction_hex: Union[str, hexstr],
                         **kwargs) -> WalletSendTransactionModel:
        """Sends a transaction that has already been built.

        Args:
            transaction_hex (hexstr, str): The hexified transaction.
            **kwargs: Extra keyword arguments. 

        Returns:
            WalletSendTransactionModel: Information about a sent transaction.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(transaction_hex, str):
            transaction_hex = hexstr(transaction_hex)
        request_model = SendTransactionRequest(transaction_hex=transaction_hex)
        data = self.post(request_model, **kwargs)
        for i in range(len(data['outputs'])):
            if 'address' in data['outputs'][i]:
                data['outputs'][i]['address'] = Address(address=data['outputs'][i]['address'], network=self._network)
                data['outputs'][i]['amount'] = Money.from_satoshi_units(data['outputs'][i]['amount'])
            data['outputs'][i] = TransactionOutputModel(**data['outputs'][i])
        return WalletSendTransactionModel(**data)

    @endpoint(f'{route}/list-wallets')
    def list_wallets(self, **kwargs) -> dict:
        """Lists all the files found in the database

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            dict: A list of wallets.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return data

    @endpoint(f'{route}/account')
    def account(self,
                wallet_name: str,
                password: str,
                **kwargs) -> str:
        """Creates a new account for a wallet.

        Args:
            password (str): The wallet password.
            wallet_name (str): The wallet name.
            **kwargs: Extra keyword arguments. 

        Returns:
            str: The newly created account name.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = GetUnusedAccountRequest(
            wallet_name=wallet_name,
            password=password
        )
        data = self.post(request_model, **kwargs)
        return data

    @endpoint(f'{route}/accounts')
    def accounts(self,
                 wallet_name: str,
                 **kwargs) -> List[str]:
        """Gets a list of accounts for the specified wallet.

        Args:
            wallet_name (str): The wallet name.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[str]: A list of accounts.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = GetAccountsRequest(wallet_name=wallet_name)
        data = self.get(request_model, **kwargs)
        return data

    @endpoint(f'{route}/unusedaddress')
    def unused_address(self,
                       wallet_name: str,
                       account_name: str = 'account 0',
                       segwit: bool = False,
                       **kwargs) -> Address:
        """Gets an unused address (in the Base58 format) for a wallet account.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            segwit (bool, optional): If True, get a segwit address. Default=False.
            **kwargs: Extra keyword arguments. 

        Returns:
            Address: An unused address.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = GetUnusedAddressRequest(
            wallet_name=wallet_name,
            account_name=account_name,
            segwit=segwit
        )
        data = self.get(request_model, **kwargs)
        return Address(address=data, network=self._network)

    @endpoint(f'{route}/unusedaddresses')
    def unused_addresses(self,
                         wallet_name: str,
                         count: int,
                         account_name: str = 'account 0',
                         segwit: bool = False,
                         **kwargs) -> List[Address]:
        """Gets a specified number of unused addresses (in the Base58 format) for a wallet account.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            count (int): The number of addresses to get.
            segwit (bool, optional): If True, get a segwit address. Default=False.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[Address]: A list of unused addresses.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = GetUnusedAddressesRequest(
            wallet_name=wallet_name,
            count=count,
            account_name=account_name,
            segwit=segwit
        )
        data = self.get(request_model, **kwargs)
        return [Address(address=x, network=self._network) for x in data]

    @endpoint(f'{route}/newaddresses')
    def new_addresses(self,
                      wallet_name: str,
                      count: int,
                      account_name: str = 'account 0',
                      segwit: bool = False,
                      **kwargs) -> List[Address]:
        """Gets a specified number of new addresses (in the Base58 format) for a wallet account.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            count (conint(ge=1)): The number of addresses to get.
            segwit (bool, optional): If True, get a segwit address. Default=False.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[Address]: A new address.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = GetNewAddressesRequest(
            wallet_name=wallet_name,
            count=count,
            account_name=account_name,
            segwit=segwit
        )
        data = self.get(request_model, **kwargs)
        return [Address(address=x, network=self._network) for x in data]

    @endpoint(f'{route}/addresses')
    def addresses(self,
                  wallet_name: str,
                  account_name: str = 'account 0',
                  segwit: bool = False,
                  **kwargs) -> AddressesModel:
        """Gets all addresses for a wallet account.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            segwit (bool, optional): If True, gets a segwit address. Default=False.
            **kwargs: Extra keyword arguments. 

        Returns:
            AddressesModel: All addresses associated with the account given.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = GetAddressesRequest(
            wallet_name=wallet_name,
            account_name=account_name,
            segwit=segwit
        )
        data = self.get(request_model, **kwargs)
        for i in range(len(data['addresses'])):
            data['addresses'][i]['address'] = Address(address=data['addresses'][i]['address'], network=self._network)
            data['addresses'][i]['amountConfirmed'] = Money.from_satoshi_units(data['addresses'][i]['amountConfirmed'])
            data['addresses'][i]['amountUnconfirmed'] = Money.from_satoshi_units(data['addresses'][i]['amountUnconfirmed'])
        return AddressesModel(**data)

    @endpoint(f'{route}/remove-transactions')
    def remove_transactions(self,
                            wallet_name: str,
                            ids: List[Union[uint256, str]] = None,
                            from_date: str = None,
                            remove_all: bool = False,
                            resync: bool = True,
                            **kwargs) -> List[RemovedTransactionModel]:
        """Removes transactions from the wallet.

        Args:
            wallet_name (str): The wallet name.
            ids (List[uint256, str], optional): A list of transaction ids to remove.
            from_date (str, optional): An option to remove transactions after given date.
            remove_all (bool, optional): An option to remove all transactions. Default=False.
            resync (bool, optional): If True, resyncs wallet after items removed. Default=True.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[RemovedTransactionModel]: A list of removed transactions.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if ids is not None:
            for i in range(len(ids)):
                if isinstance(ids[i], str):
                    ids[i] = uint256(ids[i])
        request_model = RemoveTransactionsRequest(
            wallet_name=wallet_name,
            ids=ids,
            from_date=from_date,
            remove_all=remove_all,
            resync=resync
        )
        data = self.delete(request_model, **kwargs)
        return [RemovedTransactionModel(**x) for x in data]

    @endpoint(f'{route}/remove-wallet')
    def remove_wallet(self,
                      wallet_name: str,
                      **kwargs) -> None:
        """Remove a wallet

        Args:
            wallet_name (str): The wallet name.
            **kwargs: Extra keyword arguments. 

        Returns:
            None

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = RemoveWalletRequest(wallet_name=wallet_name)
        self.delete(request_model, **kwargs)

    @endpoint(f'{route}/extpubkey')
    def extpubkey(self,
                  wallet_name: str,
                  account_name: str = 'account 0',
                  **kwargs) -> ExtPubKey:
        """Gets the extended public key of a specified wallet account.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            **kwargs: Extra keyword arguments. 

        Returns:
            ExtPubKey

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = ExtPubKeyRequest(
            wallet_name=wallet_name,
            account_name=account_name
        )
        data = self.get(request_model, **kwargs)
        return ExtPubKey(data)

    @endpoint(f'{route}/privatekey')
    def private_key(self,
                    password: str,
                    wallet_name: str,
                    address: Union[Address, str],
                    **kwargs) -> Key:
        """Gets the private key of a specified wallet address.

        Args:
            password (str): The wallet password.
            wallet_name (str): The wallet name.
            address (Address, str): The address to request a private key for.
            **kwargs: Extra keyword arguments. 

        Returns:
            Key: The private key.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(address, str):
            address = Address(address=address, network=self._network)
        request_model = PrivateKeyRequest(
            password=password,
            wallet_name=wallet_name,
            address=address
        )
        data = self.post(request_model, **kwargs)
        return Key(data)

    @endpoint(f'{route}/sync')
    def sync(self,
             block_hash: Union[uint256, str],
             **kwargs) -> None:
        """Requests the node resyncs from a block specified by its block hash.

        Args:
            block_hash (uint256, str): The hash to start syncing from.
            **kwargs: Extra keyword arguments. 

        Returns:
            None

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(block_hash, str):
            block_hash = uint256(block_hash)
        request_model = SyncRequest(block_hash=block_hash)
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/sync-from-date')
    def sync_from_date(self,
                       wallet_name: str,
                       date: str,
                       all_transactions: bool = True,
                       **kwargs) -> None:
        """Request the node resyncs starting from a given date and time.

        Args:
            date (str): The date to sync from in YYYY-MM-DDTHH:MM:SS format.
            all_transactions (bool, optional): If True, sync all transactions. Default=True.
            wallet_name (str): The wallet name.
            **kwargs: Extra keyword arguments. 

        Returns:
            None

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = SyncFromDateRequest(
            wallet_name=wallet_name,
            date=date,
            all_transactions=all_transactions
        )
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/wallet-stats')
    def wallet_stats(self,
                     wallet_name: str,
                     account_name: str = 'account 0',
                     min_confirmations: int = 0,
                     verbose: bool = True,
                     **kwargs) -> WalletStatsModel:
        """Retrieves information about the wallet.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            min_confirmations (int, optional): Include transaction less this amount from the chain tip. Default=0.
            verbose (bool, optional): If True, give verbose response. Default=True.
            **kwargs: Extra keyword arguments. 

        Returns:
            WalletStatsModel: Wallet statistical information.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = StatsRequest(
            wallet_name=wallet_name,
            account_name=account_name,
            min_confirmations=min_confirmations,
            verbose=verbose
        )
        data = self.get(request_model, **kwargs)
        for i in range(len(data['utxoAmounts'])):
            data['utxoAmounts'][i]['amount'] = Money.from_satoshi_units(data['utxoAmounts'][i]['amount'])
        return WalletStatsModel(**data)

    @endpoint(f'{route}/splitcoins')
    def split_coins(self,
                    wallet_name: str,
                    wallet_password: str,
                    total_amount_to_split: Union[Money, int, float, Decimal],
                    utxos_count: int,
                    account_name: str = 'account 0',
                    **kwargs) -> WalletSendTransactionModel:
        """Creates requested amount of UTXOs each of equal value and sends the transaction.

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            wallet_password (str): The wallet password.
            total_amount_to_split (Money, int, float, Decimal): The total amount to split.
            utxos_count (int): The number of utxos to create. (Must be greater than 2).
            **kwargs: Extra keyword arguments. 

        Returns:
            WalletSendTransactionModel: Information about the sent transaction.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = SplitCoinsRequest(
            wallet_name=wallet_name,
            wallet_password=wallet_password,
            total_amount_to_split=total_amount_to_split,
            utxos_count=utxos_count,
            account_name=account_name
        )
        data = self.post(request_model, **kwargs)
        for i in range(len(data['outputs'])):
            data['outputs'][i]['address'] = Address(address=data['outputs'][i]['address'], network=self._network)
            data['outputs'][i]['amount'] = Money.from_satoshi_units(data['outputs'][i]['amount'])
            data['outputs'][i] = TransactionOutputModel(**data['outputs'][i])
        return WalletSendTransactionModel(**data)

    @endpoint(f'{route}/distribute-utxos')
    def distribute_utxos(self,
                         wallet_name: str,
                         wallet_password: str,
                         utxos_count: int,
                         utxo_per_transaction: int,
                         outpoints: List[Outpoint],
                         account_name: str = 'account 0',
                         use_unique_address_per_utxo: bool = True,
                         reuse_addresses: bool = True,
                         use_change_addresses: bool = False,
                         timestamp_difference_between_transactions: int = 0,
                         min_confirmations: int = 0,
                         dry_run: bool = True,
                         **kwargs) -> DistributeUtxoModel:
        """Splits and distributes UTXOs across wallet addresses

        Args:
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            wallet_password (str): The wallet password.
            use_unique_address_per_utxo (bool, optional): If True, uses a unique address for each utxo. Default=True.
            reuse_addresses (bool, optional): If True, reuses addresses. Default=True.
            use_change_addresses (bool, optional): If True, use change addresses. Default=False.
            utxos_count (int): The number of utxos to create.
            utxo_per_transaction (int): The number of utxos per transaction.
            timestamp_difference_between_transactions (int, optional): The number of seconds between transactions. Default=0.
            min_confirmations (int, optional): The minimum number of confirmations to include in transaction. Default=0.
            outpoints (List[Outpoint]): A list of outpoints to include in the transaction.
            dry_run (bool, optional): If True, simulate transaction. Default=True.
            **kwargs: Extra keyword arguments. 

        Returns:
            DistributeUtxoModel: Information about the distribute utxo transaction.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = DistributeUTXOsRequest(
            wallet_name=wallet_name,
            wallet_password=wallet_password,
            account_name=account_name,
            use_unique_address_per_utxo=use_unique_address_per_utxo,
            reuse_addresses=reuse_addresses,
            use_change_addresses=use_change_addresses,
            utxos_count=utxos_count,
            utxo_per_transaction=utxo_per_transaction,
            timestamp_difference_between_transactions=timestamp_difference_between_transactions,
            min_confirmations=min_confirmations,
            outpoints=outpoints,
            dry_run=dry_run
        )
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
    def sweep(self,
              private_keys: List[Union[Key, str]],
              destination_address: Union[Address, str],
              broadcast: bool = False,
              **kwargs) -> List[uint256]:
        """Sweeps a wallet to specified address.

        Args:
            private_keys (List[Key, str]): A list of private keys to sweep.
            destination_address (Address, str): The address to sweep the coins to.
            broadcast (bool, optional): Broadcast transaction after creation. Default=False.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[uint256]: A list of transactions for the sweep.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(destination_address, str):
            destination_address = Address(address=destination_address, network=self._network)
        for i in range(len(private_keys)):
            if isinstance(private_keys[i], str):
                private_keys[i] = Key(private_keys[i])
        request_model = SweepRequest(
            private_keys=private_keys,
            destination_address=destination_address,
            broadcast=broadcast
        )
        data = self.post(request_model, **kwargs)
        return [uint256(x) for x in data]

    @endpoint(f'{route}/build-offline-sign-request')
    def build_offline_sign_request(self,
                                   wallet_name: str,
                                   outpoints: List[Outpoint],
                                   recipients: List[Recipient],
                                   fee_amount: Union[Money, int, float, Decimal] = None,
                                   op_return_data: str = None,
                                   op_return_amount: Union[Money, int, float, Decimal] = None,
                                   fee_type: str = None,
                                   allow_unconfirmed: bool = False,
                                   shuffle_outputs: bool = False,
                                   account_name: str = 'account 0',
                                   change_address: Union[Address, str] = None,
                                   **kwargs) -> BuildOfflineSignModel:
        """Builds an offline sign request for a transaction.

        Args:
            fee_amount (Money, int, float, Decimal): The fee amount. Cannot be set with fee_type.
            wallet_name (str): The wallet name.
            account_name (str, optional): The account name. Default='account 0'.
            outpoints (List[Outpoint]): A list of outputs to use for the transaction.
            recipients (List[Recipient]): A list of recipients, including amounts.
            op_return_data (str, optional): The OP_RETURN data.
            op_return_amount (Money, optional): The amount to burn in OP_RETURN.
            fee_type (str, optional): The fee type. Allowed [low, medium, high]
            allow_unconfirmed (bool, optional): If True, includes unconfirmed outputs. Default=False.
            shuffle_outputs (bool, optional): If True, shuffle outputs. Default=False.
            change_address (Address, optional): Specify a change address. If not set, a new change address is used.
            **kwargs: Extra keyword arguments. 

        Returns:
            BuildOfflineSignModel: A built transaction that can be signed offline.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(change_address, str):
            change_address = Address(address=change_address, network=self._network)
        request_model = BuildOfflineSignRequest(
            fee_amount=Money(fee_amount) if fee_amount is not None else None,
            wallet_name=wallet_name,
            account_name=account_name,
            outpoints=outpoints,
            recipients=recipients,
            op_return_data=op_return_data,
            op_return_amount=Money(op_return_amount) if op_return_amount is not None else None,
            fee_type=fee_type,
            allow_unconfirmed=allow_unconfirmed,
            shuffle_outputs=shuffle_outputs,
            change_address=change_address
        )
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
    def offline_sign_request(self,
                             wallet_password: str,
                             wallet_name: str,
                             unsigned_transaction: Union[str, hexstr],
                             fee: Union[Money, int, float, Decimal],
                             utxos: List[UtxoDescriptor],
                             addresses: List[AddressDescriptor],
                             wallet_account: str = 'account 0',
                             **kwargs) -> BuildTransactionModel:
        """Build an offline sign request for a transaction. The resulting transaction hex can be broadcast.

        Args:
            wallet_password (str): The wallet password.
            wallet_name (str): The wallet name.
            wallet_account (str, optional): The account name. Default='account 0'.
            unsigned_transaction (hexstr, str): The unsigned transaction hexstr.
            fee (Money, int, float, Decimal): The fee.
            utxos (List[UtxoDescriptor]): A list of utxodescriptors.
            addresses (List[AddressDescriptor]): A list of addresses to send transactions.
            **kwargs: Extra keyword arguments. 

        Returns:
            BuildTransactionModel: A signed transaction that can be broadcast.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(unsigned_transaction, str):
            unsigned_transaction = hexstr(unsigned_transaction)
        request_model = OfflineSignRequest(
            wallet_password=wallet_password,
            wallet_name=wallet_name,
            wallet_account=wallet_account,
            unsigned_transaction=unsigned_transaction,
            fee=Money(fee),
            utxos=utxos,
            addresses=addresses
        )
        data = self.post(request_model, **kwargs)
        data['fee'] = Money.from_satoshi_units(data['fee'])
        return BuildTransactionModel(**data)

    @endpoint(f'{route}/consolidate')
    def consolidate(self,
                    wallet_password: str,
                    wallet_name: str,
                    destination_address: Union[Address, str],
                    utxo_value_threshold_in_satoshis: int,
                    wallet_account: str = 'account 0',
                    broadcast: bool = False,
                    **kwargs) -> hexstr:
        """Consolidate a wallet.

        utxo_value_threshold looks to consolidate any utxo amount below the threshold.

        Args:
            wallet_password (str): The wallet password.
            wallet_name (str): The wallet name.
            wallet_account (str, optional): The account name. Default='account 0'.
            destination_address (Address, str): The destination address.
            utxo_value_threshold_in_satoshis (int): The threshold where amounts below this amount will be consolidated. (min 1e8)
            broadcast (bool, optional): If True, broadcast consolidation transaction. Default=False.
            **kwargs: Extra keyword arguments. 

        Returns:
            hexstr: A consolidation transaction ready for broadcast.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(destination_address, str):
            destination_address = Address(address=destination_address, network=self._network)
        request_model = ConsolidateRequest(
            wallet_password=wallet_password,
            wallet_name=wallet_name,
            wallet_account=wallet_account,
            destination_address=destination_address,
            utxo_value_threshold_in_satoshis=utxo_value_threshold_in_satoshis,
            broadcast=broadcast
        )
        data = self.post(request_model, **kwargs)
        return hexstr(data)
