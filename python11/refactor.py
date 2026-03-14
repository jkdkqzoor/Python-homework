"""
Задание 4. Рефакторинг по PEP8

Исправьте следующий код, чтобы он соответствовал PEP8:

# bad_code.py — исправьте этот код

import sys,os
from collections import Counter,defaultdict
import random

def Calculate_Average(numbers_list):
    ""this function calculates average""
    if len(numbers_list)==0:return 0
    total=0
    for n in numbers_list:total+=n
    return total/len(numbers_list)

class user_account:
    def __init__(self,Name,email,Age):
        self.name=Name;self.email=email;self.age=Age
    def GetInfo(self):
        return f"User: {self.name}, Email: {self.email}"
    def is_adult(self):
        if self.age>=18:
            return True
        else:
            return False

def   process_data(  data,   flag=True):
    result=[]
    for item in data:
        if flag==True:
            result.append(item*2)
        else:
            result.append(item)
    return result

x=10
y=20
z=x+y
list1=[1,2,3,4,5]
dict1={"a":1,"b":2}

Что нужно исправить:

    Импорты (порядок, группировка).
    Именование (функции, классы, переменные).
    Пробелы (вокруг операторов, после запятых).
    Составные инструкции.
    Упрощение условий.
    Добавить docstrings.

"""
import os
import sys
import random
from collections import Counter, defaultdict


def calculate_average(numbers_list: list[int]) -> float:
    """Calculate the average of a list of numbers.

    Args:
        numbers_list (list[int]): List of numeric values.

    Returns:
        float: The average value, or 0 if the list is empty.
    """
    if not numbers_list:
        return 0
    return sum(numbers_list) / len(numbers_list)


class UserAccount:
    """Represents a user account with name, email, and age.

    Methods:
        get_info() -> str: Returns formatted user info.
        is_adult() -> bool: Checks if user is 18 or older.
    """

    def __init__(self, name: str, email: str, age: int):
        self.name = name
        self.email = email
        self.age = age

    def get_info(self) -> str:
        """Return user information as a formatted string."""
        return f"User: {self.name}, Email: {self.email}"

    def is_adult(self) -> bool:
        """Return True if user is 18 or older, otherwise False."""
        return self.age >= 18


def process_data(data: list[int], flag: bool = True) -> list[int]:
    """Process a list of data by optionally doubling each item.

    Args:
        data (list[int]): Input list of numbers.
        flag (bool, optional): If True, double each item. Defaults to True.

    Returns:
        list[int]: Processed list.
    """
    result = []
    for item in data:
        result.append(item * 2 if flag else item)
    return result


# Example variables
x = 10
y = 20
z = x + y

list1 = [1, 2, 3, 4, 5]
dict1 = {"a": 1, "b": 2}