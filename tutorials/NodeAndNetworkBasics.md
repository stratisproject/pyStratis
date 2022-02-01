pyStratis Node & Network Basics
===============================

pyStratis provides a python interface to a running Strax or Cirrus node's API. 
Therefore, to use pystratis, you will need a running node daemon. 

The information in this tutorial describes some basic steps to set up a Strax/Cirrus node for use with pystratis. 
For more information on the StratisFullNode architecture, please refer to the [Stratis Academy](https://academy.stratisplatform.com/) base documentation or the [Academy's developer API reference](https://academy.stratisplatform.com/Developer%20Resources/API%20Reference/api.html#stratis-core-api-reference). 

Finally, a quick reference on the pystratis package can be found at [pystratis.readthedocs.io](https://pystratis.readthedocs.io/en/latest/)

## Node setup
### Strax
#### Strax Wallet
The most up-to-date version of the Strax Wallet can be found at [https://github.com/stratisproject/StraxUI/releases/](https://github.com/stratisproject/StraxUI/releases/).
- Installation files are available for Windows, MacOS, and Linux platforms. 
- When running, the wallet provides a user-interface to the Strax node running as a background daemon.

#### Headless (no GUI)
Clone the repository from GitHub, checkout the latest release, and enter the directory.
```commandline
git clone https://github.com/stratisproject/StratisFullNode.git
git checkout -b release/1.1.1.0
cd StratisFullNode\src\Stratis.StraxD
```
The node daemon can be started with `dotnet run`.

- Configuration settings can be updated in the stratis.conf file in the data directory or through command line args. 
- Important (optional) args:
  - `-txindex=1` For retrieving individual transaction details. Needed for some API calls.
  - `-addressindex=1` For retrieving balance details for individual addresses. Needed for some API calls.
  - `-apiuri=0.0.0.0` If node is being run on a remote device on your network (i.e. headless RPi) to access API outside of ssh tunnel.
  - `-datadir=<custom datadir path>` Change your node's data directory.
  - `-testnet` Connect the node to the testnet blockchain.
  - `-regtest` Regression testing network.
  - `-port=12344` Change the default connection port.  
  - `-apiport=12345` Change the api port.
  - `-rpcport=12346` Change the rpc port (if active, inactive by default).
  - `-signalrport=12347` Change the signalrport.  
  - Other arguments can be discovered in the stratis.conf file or by running the `dotnet run help` command.


### Cirrus
#### Cirrus Wallet
The most up-to-date version of the Cirrus Wallet can be found at [https://github.com/stratisproject/CirrusCore/releases/](https://github.com/stratisproject/CirrusCore/releases/).
- Installation files are available for Windows, MacOs, and Linux platforms. 
- When running, the wallet provides a user-interface to the Cirrus node running as a background daemon.

#### Headless (no GUI)
Clone the repository from GitHub, checkout the latest release, and enter the directory.
```commandline
git clone https://github.com/stratisproject/StratisFullNode.git
git checkout -b release/1.1.1.0
cd StratisFullNode\src\Stratis.CirrusD
```
The node daemon can be started with `dotnet run`. 
- See above for information on useful command line args.

### Interflux
Masternode setup is more complex. Please see official documentation for information on [registering](https://www.stratisplatform.com/wp-content/uploads/2020/11/STRAX-Sidechain-Masternode-Joining-the-Federation-v2.pdf) and [running](https://www.stratisplatform.com/wp-content/uploads/2020/11/STRAX-Sidechain-Masternodes-User-Setup-Guide.pdf) a masternode.

## pystratis.nodes
The [pystratis.nodes](https://pystratis.readthedocs.io/en/latest/source/pystratis.nodes.html) namespace defines the primary node types used on the Stratis/Cirrus blockchains.

Each node instance can take two arguments at initialization:
- ipaddr: The node's ip address. Update if connecting to a node remotely.
  - Defaults to `http://localhost`.
- [blockchainnetwork](https://pystratis.readthedocs.io/en/latest/source/pystratis.core.networks.html): The type of network the node is running.
  - Defaults to `StraxMain()` for strax nodes.
  - Defaults to `CirrusMain()` for cirrus nodes.
```python
# Example of connecting to a node at 192.168.3.1 running on Strax Testnet.
from pystratis.nodes import StraxNode
from pystratis.core.networks import StraxTest
node = StraxNode(ipaddr='192.168.3.1', blockchainnetwork=StraxTest())
```
- Please see [the respective network class definition](https://pystratis.readthedocs.io/en/latest/source/pystratis.core.networks.html) for overriding network defaults if your node uses non-standard port numbers.

### Standard nodes
- [StraxNode](https://pystratis.readthedocs.io/en/latest/source/pystratis.nodes.html#straxnode) - The primary node type for the Strax network.
```python
from pystratis.nodes import StraxNode
node = StraxNode()
```
  
- [CirrusNode](https://pystratis.readthedocs.io/en/latest/source/pystratis.nodes.html#cirrusnode) - The primary node type for the Cirrus sidechain.
```python
from pystratis.nodes import CirrusNode
node = CirrusNode()
```

### Interflux Gateway (Multisig Masternodes)
- [InterfluxStraxNode](https://pystratis.readthedocs.io/en/latest/source/pystratis.nodes.html#interfluxstraxnode) - The Strax member of the multisig Interflux Gateway pair. 
- [InterfluxCirrusNode](https://pystratis.readthedocs.io/en/latest/source/pystratis.nodes.html#interfluxcirrusnode) - The Cirrus member of the multisig Interflux Gateway pair.
```python
from pystratis.nodes import InterfluxStraxNode, InterfluxCirrusNode
strax_node = InterfluxStraxNode()
cirrus_node = InterfluxCirrusNode()
```

### Standard Masternodes
- [StraxMasterNode](https://pystratis.readthedocs.io/en/latest/source/pystratis.nodes.html#straxmasternode) - The Strax member of the standard masternode pair.
- [CirrusMasterNode](https://pystratis.readthedocs.io/en/latest/source/pystratis.nodes.html#cirrusmasternode) - The Cirrus member of the standard masternode pair.
```python
from pystratis.nodes import StraxMasterNode, CirrusMasterNode
strax_node = StraxMasterNode()
cirrus_node = CirrusMasterNode()
```

## Node API endpoints
At this point, you should have: 
- A running node daemon.
- An initialized pystratis.node instance.

Active API routes are implemented as class properties. 

API endpoints can be called as in the following example:

```python
# API endpoint: http://localhost:17103/api/node/status
from pystratis.nodes import StraxNode
strax_node = StraxNode()
strax_node.node.status()
```
Please see the [pystratis.api namespace](https://pystratis.readthedocs.io/en/latest/source/pystratis.api.html#subpackages) documentation (or other tutorials) for more information on calling specific API endpoints. 
