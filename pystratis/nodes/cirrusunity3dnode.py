from typing import Union
from pystratis.core.networks import CirrusMain, CirrusTest, CirrusRegTest
from pystratis.api.unity3d import Unity3D
from .cirrusnode import CirrusNode


class CirrusUnity3DNode(CirrusNode):
    """A Cirrus unity node."""
    def __init__(self, ipaddr: str = 'http://localhost', blockchainnetwork: Union[CirrusMain, CirrusTest, CirrusRegTest] = CirrusMain()):
        """Initialize a cirrus node with unity3d support."""
        super().__init__(ipaddr=ipaddr, blockchainnetwork=blockchainnetwork)
        unity3d_route = f"{self.ipaddr}:{blockchainnetwork.UNITY3D_PORT}"
        # Unity3D endpoints do not appear in swagger.
        self._unity3d = Unity3D(baseuri=unity3d_route, network=blockchainnetwork)

    @property
    def unity3d(self) -> Unity3D:
        """The unity3dapi route.

        Returns:
            Unity3D: A Unity3D instance.
        """
        return self._unity3d
