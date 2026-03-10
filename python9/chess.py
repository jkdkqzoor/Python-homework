"""
Задание 1. Шахматные фигуры (наследование, абстракция, полиморфизм)

Создайте базовый класс ChessPiece:

    Атрибуты: color (белый/чёрный), position (кортеж из двух чисел 0-7)
    Метод change_color() — меняет цвет на противоположный
    Метод set_position(x, y) — устанавливает позицию (с проверкой границ 0-7)
    Защищённый метод _is_valid_position(x, y) — проверяет, что координаты в пределах доски
    Абстрактный метод can_move_to(x, y) — проверяет, может ли фигура пойти на указанную клетку

Создайте классы-наследники для каждой фигуры:

    Pawn (пешка) — ходит на 1 клетку вперёд (направление зависит от цвета)
    Rook (ладья) — ходит по горизонтали или вертикали
    Knight (конь) — ходит буквой «Г»
    Bishop (слон) — ходит по диагонали
    Queen (ферзь) — ходит как ладья + слон
    King (король) — ходит на 1 клетку в любом направлении

# Пример использования:
rook = Rook("white", (0, 0))
print(rook.can_move_to(0, 5))  # True (по вертикали)
print(rook.can_move_to(3, 3))  # False (по диагонали нельзя)

knight = Knight("black", (1, 0))
print(knight.can_move_to(2, 2))  # True (буква «Г»)

Напишите функцию pieces_that_can_reach(pieces: list, x: int, y: int) -> list, которая возвращает список фигур, способных достичь указанной клетки за один ход.
"""

class ChessPiece:
    def __init__(self, color:str, position:tuple):
        self.color = color
        self.position = position

    def change_color(self):
        if self.color == "black":
            self.color = "white"
        else:
            self.color = "black"

    def set_position(self, x:int,y:int)->tuple:
        if self._is_valid_position(x, y):
            self.position = (x, y)
        else:
            raise ValueError

    def _is_valid_position(self, x:int, y:int)->bool:
        return x >= 0 and x < 8 and y < 8 and y >= 0
    
    def can_move_to(self, x:int,y:int):
        raise NotImplementedError


class Pawn(ChessPiece):
    def can_move_to(self, x:int, y:int)->bool:
        if not self._is_valid_position(x, y):
            return False
        return self.color == "white" and y == self.position[1] + 1 or y == self.position[0] - 1
            
        
class Rook(ChessPiece):
    def can_move_to(self, x:int, y:int)->bool:
        if not self._is_valid_position(x, y):
            return False
        
        cx, cy = self.position
        return x == cx or y == cy
    

class Knight(ChessPiece):
    def can_move_to(self, x:int, y:int)->bool:
        if not self._is_valid_position(x, y):
            return False
        
        cx, cy = self.position
        dx = abs(x-cx)
        dy = abs(y - cy)

        return (dx, dy) in [(1, 2), (2, 1)]
    

class Bishop(ChessPiece):
    def can_move_to(self, x:int, y:int)->bool:
        if not self._is_valid_position(x, y):
            return False
        
        cx, cy = self.position

        return abs(x - cx) == abs(y - cy)


class Queen(ChessPiece):
    def can_move_to(self, x:int, y:int)->bool:
        if not self._is_valid_position(x, y):
            return False
        
        cx, cy = self.position
        return (x == cx or y == cy) or (abs(x - cx) == abs(y - cy))
    

class King(ChessPiece):
    def can_move_to(self, x:int, y:int)->bool:
        if not self._is_valid_position(x, y):
            return False
        
        cx, cy = self.position

        return max(abs(x - cx), abs(y - cy)) == 1


def pieces_that_can_reach(pieces: list, x:int, y:int) -> list:
    result = []
    for piece in pieces:
        if piece.can_move_to(x,y):
            result.append(piece)
    
    return result


rook = Rook("white",(0, 0))
print(rook.can_move_to(0,5))
print(rook.can_move_to(3,3))

knight = Knight("black",(1,0))
print(knight.can_move_to(2,2))