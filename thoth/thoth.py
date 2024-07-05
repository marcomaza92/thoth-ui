"""Main Module"""

import reflex as rx

# from rxconfig import config
from thoth.styles.styles import *  # pylint: disable=wildcard-import
from thoth.labels.labels import *  # pylint: disable=wildcard-import


def index() -> rx.Component:
    """Main Page"""

    return rx.el.main(
        rx.el.header(
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
                rx.text(
                    introduction["usage_i"],
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
                rx.text(branching["content_iii"], style=[text_style]),
                rx.list.unordered(rx.foreach(branching["list_i"], rx.list.item)),
                direction="column",
                justify="between",
                spacing="5",
            ),
        ),
        rx.section(
            rx.heading(commits["title"], style=[primary_color, h2_style]),
            rx.flex(
                rx.text(commits["content_i"], style=[text_style]),
                rx.text(commits["content_ii"], style=[text_style]),
                rx.text(commits["content_iii"], style=[text_style]),
                rx.list.unordered(
                    rx.foreach(
                        commits["list_i"], lambda item: rx.list.item(rx.code(item))
                    )
                ),
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
                rx.image(src=analysis["image_i"]),
                direction="column",
                justify="between",
                spacing="5",
            ),
        ),
        rx.section(
            rx.heading(code_review["title"], style=[primary_color, h2_style]),
            rx.flex(
                rx.text(code_review["content_i"], style=[text_style]),
                rx.list.unordered(rx.foreach(code_review["list_i"], rx.list.item)),
                rx.link(
                    code_review["link_i"]["text"],
                    href=code_review["link_i"]["url"],
                    target="_blank",
                ),
                direction="column",
                justify="between",
                spacing="5",
            ),
        ),
        rx.section(
            rx.heading(ci_cd["title"], style=[primary_color, h2_style]),
            rx.flex(
                rx.text(ci_cd["content_i"], style=[text_style]),
                rx.list.unordered(rx.foreach(ci_cd["list_i"], rx.list.item)),
                rx.text(ci_cd["content_ii"], style=[text_style]),
                rx.image(src=ci_cd["image_i"]),
                rx.text(ci_cd["content_iii"], style=[text_style]),
                rx.list.unordered(rx.foreach(ci_cd["list_ii"], rx.list.item)),
                rx.image(src=ci_cd["image_ii"]),
                direction="column",
                justify="between",
                spacing="5",
            ),
        ),
        rx.el.footer(
            rx.heading(next_steps["title"], style=[primary_color, h2_style]),
            rx.flex(
                rx.text(next_steps["content_i"], style=[text_style]),
                rx.link(
                    next_steps["link_i"]["text"],
                    href=next_steps["link_i"]["url"],
                    target="_blank",
                ),
                direction="column",
                justify="between",
                spacing="5",
            ),
        ),
        spacing="5",
        style=[main_style],
    )


app = rx.App()  # pylint: disable=not-callable
app.add_page(index)
