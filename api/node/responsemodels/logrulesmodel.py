from pydantic import Field
from pybitcoin import Model


class LogRulesModel(Model):
    """A LogRulesModel."""
    rule_name: str = Field(alias='ruleName')
    log_level: str = Field(alias='logLevel')
    filename: str
