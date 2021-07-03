from pydantic import Field, BaseModel


class LogRule(BaseModel):
    """
    A log rule model.

    Args:
        rule_name (str): The name of rule.
        log_level (str): The mininal event level of event to be matched by this rule.
        filename (str): The name of the logfile for this rule.
        
    Note:
        More information about logging in Stratis Full Node can be found here__.

    .. __: https://github.com/stratisproject/StratisBitcoinFullNode/blob/master/Documentation/using-logging.md#using-logging
    """
    rule_name: str = Field(alias='ruleName')
    log_level: str = Field(alias='logLevel')
    filename: str

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs):
        return super().json(by_alias=True, exclude_none=True)
