from typing import Optional
from pybitcoin import Model


class FeaturesDataModel(Model):
    """A FeaturesDataModel."""
    namespace: Optional[str]
    state: Optional[str]
