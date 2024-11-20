from models import Library
from utils import validate_year, validate_status, format_book_info


def display_menu() -> None:
    print("\n=== Библиотечная система ===")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Поиск книги")
    print("4. Показать все книги")
    print("5. Изменить статус книги")
    print("0. Выход")


def main_menu() -> None:
    library = Library()
    while True:
        display_menu()
        choice = input("\nВыберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            while True:
                year_str = input("Введите год издания: ")
                success, year, error_message = validate_year(year_str)
                if success:
                    break
                print(error_message)

            library.add_book(title, author, year)
            print("Книга успешно добавлена!")

        elif choice == "2":
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                if library.delete_book(book_id):
                    print("Книга успешно удалена!")
                else:
                    print("Книга с таким ID не найдена!")
            except ValueError:
                print("Некорректный ID книги!")

        elif choice == "3":
            query = input("Введите поисковый запрос: ")
            found_books = library.search_books(query)
            if found_books:
                print("\nНайденные книги:")
                for book in found_books:
                    print(format_book_info(book))
            else:
                print("Книги не найдены!")

        elif choice == "4":
            if library.books:
                print("\nСписок всех книг:")
                for book in library.books.values():
                    print(format_book_info(book))
            else:
                print("Библиотека пуста!")

        elif choice == "5":
            try:
                book_id = int(input("Введите ID книги: "))
                new_status = input("Введите новый статус (в наличии/выдана): ")
                success, error_message = validate_status(new_status)
                if not success:
                    print(error_message)
                    continue
                if library.change_status(book_id, new_status):
                    print("Статус книги успешно изменен!")
                else:
                    print("Книга с таким ID не найдена!")
            except ValueError:
                print("Некорректный ID книги!")

        elif choice == "0":
            break

        else:
            print("Некорректный выбор! Попробуйте снова.")


if __name__ == "__main__":
    main_menu()
