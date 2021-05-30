from pydantic import Field, conint
from pybitcoin import Model


class DeploymentFlagsModel(Model):
    """A DeploymentFlagsModel."""
    deployment_name: str = Field(alias='deploymentName')
    deployment_index: conint(ge=0) = Field(alias='deploymentIndex')
    state_value: conint(ge=0) = Field(alias='stateValue')
    threshold_state: str = Field(alias='thresholdState')
    height: conint(ge=0)
    since_height: conint(ge=0) = Field(alias='sinceHeight')
    confirmation_period: conint(ge=0) = Field(alias='confirmationPeriod')
    period_start_height: conint(ge=0) = Field(alias='periodStartHeight')
    period_end_height: conint(ge=0) = Field(alias='periodEndHeight')
    votes: conint(ge=0)
    blocks: conint(ge=0)
    versions: dict
    threshold: conint(ge=0)
    time_start: str = Field(alias='timeStart')
    time_time_out: str = Field(alias='timeTimeOut')
