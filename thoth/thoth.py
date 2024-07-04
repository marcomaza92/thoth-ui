"""Main Module"""

import reflex as rx

# from rxconfig import config


def index() -> rx.Component:
    """Main Page"""
    return rx.container(
        rx.container(
            rx.color_mode.button(position="top-right"),
            rx.vstack(
                rx.heading("Thoth - Group 5", size="9"),
                rx.text(
                    "Thoth - Group 5",
                    size="5",
                ),
                rx.link(
                    rx.button("Some Magic!"),
                    href="https://reflex.dev/docs/getting-started/introduction/",
                    is_external=True,
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
            ),
        ),
        rx.container(
            rx.heading("Branching", size="9"),
            rx.text(
                    "Tomamos la decisión de hacer un Branching con dos ramas: una de desarrollo (Develop) y otra de producción (Main) debido a que planteamos el caso en el que fuéramos desarrolladores de un equipo para una empresa chica. Entonces, nos pareció la mejor idea usar dos entornos de trabajo para reducir costos y porque veíamos que era innecesario que fuera más complejo. Decidimos combinar GitFlow y GitLab Flow por las siguientes razones: poder separar en ramas de Desarrollo y Produccion, y ademas nos da la opcion de poder utilizar otras ramas como Feature para el desarrollo de nuevas caracteristicas,Realese y Hotfix para correciones rapidas y controlar las versiones del codigo, ya que el uso de ramas dedicadas nos da un historial mas organizado.",
            ),
            rx.text(
                    "Y para realizar los commits de las Branches decidimos utilizar Conventional Commits para mejorar la automatizacion y claridad debido a que utiliza distintios tipos como:",
            ),
            rx.list.unordered(
                rx.list.item("Feat= agrega funcionalidades parciales o completas"),
                rx.list.item("Fix= arregla errores que impiden el correcto funcionamiento de una feature"),
                rx.list.item("Docs= modifica archivos de documentación o archivos de código que requieran documentación"),
                rx.list.item("Test"),
                rx.list.item("etc"),
            ),
            spacing="5",
            justify="center",
            min_height="50vh",
        ),
            rx.color_mode.button(position="top-right"),
            rx.vstack(
                rx.heading("Commit", size="9"),
                rx.text(
                    "Conventional Commit",
                    size="5",
                ),
                rx.list.unordered(
                    rx.list.item("scope: message"),
                    rx.list.item("Example 2"),
                    rx.list.item("Example 3"),
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
            ),
        )



app = rx.App()  # pylint: disable=not-callable
app.add_page(index)
