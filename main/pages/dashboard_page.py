from constants import URL
from core.pages import BasePage
from main.components.dashboard.my_actions import MyActions
from main.components.dashboard.time_at_work_component import TimeAtWorkComponent
from main.components.header import Header
from main.components.side_menu import SideMenu


class DashboardPage(BasePage):
    url = f"{URL}/dashboard/index"

    header = Header()
    side_menu = SideMenu()

    time_at_work = TimeAtWorkComponent()
    my_actions = MyActions()

    def is_loaded(self, timeout=5):
        return all((
            self.time_at_work.is_loaded(timeout=timeout),
            self.my_actions.is_loaded(timeout=timeout)
        ))

