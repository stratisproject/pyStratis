from typing import Optional, List
from pydantic import Field
from pystratis.api import Model
from pystratis.core import Key
from pystratis.core.types import Address


# noinspection PyUnresolvedReferences
class SweepRequest(Model):
    """A request model for the wallet/sweep endpoint.

    Args:
        private_keys (List[Key]): A list of private keys to sweep.
        destination_address (Address): The address to sweep the coins to.
        broadcast (bool, optional): Broadcast transaction after creation. Default=False.
    """
    private_keys: List[Key] = Field(alias='privateKeys')
    destination_address: Address = Field(alias='destinationAddress')
    broadcast: Optional[bool] = False
