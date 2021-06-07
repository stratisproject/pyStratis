from typing import List, Optional
from pydantic import Field, conint, Json
from pybitcoin import Model
from .transferinfomodel import TransferInfoModel
from .logmodel import LogModel


class LocalExecutionResultModel(Model):
    """A LocalExecutionResultModel."""
    internal_transfers: Optional[List[TransferInfoModel]] = Field(alias='InternalTransfers')
    gas_consumed: Optional[conint(ge=0)] = Field(alias='GasConsumed')
    revert: Optional[bool] = Field(alias='Revert')
    error_message: Optional[str] = Field(alias='ErrorMessage')
    return_obj: Optional[Json] = Field(alias='Return')
    logs: Optional[List[LogModel]] = Field(alias='Logs')
