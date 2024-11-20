from datetime import datetime
from typing import Tuple


def validate_year(year_str: str) -> Tuple[bool, int, str]:
    """
    Проверка корректности введенного года.

    Returns:
        Tuple[bool, int, str]: (успех, год, сообщение об ошибке)
    """
    try:
        year = int(year_str)
        if 0 <= year <= datetime.now().year:
            return True, year, ""
        return False, 0, "Год должен быть между 0 и текущим годом"
    except ValueError:
        return False, 0, "Пожалуйста, введите корректный год"


def validate_status(status: str) -> Tuple[bool, str]:
    """
    Проверка корректности статуса книги.

    Returns:
        Tuple[bool, str]: (успех, сообщение об ошибке)
    """
    if status in ["в наличии", "выдана"]:
        return True, ""
    return False, "Некорректный статус! Используйте 'в наличии' или 'выдана'"


def format_book_info(book) -> str:
    """Форматирование информации о книге для вывода."""
    return (f"ID: {book.book_id}, '{book.title}' автор: {book.author}, "
            f"год: {book.year}, статус: {book.status}")
