from typing import List
from lib.Enova import Enova
from mojo import context  # type: ignore

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


def main() -> None:
    context.log.info("Hello from muse-python!")

    # message: str = f"Your IP address is: {get_ip()}"
    # say: str = cowsay.get_output_string("cow", message)

    # context.log.info(f"\n{say}\n")

    tl_feedback = Timer()
    tl_feedback.start(on_tl_feedback_tick)

    enova = Enova()
    enova.switch(1, 2, 0)
    enova.switch(2, 3, 1)
    enova.switch(3, 4, 2)

    display.online(lambda _: context.log.info("Display Online"))
    display.offline(lambda _: context.log.info("Display Offline"))

    tp.online(on_tp_online)
    tp.offline(lambda _: context.log.info("Touch Panel Offline"))


def on_tp_online(event: dict) -> None:
    context.log.info("Registering Touch Panel Events")

    for source in sources:
        tp.port[source["port"]].button[source["channel"]].watch(on_source_select)

    panel_reset()


def on_source_select(event: dict) -> None:
    global selected_source, required_popup

    context.log.info(f"Source Selected: {event}")

    selected_source = event["channel"]
    required_popup = selected_source

    panel_refresh()


def panel_reset() -> None:
    tp.port[1].send_command("@PPX")
    tp.port[1].send_command("ADBEEP")

    panel_refresh()


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
        tp.port[source["port"]].button[source["channel"]] = (
            selected_source == source["channel"]
        )


if __name__ == "__main__":
    main()

context.run(globals())
