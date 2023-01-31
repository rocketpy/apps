# Web apps in pure Python - Build web apps in minutes. Deploy with a single command.


# Component: https://pynecone.io/docs/library

# pip install pynecone-io

# mkdir my_app_name
# cd my_app_name
# pc init


# Example Pynecone App
import pynecone as pc
import openai

openai.api_key = "YOUR_API_KEY"

class State(pc.State):
    """The app state."""
    prompt = ""
    image_url = ""
    image_processing = False
    image_made = False

    def process_image(self):
        """Set the image processing flag to true and indicate image is not made yet."""
        self.image_processing = True
        self.image_made = False        

    def get_image(self):
        """Get the image from the prompt."""
        response = openai.Image.create(prompt=self.prompt, n=1, size="1024x1024")
        self.image_url = response["data"][0]["url"]
        self.image_processing = False
        self.image_made = True

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

