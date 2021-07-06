from pydantic import Field
from pystratis.api import Model


class DeploymentFlagsModel(Model):
    """A pydantic model representing deployment flags."""
    deployment_name: str = Field(alias='deploymentName')
    """The deployment flag name."""
    deployment_index: int = Field(alias='deploymentIndex')
    """The deployment index."""
    state_value: int = Field(alias='stateValue')
    """The deployment flag state value."""
    threshold_state: str = Field(alias='thresholdState')
    """The deployment flag threshold state."""
    height: int
    """The block height."""
    since_height: int = Field(alias='sinceHeight')
    """The flag's activation height."""
    confirmation_period: int = Field(alias='confirmationPeriod')
    """The confirmation period size."""
    period_start_height: int = Field(alias='periodStartHeight')
    """The activation period start height."""
    period_end_height: int = Field(alias='periodEndHeight')
    """The activation period ending height."""
    votes: int
    """The number of votes."""
    blocks: int
    """Blocks."""
    versions: dict
    """Versions."""
    threshold: int
    """The threshold."""
    time_start: str = Field(alias='timeStart')
    """The start time."""
    time_time_out: str = Field(alias='timeTimeOut')
    """The timeout time."""
