from typing import List
from pydantic import Field, conint, Json
from pybitcoin import Model
from .transferinfomodel import TransferInfoModel
from .logmodel import LogModel


class LocalExecutionResultModel(Model):
    """A LocalExecutionResultModel."""
    internal_transfers: List[TransferInfoModel] = Field(alias='InternalTransfers')
    gas_consumed: conint(ge=0) = Field(alias='GasConsumed')
    revert: bool = Field(alias='Revert')
    error_message: str = Field(alias='ErrorMessage')
    return_obj: Json = Field(alias='Return')
    logs: List[LogModel] = Field(alias='Logs')
