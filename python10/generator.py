"""
Задание 4. Генераторы

4.1. Генератор Fibonacci

Напишите генератор fibonacci(n), который выдаёт первые n чисел Фибоначчи:

def fibonacci(n: int):
    # Ваш код с yield
    pass

print(list(fibonacci(10)))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

4.2. Бесконечный генератор

Напишите генератор infinite_sequence(start=0), который бесконечно генерирует числа:

def infinite_sequence(start: int = 0):
    # Ваш код
    pass

gen = infinite_sequence(10)
print(next(gen))  # 10
print(next(gen))  # 11
print(next(gen))  # 12

4.3. Генератор для чтения файла по частям

Напишите генератор read_in_chunks(filename, chunk_size=1024), который читает файл порциями:

def read_in_chunks(filename: str, chunk_size: int = 1024):
    # Ваш код
    pass

for chunk in read_in_chunks("large_file.txt", 100):
    print(len(chunk))  # Выведет размеры порций
"""

def fibonacci(n: int):
    """Генератор Fibonacci"""
    count = 0
    a, b = 0, 1
    while count < n:
        yield a
        a, b = b, a + b
        count += 1
    
print(list(fibonacci(10)))


def infinite_sequence(start:int = 0):
    """Бесконечный генератор"""
    while True:
        yield start
        start += 1

gen = infinite_sequence(10)

print(next(gen))
print(next(gen))
print(next(gen))


def read_in_chunks(filename:str, chunk_size:int = 1024):
    """Генератор для чтения файла по частям"""
    with open(filename, "r") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

for chunk in read_in_chunks("students.py", 100):
    print(len(chunk))