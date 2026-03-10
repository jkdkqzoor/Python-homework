"""
Задание 2. Student и Group (подготовка к следующему занятию)

Создайте класс Student:

    Атрибуты: name, age, grades (список оценок)
    Метод add_grade(grade) — добавляет оценку
    Метод average_grade() — возвращает средний балл

Создайте класс Group:

    Атрибуты: name (название группы), students (список студентов)
    Метод add_student(student) — добавляет студента
    Метод remove_student(name) — удаляет студента по имени

Эти классы понадобятся на следующем занятии для изучения магических методов!
"""

class Student:
    name:str
    age:int
    grades:list

    def add_grade(self, grade:int)->None:
        self.grades.append(grade)

    def average_grade(self)->float:
        return round(sum(self.grades)/len(self.grades), 2)
    

class Group:
    name:str
    students:list[Student]
    
    def add_student(self, student:Student)->None:
        self.students.append(Student)

    def remove_student(self, name:str)->None:
        for student in self.students:
            if student.name == name:
                self.students.remove(student) 


