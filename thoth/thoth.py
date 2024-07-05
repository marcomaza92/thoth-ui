"""Main Module"""

import reflex as rx

# from rxconfig import config
from thoth.styles.styles import *  # pylint: disable=wildcard-import
from thoth.labels.labels import *  # pylint: disable=wildcard-import


def index() -> rx.Component:
    """Main Page"""

    return rx.container(
        rx.section(
            rx.flex(
                rx.box(
                    rx.heading(
                        header["title"], as_="h1", style=[primary_color, h1_style]
                    ),
                    rx.text(header["subtitle"], as_="p", style=[text_style]),
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
                introduction["title"], as_="h2", style=[primary_color, h2_style]
            ),
            rx.flex(
                rx.text(
                    introduction["naming"],
                    as_="p",
                    style=[text_style],
                ),
                rx.text(
                    introduction["explanation_i"],
                    rx.text.em("magia"),
                    introduction["explanation_ii"],
                    as_="p",
                    style=[text_style],
                ),
                direction="column",
                justify="between",
                spacing="5",
            ),
        ),
        rx.section(
            rx.heading(branching["title"], style=[primary_color, h2_style]),
            rx.flex(
                rx.text(branching["content_i"], style=[text_style]),
                rx.text(branching["content_ii"], style=[text_style]),
                rx.list.unordered(rx.foreach(branching["list"], rx.list.item)),
                direction="column",
                justify="between",
                spacing="5",
            ),
        ),
        rx.section(
            rx.heading(commits["title"], style=[primary_color, h2_style]),
            rx.flex(
                rx.text(commits["content_i"], style=[text_style]),
                rx.list.unordered(rx.foreach(commits["list"], rx.list.item)),
                direction="column",
                justify="between",
                spacing="5",
            ),
        ),
        rx.section(
            rx.heading(analysis["title"], style=[primary_color, h2_style]),
            rx.flex(
                rx.text(analysis["content_i"], style=[text_style]),
                rx.text(analysis["content_ii"], style=[text_style]),
                rx.image(src="/analysis_i.png"),
                direction="column",
                justify="between",
                spacing="5",
            ),
        ),
        rx.section(
            rx.heading(code_review["title"], style=[primary_color, h2_style]),
            rx.flex(
                rx.text(code_review["content_i"], style=[text_style]),
                rx.list.unordered(rx.foreach(code_review["list"], rx.list.item)),
                rx.link(
                    "Ejemplo de Merge Request",
                    href=code_review["link"],
                    target="_blank",
                ),
                direction="column",
                justify="between",
                spacing="5",
            ),
        ),
        spacing="5",
    )


app = rx.App()  # pylint: disable=not-callable
app.add_page(index)
