"""
Задание 5. ⭐ Свой класс Range

Создайте класс MyRange, который работает как встроенный range, но реализован вами:

class Ms1 = Student("Ivan",20, [4, 5 ,5])
# s2 = Student("Mary",19,[5,5,5])
# s3 = Student("Petr",21, [3,4,4])yRange:
    def __init__(self, *args):
        # Поддержка MyRange(stop), MyRange(start, stop), MyRange(start, stop, step)
        pass

    def __iter__(self): ...
    def __len__(self): ...
    def __getitem__(self, index): ...  # Поддержка индексации и срезов
    def __contains__(self, value): ...
    def __repr__(self): ...
    def __eq__(self, other): ...
    def __reversed__(self): ...

# Пример использования:
r = MyRange(1, 10, 2)

# Итерация
for i in r:
    print(i, end=" ")  # 1 3 5 7 9

# Длина
print(len(r))  # 5

# Индексация
print(r[0])   # 1
print(r[-1])  # 9
print(r[1:3]) # MyRange(3, 7, 2) или [3, 5]

# Проверка вхождения
print(5 in r)  # True
print(6 in r)  # False

# Сравнение
print(r == MyRange(1, 10, 2))  # True

# Обратный порядок
print(list(reversed(r)))  # [9, 7, 5, 3, 1]

Подсказка: изучите, как работает range — он не хранит все числа в памяти, а вычисляет их по формуле.

"""

class MyRange:
    def __init__(self, *args):
        if len(args) == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif len(args) == 2:
            self.start, self.stop = args
            self.step = 1
        elif len(args) == 3:
            self.start, self.stop, self.step = args
        else:
            raise TypeError("Expected 1-3 args")
        if self.step == 0:
            raise ValueError("Step error")

    def __iter__(self):
        current = self.start
        if self.step > 0:
            while current < self.stop:
                yield current
                current += self.step 
        else:
            while current > self.stop:
                yield current
                current += self.step   

    def __len__(self):
        start, stop, step = self.start, self.stop, self.step
        if step > 0:
            if start >= stop:
                return 0
            return (stop - start - 1) // step + 1
        else:
            if start <= stop:
                return 0
            return (start - stop - 1) // (-step) + 1


    def __getitem__(self, index:int)->int:
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            newstart = self[start]
            newstop = self[stop]
            newstep = self.step * step
            return MyRange(newstart, newstop, newstep)
        elif index < 0:
            index += len(self)
        elif index < 0 or index >= len(self):
            raise IndexError("out of range")        
        return self.start + index * self.step    

    def __contains__(self, value:int)->bool:
        if len(self) == 0:
            return False
        if self.step > 0:
            if value < self.start or value >= self.stop:
                return False
        else:
            if value > self.start or value <= self.stop:
                return False
        return (value - self.start) % abs(self.step) == 0 

    def __repr__(self):
        return f"{self.start, self.stop, self.step}"         

    def __eq__(self, other)->bool:
        return self.start == other.start and self.stop == other.stop and self.step == other.step


# Пример использования:
r = MyRange(1, 10, 2)

# Итерация
for i in r:
    print(i, end=" ")  # 1 3 5 7 9

# Длина
print()
print(len(r))  # 5

# Индексация
print(r[0])   # 1
print(r[-1])  # 9
print(r[1:3]) # MyRange(3, 7, 2) или [3, 5]

# Проверка вхождения
print(5 in r)  # True
print(6 in r)  # False

# Сравнение
print(r == MyRange(1, 10, 2))  # True

# Обратный порядок
print(list(reversed(r)))  # [9, 7, 5, 3, 1]