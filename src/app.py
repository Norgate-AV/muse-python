from typing import List
from lib.Enova import Enova
from mojo import context  # type: ignore
from lib.UserInterface import UserInterface

# from typing import TYPE_CHECKING
# import cowsay  # type: ignore
from Timer import Timer

# from utils import get_ip
# from types.timeline import TimelineEvent

tp = context.devices.get("AMX-10001")
exbcomm2 = context.devices.get("AMX-6001")
exbmp1 = context.devices.get("AMX-7001")

display = exbcomm2.port[1]


PAGE_LOGO: int = 0
PAGE_MAIN: int = 1

pages: List[str] = ["Logo", "Main"]

required_page: int = 0
required_popup: int = 0

selected_source: int = 0

sources: List[dict] = [
    {
        "name": "PC",
        "label": "Main PC",
        "port": 1,
        "channel": 33,
        "address": 33,
        "popup": "Local PC",
    },
    {
        "name": "Laptops",
        "label": "Laptops",
        "port": 1,
        "channel": 31,
        "address": 31,
        "popup": "Laptops",
    },
    {
        "name": "Visualiser",
        "label": "Visualiser",
        "port": 1,
        "channel": 32,
        "address": 32,
        "popup": "Visualiser",
    },
    {
        "name": "BYOD",
        "label": "BYOD",
        "port": 1,
        "channel": 34,
        "address": 34,
        "popup": "BYOD",
    },
]


def ui_online_status_change_event(event) -> None:
    print_event(event)

    # inspect the event object
    for prop in dir(event):
        # if not prop.startswith("__"):
        context.log.info(f"{prop}: {getattr(event, prop)}")
    # context.log.info("Registering Touch Panel Events")

    for source in sources:
        context.log.info(f"Registering Source: {source['name']}")
        tp.port[source["port"]].button[source["channel"]].watch(on_source_select)

    tp.port[1].button[1].watch(on_touch_to_start)

    # panel_reset()


def main() -> None:
    context.log.info("Hello from muse-python!")

    # message: str = f"Your IP address is: {get_ip()}"
    # say: str = cowsay.get_output_string("cow", message)

    # context.log.info(f"\n{say}\n")

    # tl_feedback = Timer()
    # tl_feedback.start(on_tl_feedback_tick)

    # enova = Enova()
    # enova.switch(1, 2, 0)
    # enova.switch(2, 3, 1)
    # enova.switch(3, 4, 2)

    # display.online(lambda _: context.log.info("Display Online"))
    # display.offline(lambda _: context.log.info("Display Offline"))

    # tp.online(on_tp_online)
    # tp.offline(lambda _: context.log.info("Touch Panel Offline"))


def on_touch_to_start(event) -> None:
    if not event.value:
        return

    print_event(event)

    global required_page

    context.log.info("Touch to Start")

    required_page = PAGE_MAIN

    panel_refresh()


def on_source_select(event) -> None:
    if not event.value:
        return

    print_event(event)

    global selected_source, required_popup

    context.log.info(f"Source Selected: {event.id}")

    selected_source = event.id
    required_popup = selected_source

    ui.show_popup(sources[selected_source]["popup"])


def panel_refresh() -> None:
    global required_page, required_popup

    tp.port[1].send_command("@PPF-Dialogs")
    tp.port[1].send_command(f"PAGE-{pages[required_page]}")

    if required_page == PAGE_MAIN:
        tp.port[1].send_command(
            f"@PPN-Sources - {sources[required_popup]['popup']};{pages[required_page]}"
        )
    elif required_page == PAGE_LOGO:
        tp.port[1].send_command("@PPN-Sources - Off;Main")


def on_tl_feedback_tick(_) -> None:
    for source in sources:
        tp.port[source["port"]].channel[source["channel"]] = (
            selected_source == source["channel"]
        )


def print_event(event) -> None:
    context.log.info(f"Event ID: {event.id}")
    context.log.info(f"Event Path: {event.path if hasattr(event, 'path') else ''}")
    context.log.info(f"Event Source: {event.source}")
    context.log.info(f"Event Value: {event.value if hasattr(event, 'value') else ''}")
    context.log.info(
        f"Event Args: {event.arguments if hasattr(event, 'arguments') else ''}"
    )
    context.log.info(
        f"Event Old Value: {event.oldValue if hasattr(event, 'oldValue') else ''}"
    )


ui = UserInterface(tp)
ui.online_status_change.append(ui_online_status_change_event)
ui.register()

if __name__ == "__main__":
    main()

context.run(globals())
