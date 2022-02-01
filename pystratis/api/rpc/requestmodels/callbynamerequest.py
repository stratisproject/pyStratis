from typing import Optional
from pydantic import Field
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class CallByNameRequest(Model):
    """A request model for the rpc/callbyname endpoint.

    Args:
        method_name (str): The complete RPC command.
    """
    method_name: str = Field(alias='methodName')
