from typing import Optional
from pybitcoin import Model, FeatureInitializationState


class FeaturesDataModel(Model):
    """A FeaturesDataModel."""
    namespace: Optional[str]
    state: Optional[FeatureInitializationState]
