from typing import Optional
from pydantic import Field, conint
from pybitcoin import Model


class DeploymentFlagsModel(Model):
    """A DeploymentFlagsModel."""
    deployment_name: Optional[str] = Field(alias='deploymentName')
    deployment_index: Optional[conint(ge=0)] = Field(alias='deploymentIndex')
    state_value: Optional[conint(ge=0)] = Field(alias='stateValue')
    threshold_state: Optional[str] = Field(alias='thresholdState')
    height: Optional[conint(ge=0)]
    since_height: Optional[conint(ge=0)] = Field(alias='sinceHeight')
    confirmation_period: Optional[conint(ge=0)] = Field(alias='confirmationPeriod')
    period_start_height: Optional[conint(ge=0)] = Field(alias='periodStartHeight')
    period_end_height: Optional[conint(ge=0)] = Field(alias='periodEndHeight')
    votes: Optional[conint(ge=0)]
    blocks: Optional[conint(ge=0)]
    versions: Optional[dict]
    threshold: Optional[conint(ge=0)]
    time_start: Optional[str] = Field(alias='timeStart')
    time_time_out: Optional[str] = Field(alias='timeTimeOut')
