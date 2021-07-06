from pydantic import Field
from .model import Model


class LogRule(Model):
    """
    A log rule model.
        
    Note:
        More information about logging in Stratis Full Node can be found here__.

    .. __: https://github.com/stratisproject/StratisBitcoinFullNode/blob/master/Documentation/using-logging.md#using-logging
    """
    rule_name: str = Field(alias='ruleName')
    """The name of the log rule."""
    log_level: str = Field(alias='logLevel')
    """The log level."""
    filename: str
    """The log file name."""
