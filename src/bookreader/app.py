"""
A cross-platform book reader
"""

import toga
from toga.style import Pack


class BookReader(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        # --- НОВЫЙ КОД: Создаем placeholder для списка книг ---
        library_content_box = toga.Box(style=toga.style.Pack(direction=toga.style.pack.COLUMN))

        # Добавляем несколько фейковых элементов книг на английском
        self._add_fake_book_item(library_content_box, "Book Cover 1", "Book Title 1")
        self._add_fake_book_item(library_content_box, "Book Cover 2", "Book Title 2")
        self._add_fake_book_item(library_content_box, "Book Cover 3", "Book Title 3")

        # Добавляем контейнер со списком книг в главный контейнер окна
        main_box.add(library_content_box)

        self.main_window = toga.MainWindow(title="Book Reader")
        self.main_window.content = main_box
        self.main_window.show()

        # --- НОВЫЙ МЕТОД ДЛЯ СОЗДАНИЯ ОДНОГО ЭЛЕМЕНТА КНИГИ (текст на английском) ---
    def _add_fake_book_item(self, parent_box, cover_text, title_text):
        """
        Creates and adds a fake book item (cover + title) to the parent box.
        """
        # Контейнер для одной книги, горизонтальное расположение, с отступами
        book_item_box = toga.Box(style=toga.style.Pack(direction=toga.style.pack.ROW, padding=5))

        # Фейковая обложка - пока просто текст, потом заменим на картинку
        cover_placeholder = toga.Label(cover_text, style=toga.style.Pack(width=100, height=150))

        # Название книги
        title_label = toga.Label(title_text, style=toga.style.Pack(padding_left=10))

        # Добавляем элементы в контейнер книги
        book_item_box.add(cover_placeholder)
        book_item_box.add(title_label)

        # Добавляем контейнер книги в родительский контейнер
        parent_box.add(book_item_box)

def main():
    return BookReader()
