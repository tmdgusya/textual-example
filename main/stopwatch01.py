from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

# @see https://textual.textualize.io/tutorial/
class StopwatchApp(App):
    """A Textual app to manage stopwatched"""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An Action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()
