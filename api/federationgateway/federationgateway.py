from typing import List, Union
from api import APIRequest, EndpointRegister, endpoint
from api.federationgateway.requestmodels import *
from api.federationgateway.responsemodels import *


class FederationGateway(APIRequest, metaclass=EndpointRegister):
    route = '/api/federationgateway'

    def __init__(self, **kwargs):
        super(FederationGateway, self).__init__(**kwargs)

    @endpoint(f'{route}/deposits')
    def deposits(self, request_model: DepositsRequest, **kwargs) -> List[MaturedBlockDepositsModel]:
        """Retrieves block deposits

        Args:
            request_model: DepositsRequest model
            **kwargs:

        Returns:
            List[MaturedBlockDepositsModel]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)
        serializable_result = SerializableResult(**data)

        return [MaturedBlockDepositsModel(**x) for x in serializable_result.value]

    @endpoint(f'{route}/transfer/pending')
    def pending_transfer(self, request_model: PendingTransferRequest, **kwargs) -> List[CrossChainTransferModel]:
        """Gets pending transfers

        Args:
            request_model: PendingTransferRequest model
            **kwargs:

        Returns:
            List[CrossChainTransferModel]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return [CrossChainTransferModel(**x) for x in data]

    @endpoint(f'{route}/transfer/fullysigned')
    def fullysigned_transfer(self, request_model: FullySignedTransferRequest, **kwargs) -> List[CrossChainTransferModel]:
        """Get fully signed transfers.

        Args:
            request_model: FullySignedTransferRequest model
            **kwargs:

        Returns:
            List[CrossChainTransferModel]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return [CrossChainTransferModel(**x) for x in data]

    @endpoint(f'{route}/member/info')
    def member_info(self, **kwargs) -> FederationMemberInfoModel:
        """Gets info on the state of a multisig member.

        Args:
            **kwargs:

        Returns:
            FederationMemberInfoModel

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return FederationMemberInfoModel(**data)

    @endpoint(f'{route}/info')
    def info(self, **kwargs) -> FederationGatewayInfoModel:
        """Gets info on the state of the federation.

        Args:
            **kwargs:

        Returns:
            FederationGatewayInfoModel

        Raises:
            APIError
        """
        data = self.get(**kwargs)

        return FederationGatewayInfoModel(**data)

    @endpoint(f'{route}/member/ip/add')
    def ip_add(self, request_model: MemberIPAddRequest, **kwargs) -> str:
        """Add a federation member's IP address to the federation IP list

        Args:
            request_model: MemberIPAddRequest model
            **kwargs:

        Returns:
            str

        Raises:
            APIError
        """
        data = self.put(request_model, **kwargs)

        return data

    @endpoint(f'{route}/member/ip/remove')
    def ip_remove(self, request_model: MemberIPRemoveRequest, **kwargs) -> str:
        """Remove a federation member's IP address to the federation IP list

        Args:
            request_model: MemberIPRemoveRequest model
            **kwargs:

        Returns:
            str

        Raises:
            APIError
        """
        data = self.put(request_model, **kwargs)

        return data

    @endpoint(f'{route}/member/ip/replace')
    def ip_add(self, request_model: MemberIPReplaceRequest, **kwargs) -> str:
        """Replace a federation member's IP from the federation IP list with another.

        Args:
            request_model: MemberIPReplaceRequest model
            **kwargs:

        Returns:
            str

        Raises:
            APIError
        """
        data = self.put(request_model, **kwargs)

        return data

    @endpoint(f'{route}/transfer/verify')
    def verify_transfer(self, request_model: VerifyTransferRequest, **kwargs) -> Union[str, ValidateTransactionResultModel]:
        """Validate a transfer transaction

        Args:
            request_model: VerifyTransferRequest model
            **kwargs:

        Returns:
            Union[str, ValidateTransactionResultModel]

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        if isinstance(data, str):
            return data
        return ValidateTransactionResultModel(**data)
