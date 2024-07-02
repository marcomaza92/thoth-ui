"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
  """The app state."""

  ...


def index() -> rx.Component:
  # Welcome Page (Index)
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
      rx.color_mode.button(position="top-right"),
      rx.vstack(
        rx.heading("Commit", size="9"),
        rx.text(
          "Conventional Commit",
          size="5",
        ),
        rx.list.unordered(
          rx.list.item("scope: message"),
          rx.list.item("feat: add new container for the Branching information"),
          rx.list.item("fix: update app setup in README.md"),
          rx.list.item("chore: remove unused packages")
        ),
        spacing="5",
        justify="center",
        min_height="85vh",
      ),
    )
  )
  

app = rx.App()
app.add_page(index)
