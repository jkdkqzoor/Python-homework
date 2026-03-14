"""
Задание 1. Файловый менеджер (модуль os)

Напишите утилиты для работы с файловой системой:

import os

def find_files(directory: str, extension: str) -> list:
    ""
    Рекурсивно находит все файлы с указанным расширением.

    Args:
        directory: путь к директории
        extension: расширение файла (например, ".py")

    Returns:
        Список полных путей к найденным файлам
    ""
    pass

def get_directory_size(directory: str) -> int:
    ""Возвращает общий размер директории в байтах.""
    pass

def find_duplicates(directory: str) -> dict:
    ""
    Находит файлы с одинаковыми именами в разных поддиректориях.

    Returns:
        Словарь {имя_файла: [список путей]}
    ""
    pass
"""

import os


def find_files(directory: str, extension: str) -> list:
    """
    Рекурсивно находит все файлы с указанным расширением.

    Args:
        directory: путь к директории
        extension: расширение файла (например, ".py")

    Returns:
        Список полных путей к найденным файлам
    """
    result: list[str] = []
    contents = os.listdir(directory)
    for file in contents:
        if file.endswith(extension):
            result.append(file)
    if not result:
        raise FileNotFoundError
    return result


def get_directory_size(directory: str) -> int:
    """Возвращает общий размер директории в байтах."""
    return os.path.getsize(directory)


def find_duplicates(directory: str) -> dict:
    """
    Находит файлы с одинаковыми именами в разных поддиректориях.

    Returns:
        Словарь {имя_файла: [список путей]}
    """
    files = {}
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
                files.setdefault(filename, []).append(os.path.join(dirpath, filename))
    return {name: paths for name, paths in files.items() if len(paths) > 1}


# Пример использования:
py_files = find_files(".", ".py")
print(f"Найдено {len(py_files)} Python-файлов")

size = get_directory_size(".")
print(f"Размер: {size / 1024 / 1024:.2f} MB")
