from typing import Optional
from pydantic import BaseModel, Field, conint


class WalletGeneralInfoModel(BaseModel):
    """A WalletGeneralInfoModel."""
    wallet_name: str = Field(alias='walletName')
    network: str
    creation_time: str = Field(alias='creationTime')
    is_decrypted: bool = Field(alias='isDecrypted')
    last_block_synced_height: Optional[conint(ge=0)] = Field(alias='lastBlockSyncedHeight')
    chain_tip: Optional[conint(ge=0)] = Field(alias='chainTip')
    is_chain_synced: bool = Field(alias='isChainSynced')
    connected_nodes: conint(ge=0) = Field(alias='connectedNodes')

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
