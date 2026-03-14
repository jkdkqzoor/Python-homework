"""
Задание 3. Комбинаторика (модуль itertools)

Решите задачи с использованием itertools:

import itertools

def all_combinations(items: list, min_size: int = 1, max_size: int = None) -> list:
    ""Возвращает все комбинации элементов от min_size до max_size.""
    pass

def unique_permutations(items: list) -> list:
    ""Возвращает уникальные перестановки (для списков с повторами).""
    pass

def cartesian_product(*iterables) -> list:
    ""Возвращает декартово произведение.""
    pass

# Пример использования:
print(all_combinations([1, 2, 3], 2, 2))
# [(1, 2), (1, 3), (2, 3)]

print(unique_permutations([1, 1, 2]))
# [(1, 1, 2), (1, 2, 1), (2, 1, 1)]

print(cartesian_product([1, 2], ['a', 'b']))
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

Практическое применение: Напишите функцию, которая генерирует все возможные комбинации пиццы из списка топпингов (от 1 до 4 топпингов):

toppings = ["pepperoni", "mushrooms", "olives", "onions", "peppers"]
pizzas = all_pizza_combinations(toppings, max_toppings=4)
print(f"Всего вариантов пиццы: {len(pizzas)}")
"""

import itertools


def all_combinations(items: list, min_size: int = 1, max_size: int = None) -> list:
    """Возвращает все комбинации элементов от min_size до max_size."""
    result = []
    for i in range(min_size, max_size + 1, 1):
        combine = itertools.combinations(items, i)
        result.extend(combine)
    return result


def unique_permutations(items: list) -> list:
    """Возвращает уникальные перестановки (для списков с повторами)."""
    return list(set(itertools.permutations(items)))


def cartesian_product(*iterables) -> list:
    """Возвращает декартово произведение."""
    return list(itertools.product(*iterables))


# Пример использования:
print(all_combinations([1, 2, 3], 2, 2))
# [(1, 2), (1, 3), (2, 3)]

print(unique_permutations([1, 1, 2]))
# [(1, 1, 2), (1, 2, 1), (2, 1, 1)]

print(cartesian_product([1, 2], ['a', 'b']))
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

#Практическое применение: Напишите функцию, которая генерирует все возможные комбинации пиццы из списка топпингов (от 1 до 4 топпингов):


def all_pizza_combinations(topps: list[str], min_toppings: int = 1, max_toppings: int = 4) -> list:
    result = []
    for i in range(min_toppings, max_toppings + 1, 1):
        combine = itertools.combinations(topps, i)
        result.extend(combine)
    return result

toppings = ["pepperoni", "mushrooms", "olives", "onions", "peppers"]
pizzas = all_pizza_combinations(toppings, max_toppings=4)
print(f"Всего вариантов пиццы: {len(pizzas)}")