from typing import Optional
from pystratis.api import Model, FeatureInitializationState


class FeaturesDataModel(Model):
    """A FeaturesDataModel."""
    namespace: Optional[str]
    state: Optional[FeatureInitializationState]
