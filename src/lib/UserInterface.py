from mojo import context  # type: ignore
from typing import List, Callable


class UserInterface:
    __device = None
    __page: str = ""
    __popup: str = ""

    online_status_change: List[Callable] = []

    def __init__(self, device):
        self.__device = device
        self.__page = ""
        self.__popup = ""
        self.online_status_change = []

    def register(self):
        self.__register_event_handlers()

    def show_page(self, page):
        self.__page = page
        self.__refresh()

    def show_popup(self, popup):
        self.__popup = popup
        self.__refresh()

    def __refresh(self):
        self.__device.send_command("@PPF-Dialogs")
        self.__device.send_command(f"PAGE-{self.__page}")
        self.__device.send_command(f"@PPN-{self.__popup}")

    def __register_event_handlers(self):
        self.__device.online(self.__on_online)
        self.__device.offline(self.__on_offline)

    def __on_online(self, event):
        context.log.info("Touch Panel: Online")
        self.__on_online_status_change(event)

        self.__reset()
        self.__refresh()

    def __on_offline(self, event):
        context.log.info("Touch Panel: Offline")
        self.__on_online_status_change(event)

    def __reset(self):
        self.__device.send_command("@PPX")
        self.__device.send_command("ADBEEP")

    def is_online(self):
        return self.__device.isOnline()

    def is_offline(self):
        return self.__device.isOffline()

    def __on_online_status_change(self, event):
        for handler in self.online_status_change:
            handler(event)
