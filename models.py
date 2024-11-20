from dataclasses import dataclass
from typing import Dict, List
import json


@dataclass
class Book:
    book_id: int
    title: str
    author: str
    year: int
    status: str = "в наличии"


class Library:
    def __init__(self, file_path: str = "library.json"):
        self.file_path = file_path
        self.books: Dict[int, Book] = {}
        self.load_books()

    def load_books(self) -> None:
        """Загрузка книг из JSON файла."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                books_data = json.load(file)
                self.books = {
                    int(id_): Book(**data)
                    for id_, data in books_data.items()
                }
        except FileNotFoundError:
            self.books = {}

    def save_books(self) -> None:
        """Сохранение книг в JSON файл."""
        books_data = {
            str(book_id): {
                'id': book.book_id,
                'title': book.title,
                'author': book.author,
                'year': book.year,
                'status': book.status
            }
            for book_id, book in self.books.items()
        }
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(books_data, file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int) -> Book:
        """Добавление новой книги."""
        new_id = max(self.books.keys(), default=0) + 1
        book = Book(book_id=new_id, title=title, author=author, year=year)
        self.books[new_id] = book
        self.save_books()
        return book

    def delete_book(self, book_id: int) -> bool:
        """Удаление книги по ID."""
        if book_id in self.books:
            del self.books[book_id]
            self.save_books()
            return True
        return False

    def search_books(self, query: str) -> List[Book]:
        """Поиск книг по названию, автору или году."""
        query = query.lower()
        return [
            book for book in self.books.values()
            if query in book.title.lower() or query in book.author.lower() or query in str(book.year)
        ]

    def change_status(self, book_id: int, new_status: str) -> bool:
        """Изменение статуса книги."""
        if book_id in self.books:
            self.books[book_id].status = new_status
            self.save_books()
            return True
        return False
