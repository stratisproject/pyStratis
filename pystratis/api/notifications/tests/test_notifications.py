import pytest
from pytest_mock import MockerFixture
from pystratis.api.notifications import Notifications
from pystratis.core.networks import StraxMain, CirrusMain


@pytest.mark.parametrize('network', [StraxMain(), CirrusMain()], ids=['StraxMain', 'CirrusMain'])
def test_sync(mocker: MockerFixture, network, generate_uint256):
    data = None
    mocker.patch.object(Notifications, 'get', return_value=data)
    notifications = Notifications(network=network, baseuri=mocker.MagicMock())

    notifications.sync(sync_from=generate_uint256)

    # noinspection PyUnresolvedReferences
    notifications.get.assert_called_once()
