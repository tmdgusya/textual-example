from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Button, Static
from textual.reactive import reactive
from time import monotonic

class TimeDisplay(Static):
    """A widget to display elapsed time."""

    start_time = reactive(monotonic)
    time = reactive(0.0)

    def _on_mount(self) -> None:
        self.set_interval(1 / 60, self.update_time)

    def update_time(self) -> None:
        """Update the time."""
        self.time = monotonic() - self.start_time
    
    def watch_time(self, time: float) -> None:
        """Watch the time."""
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        self.update(f"{hours:02,.0f}:{minutes:02,.0f}:{seconds:05.2f}")

class Stopwatch(Static):
    """A stopwatch widget."""

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start":
            self.add_class("started")
        elif event.button.id == "stop":
            self.remove_class("started")

    def compose(self) -> ComposeResult:
        """Create child widgets for the stopwatch."""
        yield Button("Start", id = "start", variant = "success")
        yield Button("Stop", id = "stop", variant = "error")
        yield Button("Reset", id = "reset")
        yield TimeDisplay("00:00:00.000")

# @see https://textual.textualize.io/tutorial/
class StopwatchApp(App):
    """A Textual app to manage stopwatched"""

    CSS_PATH = "stopwatch03.css"
    # a list of tuples of (key, action, description)
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"), ("i", "install", "Install the app")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Container(Stopwatch(), Stopwatch(), Stopwatch())

    def action_toggle_dark(self) -> None:
        """An Action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()
