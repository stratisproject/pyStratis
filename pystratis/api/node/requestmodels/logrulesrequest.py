from typing import List
from pydantic import Field
from pystratis.api import LogRule, Model


# noinspection PyUnresolvedReferences
class LogRulesRequest(Model):
    """A request model for the node/logrules endpoint.

    Args:
        log_rules (List[LogRule]): A list of log rules to change.
    """
    log_rules: List[LogRule] = Field(alias='logRules')
