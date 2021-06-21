from typing import List, Optional, Any
from pydantic import Field, conint
from pybitcoin import Model
from .transferinfomodel import TransferInfoModel
from .logmodel import LogModel


class LocalExecutionResultModel(Model):
    """A LocalExecutionResultModel."""
    internal_transfers: Optional[List[TransferInfoModel]] = Field(alias='internalTransfers')
    gas_consumed: Optional[conint(ge=0)] = Field(alias='gasConsumed')
    revert: Optional[bool] = Field(alias='revert')
    error_message: Optional[str] = Field(alias='errorMessage')
    return_obj: Optional[Any] = Field(alias='return')
    logs: Optional[List[LogModel]]
