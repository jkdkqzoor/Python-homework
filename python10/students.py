"""
Задание 1. Расширение класса Group (контейнерные методы)

Возьмите класс Group и добавьте магические методы, чтобы группа вела себя как контейнер:

    __len__ — количество студентов в группе
    __getitem__(index) — получение студента по индексу
    __setitem__(index, student) — замена студента по индексу
    __delitem__(index) — удаление студента по индексу
    __iter__ — итерация по студентам
    __contains__(student) — проверка, есть ли студент в группе

# Пример использования:
group = Group("Python-101")
group.add_student(Student("Иван", 20, [4, 5]))
group.add_student(Student("Мария", 19, [5, 5]))
group.add_student(Student("Пётр", 21, [3, 4]))

print(len(group))  # 3
print(group[0].name)  # Иван
print(Student("Мария", 19, [5, 5]) in group)  # True

for student in group:
    print(student)

# Найти лучшего студента
best = max(group)
print(f"Лучший студент: {best.name}")
"""

class Student:
    name:str
    age:int
    grades:list[int]
    def __init__(self, name:str, age:int, grades:list[int]=None):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade:int):
        self.grades.append(grade)
    
    def average_grade(self)->float:
        return sum(self.grades)/len(self.grades)

    def __str__(self)->str:
        return f"Student: {self.name}, avg: {round(self.average_grade(), 2)}"

    def __repr__(self)->str:
        return f"Student('{self.name}', {self.age}, {self.grades})"
    
    def __eq__(self,other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()


class Group:
    name:str
    students:list[Student]
    def __init__(self, name:str):
        self.name = name
        self.students = []
        self.counter = 0

    def __len__(self)->int:
        return len(self.students)
    
    def __getitem__(self, index:int)->Student:
        return self.students[index]

    def __setitem__(self, index, student:Student):
        self.students[index] = student

    def __delitem__(self, index:int):
        self.students.remove(index)

    def __iter__(self):
        yield from self.students

    def __next__(self):
        for student in self.students:
            yield student

    def add_student(self, student:Student):
        self.students.append(student)

    def __contains__(self, student:Student)->bool:
        for stud in self.students:
            if student.name == stud.name:
                return True
        else:
            return False
        

# s1 = Student("Ivan",20, [4, 5 ,5])
# s2 = Student("Mary",19,[5,5,5])
# s3 = Student("Petr",21, [3,4,4])

# print(s1)
# print(repr(s2))
# students = [s1,s2,s3]
# print(max(students).name)

# Пример использования:
group = Group("Python-101")
group.add_student(Student("Иван", 20, [4, 5]))
group.add_student(Student("Мария", 19, [5, 5]))
group.add_student(Student("Пётр", 21, [3, 4]))

print(len(group))  # 3
print(group[0].name)  # Иван
print(Student("Мария", 19, [5, 5]) in group)  # True

for student in group:
    print(student)

# Найти лучшего студента
best = max(group)
print(f"Лучший студент: {best.name}")