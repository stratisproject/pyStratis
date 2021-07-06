from pystratis.api import Model, FeatureInitializationState


class FeaturesDataModel(Model):
    """A pydantic model for features data."""
    namespace: str
    """The feature namespace."""
    state: FeatureInitializationState
    """The feature initialization state."""
