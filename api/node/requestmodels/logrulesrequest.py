from typing import List
from pydantic import Field
from pybitcoin import LogRule, Model


class LogRulesRequest(Model):
    """A LogRulesRequest."""
    log_rules: List[LogRule] = Field(alias='logRules')
