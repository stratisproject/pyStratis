from typing import Optional
from pydantic import Field
from pystratis.core import Model


class LogRulesModel(Model):
    """A LogRulesModel."""
    rule_name: Optional[str] = Field(alias='ruleName')
    log_level: Optional[str] = Field(alias='logLevel')
    filename: Optional[str]
