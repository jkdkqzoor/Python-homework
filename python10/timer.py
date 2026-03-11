"""
Задание 3. Контекстный менеджер Timer

Создайте контекстный менеджер Timer, который измеряет время выполнения блока кода:

import time

class Timer:
    def __init__(self, name: str = "Block"):
        self.name = name
        self.elapsed = None

    def __enter__(self):
        # Запомнить время начала
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Вычислить и вывести время
        pass

# Пример использования:
with Timer("Sorting"):
    data = [i for i in range(1000000)]
    sorted(data, reverse=True)
# Sorting: 0.1234 seconds

with Timer("Sleeping"):
    time.sleep(0.5)
# Sleeping: 0.5012 seconds

"""

import time

class Timer:
    def __init__(self, name:str = "Block"):
        self.name = name
        self.elapsed = None

    def __enter__(self):    
        self.elapsed = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.name}: {round(time.time()-self.elapsed, 4)}")

# Пример использования:
with Timer("Sorting"):
    data = [i for i in range(1000000)]
    sorted(data, reverse=True)
# Sorting: 0.1234 seconds

with Timer("Sleeping"):
    time.sleep(0.5)
# Sleeping: 0.5012 seconds