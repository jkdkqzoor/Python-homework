"""
Задание 2. Класс Vector (перегрузка операторов)

Создайте класс Vector для работы с математическими векторами:

class Vector:
    def __init__(self, *components):
        self.components = components

    def __add__(self, other): ...      # v1 + v2
    def __sub__(self, other): ...      # v1 - v2
    def __mul__(self, scalar): ...     # v * 3 (умножение на скаляр)
    def __rmul__(self, scalar): ...    # 3 * v
    def __eq__(self, other): ...       # v1 == v2
    def __abs__(self): ...             # abs(v) — длина вектора
    def __len__(self): ...             # len(v) — размерность
    def __getitem__(self, index): ...  # v[0]
    def __repr__(self): ...            # Vector(1, 2, 3)
    def __str__(self): ...             # "(1, 2, 3)"

# Пример использования:
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)      # (5, 7, 9)
print(v1 - v2)      # (-3, -3, -3)
print(v1 * 2)       # (2, 4, 6)
print(3 * v1)       # (3, 6, 9)
print(abs(v1))      # 3.7416... (sqrt(1+4+9))
print(v1 == Vector(1, 2, 3))  # True
print(len(v1))      # 3
print(v1[0])        # 1
"""

from math import sqrt

class Vector:
    def __init__(self, *components):
        self.components = components
    
    def __iter__(self):
        yield from self.components

    def __next__(self):
        for x in self.components:
            yield x

    def __add__(self, other):
        return tuple(x + y for x, y in zip(self, other))
    
    def __sub__(self, other):
        return tuple(x - y for x, y in zip(self, other))

    def __mul__(self, scalar):
        return tuple(x * scalar for x in self)

    def __rmul__(self, scalar):
        return tuple(x*scalar for x in self)
    
    def __eq__(self, other):
        return all(x == y for x, y in zip(self, other))

    def __abs__(self):
        return sqrt(sum((x**2 for x in self)))

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]

    def __repr__(self):
        return f"Vector{self.components}"

    def __str__(self):
        return f"{self.components}"

# Пример использования:
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)      # (5, 7, 9)
print(v1 - v2)      # (-3, -3, -3)
print(v1 * 2)       # (2, 4, 6)
print(3 * v1)       # (3, 6, 9)
print(abs(v1))      # 3.7416... (sqrt(1+4+9))
print(v1 == Vector(1, 2, 3))  # True
print(len(v1))      # 3
print(v1[0])        # 1