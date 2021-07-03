from typing import Optional
from pystratis.core import Model, FeatureInitializationState


class FeaturesDataModel(Model):
    """A FeaturesDataModel."""
    namespace: Optional[str]
    state: Optional[FeatureInitializationState]
