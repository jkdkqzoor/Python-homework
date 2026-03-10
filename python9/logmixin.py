"""
Задание 3. Миксин для логирования

Создайте миксин LoggableMixin, который добавляет возможность логирования:

    Метод log(message) — печатает сообщение с именем класса и временем

from datetime import datetime

class LoggableMixin:
    def log(self, message: str):
        class_name = self.__class__.__name__
        time = datetime.now().strftime("%H:%M:%S")
        print(f"[{time}] {class_name}: {message}")

Создайте класс Order, который наследуется от LoggableMixin:

    Атрибуты: order_id, items (список товаров), status
    Метод add_item(item) — добавляет товар и логирует это
    Метод set_status(status) — меняет статус и логирует

# Пример использования:
order = Order(order_id=123)
order.add_item("Laptop")
# [14:30:15] Order: Added item: Laptop
order.set_status("shipped")
# [14:30:16] Order: Status changed to: shipped
"""

from datetime import datetime


class LoggableMixin:
    def log(self, message: str):
        class_name = self.__class__.__name__
        time = datetime.now().strftime("%H:%M:%S")
        print(f"[{time}] {class_name}: {message}")


class Order(LoggableMixin):
    order_id:int
    items:list
    status:str
    def __init__(self, order_id:int):
        self.order_id = order_id
        self.items = []
        self.status = ""

    def add_item(self, item:str)->None:
        self.items.append(item)
        self.log(f"Added item: {item}")

    def set_status(self, status:str)->None:
        self.status = status
        self.log(f"Status changed to {status}")


order = Order(order_id=123)
order.add_item("Laptop")
# [14:30:15] Order: Added item: Laptop
order.set_status("shipped")
# [14:30:16] Order: Status changed to: shipped