"""
Задание 4. Собственные исключения

Создайте иерархию исключений для системы валидации:

class ValidationError(Exception):
    ""Базовое исключение валидации""
    pass

class EmptyValueError(ValidationError):
    ""Значение пустое""
    pass

class InvalidRangeError(ValidationError):
    ""Значение вне допустимого диапазона""
    pass

Создайте класс User:

    Атрибуты: username, age, email
    В __init__ валидируйте данные:
        username не должен быть пустым → EmptyValueError
        age должен быть от 0 до 150 → InvalidRangeError
        email должен содержать @ → ValidationError

# Пример использования:
try:
    user = User("", 25, "test@mail.com")
except EmptyValueError as e:
    print(f"Ошибка: {e}")  # Ошибка: username cannot be empty

try:
    user = User("john", 200, "test@mail.com")
except InvalidRangeError as e:
    print(f"Ошибка: {e}")  # Ошибка: age must be between 0 and 150
"""

class ValidationError(Exception):
    """Базовое исключение валидации"""
    pass


class EmptyValueError(ValidationError):
    """Значение пустое"""
    pass


class InvalidRangeError(ValidationError):
    """Значение вне допустимого диапазона"""
    pass


class User:
    username:str
    age:int
    email:str
    def __init__(self, username:str, age:int, email:str):
        if not username:
            raise EmptyValueError("username cannot be empty")
        else:
            self.username = username
        if age < 0 or age > 150:
            raise InvalidRangeError("age must be between 0 and 150")
        else:
            self.age = age
        if not "@" in email:
            raise ValidationError("invalid email")
        else:
            self.email = email       


try:
    user = User("", 25, "test@mail.com")
except EmptyValueError as e:
    print(f"Ошибка: {e}")  # Ошибка: username cannot be empty

try:
    user = User("john", 200, "test@mail.com")
except InvalidRangeError as e:
    print(f"Ошибка: {e}")  # Ошибка: age must be between 0 and 150