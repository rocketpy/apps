# Build web apps in minutes. Deploy with a single command.

# Component: https://pynecone.io/docs/library

# pip install pynecone-io

# mkdir my_app_name
# cd my_app_name
# pc init

#  Example

import pynecone as pc


class State(pc.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def index():
    return pc.hstack(
        pc.button(
            "Decrement",
            color_scheme="red",
            border_radius="1em",
            on_click=State.decrement,
        ),
        pc.heading(State.count, font_size="2em"),
        pc.button(
            "Increment",
            color_scheme="green",
            border_radius="1em",
            on_click=State.increment,
        ),
    )
app = pc.App(state=State)
app.add_page(index)
app.compile()

