from pystratis.api import Model
from pystratis.core import PubKey
from pydantic import Field


class PollsTipModel(Model):
    """A pydantic model representing the voting polls tip."""
    tip_height: int = Field(alias='tipHeight')
    """The tip height."""
    tip_height_percentage: int = Field(alias='tipHeightPercentage')
    """The tip height percentage."""
