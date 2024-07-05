"""Main Module"""
import reflex as rx
# from rxconfig import config
from thoth.styles.styles import *
from thoth.labels.labels import *

def index() -> rx.Component:
    """Main Page"""

    return rx.container(
        rx.section(
            rx.flex(
                rx.box(
                    rx.heading(
                        header["title"],
                        as_="h1",
                        style=[primary_color, h1_style]
                    ),
                    rx.text(
                        header["subtitle"],
                        as_="p",
                        style=[text_style]
                    ),
                ),
                rx.box(
                    rx.color_mode.button(),
                ),
                direction="row",
                justify="between",
                spacing="2",
            ),
        ),
        rx.section(
            rx.heading(
                        introduction["title"],
                        as_="h2",
                        style=[primary_color, h2_style]
                    ),
            rx.flex(
                    rx.text(
                        introduction["naming"],
                        as_="p",
                        style=[text_style],
                    ),
                    rx.text(
                        introduction["explanationI"],
                        rx.text.em('magia'),
                        introduction["explanationII"],
                        as_="p",
                        style=[text_style],
                    ),
                    direction="column",
                justify="between",
                spacing="5"
            ),
        ),
        rx.section(
            rx.heading(branching["title"], style=[primary_color, h2_style]),
            rx.flex(
            rx.text(
                branching["contentI"],
                style=[text_style]
            ),
            rx.text(
                branching["contentII"],
                style=[text_style]
            ),
            rx.list.unordered(
                rx.foreach(branching["list"], rx.list.item)
            ),
            direction="column",
                justify="between",
                spacing="5"
            ),
        ),
        rx.section(
                rx.heading(commits["title"], style=[primary_color, h2_style]),
                rx.flex(
                rx.text(
                    commits["contentI"],
                    style=[text_style]
                ),
                rx.list.unordered(
                    rx.foreach(commits["list"], rx.list.item)
                ),
                direction="column",
                justify="between",
                spacing="5"
                ),
        ),
        spacing="5",
    )

app = rx.App()  # pylint: disable=not-callable
app.add_page(index)
