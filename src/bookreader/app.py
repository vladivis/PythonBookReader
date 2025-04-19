"""
A cross-platform book reader
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class BookReader(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        library_title_label = toga.Label("Your Library")
        main_box.add(library_title_label)

        self.main_window = toga.MainWindow(title="Book Reader")
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return BookReader()
