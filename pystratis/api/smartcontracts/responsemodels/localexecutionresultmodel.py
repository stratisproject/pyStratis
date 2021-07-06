from typing import List, Optional, Any
from pydantic import Field
from pystratis.api import Model
from .transferinfomodel import TransferInfoModel
from .logmodel import LogModel


class LocalExecutionResultModel(Model):
    """A pydantic model representing the result of a local smart contact execution call."""
    internal_transfers: Optional[List[TransferInfoModel]] = Field(alias='internalTransfers')
    """A list of internal transfers."""
    gas_consumed: int = Field(alias='gasConsumed')
    """The amount of gas consumed by the call."""
    revert: Optional[bool] = Field(alias='revert')
    """If true, call was not successful."""
    error_message: Optional[str] = Field(alias='errorMessage')
    """An error message, if thrown."""
    return_obj: Optional[Any] = Field(alias='return')
    """An optional return object."""
    logs: Optional[List[LogModel]]
    """An optional list of logs returned."""
