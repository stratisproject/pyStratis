from typing import Optional, List
from pydantic import Field, conint
from pystratis.api import Model
from pystratis.core.types import Address


# noinspection PyUnresolvedReferences
class ReceiptSearchRequest(Model):
    """A request model for the smartcontracts/receipt-search endpoint.

    Args:
        contract_address (Address): The address for the smart contract.
        event_name (str, optional): The event to search for.
        topics (List[str], optional): A list of topics to search for.
        from_block (conint(ge=0)): Block to start search from.
        to_block (conint(ge=0)): Block to search up to.
    """
    contract_address: Address = Field(alias='ContractAddress')
    event_name: Optional[str] = Field(alias='eventName')
    topics: Optional[List[str]]
    from_block: conint(ge=0) = Field(default=0, alias='fromBlock')
    to_block: Optional[conint(ge=0)] = Field(alias='toBlock')
