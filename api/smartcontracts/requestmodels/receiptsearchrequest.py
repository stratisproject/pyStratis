from typing import Optional, List
from pydantic import Field, conint
from pybitcoin import Model
from pybitcoin.types import Address


class ReceiptSearchRequest(Model):
    """A ReceiptSearchRequest."""
    contract_address: Address = Field(alias='ContractAddress')
    event_name: Optional[str] = Field(alias='eventName')
    topics: Optional[List[str]]
    from_block: conint(ge=0) = Field(default=0, alias='fromBlock')
    to_block: Optional[conint(ge=0)] = Field(alias='toBlock')
