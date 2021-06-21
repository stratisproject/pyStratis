from pydantic import Field, BaseModel


class LogRule(BaseModel):
    """A LogRule."""
    rule_name: str = Field(alias='ruleName')
    log_level: str = Field(alias='logLevel')

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs):
        return super().json(by_alias=True, exclude_none=True)
