"""
Задание 5. ⭐ Банковская система (комплексное)

Создайте систему банковских счетов:

Исключения:

    BankError — базовое исключение
    InsufficientFundsError — недостаточно средств
    InvalidAmountError — некорректная сумма (отрицательная или ноль)

Базовый класс Account:

    Атрибуты: account_number, owner_name, _balance (защищённый)
    Метод deposit(amount) — пополнение (с валидацией суммы)
    Метод withdraw(amount) — снятие (с проверкой баланса)
    Метод get_balance() — возвращает баланс
    Метод transfer(other_account, amount) — перевод на другой счёт

Класс SavingsAccount(Account):

    Дополнительный атрибут interest_rate (процентная ставка)
    Метод add_interest() — начисляет проценты на баланс
    Переопределите withdraw() — нельзя снять больше 50% баланса за раз

Класс CheckingAccount(Account):

    Дополнительный атрибут overdraft_limit (лимит овердрафта)
    Переопределите withdraw() — можно уходить в минус до лимита овердрафта

# Пример использования:
savings = SavingsAccount("001", "Alice", interest_rate=0.05)
savings.deposit(1000)
savings.add_interest()
print(savings.get_balance())  # 1050.0

checking = CheckingAccount("002", "Bob", overdraft_limit=500)
checking.deposit(100)
checking.withdraw(400)  # OK, баланс = -300 (в пределах овердрафта)
print(checking.get_balance())  # -300

try:
    checking.withdraw(300)  # Превысит лимит овердрафта
except InsufficientFundsError as e:
    print(e)


"""

class BankError(Exception):
    """Base exeption"""
    pass


class InsufficientFundsError(BankError):
    """Not enough funds"""
    pass


class InvalidAmmountError(InsufficientFundsError):
    """Invalid ammount"""
    pass


class Account:
    account_number:int
    owner_name:str
    _balance:float
    def __init__(self, account_number:int, owner_name:str):
        self.account_number = account_number
        self.owner_name = owner_name
        self._balance = 0
        
    def deposit(self, amount:float)->None:
        if amount <= 0 :
            raise InvalidAmmountError("Invalid amount")
        else:
            self._balance += amount

    def withdraw(self, amount:float)->None:
        if amount > self._balance:
            raise InsufficientFundsError("insufficient funds")
        else:
            self._balance -= amount

    def get_balance(self)->float:
        return self._balance
    
    def transfer(self, other_account, amount:float)->None:
        if amount > self._balance:
            raise InsufficientFundsError("insufficient funds")
        else:
            self._balance -= amount
            other_account._balance += amount


class SavingsAccount(Account):
    interest_rate:float
    def __init__(self, account_number:int, owner_name:str, interest_rate:float):
        super().__init__(account_number, owner_name)
        self.interest_rate = interest_rate

    def add_interest(self)->None:
        self._balance += self._balance * self.interest_rate

    def withdraw(self, amount:float)->None:
        if amount * 2 > self._balance:
            raise InvalidAmmountError(r"u cant withdraw more than 50% of balance")
    

class CheckingAccount(Account):
    overdraft_limit:int
    def __init__(self, account_number:int, owner_name:str, overdraft_limit:int):
        super().__init__(account_number, owner_name)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount:float)->None:
        if amount > self._balance + self.overdraft_limit:
            raise InvalidAmmountError("invalid ammount to withdraw, more than overdraft limit")
        else:
            self._balance -= amount


# Пример использования:
savings = SavingsAccount("001", "Alice", interest_rate=0.05)
savings.deposit(1000)
savings.add_interest()
print(savings.get_balance())  # 1050.0

checking = CheckingAccount("002", "Bob", overdraft_limit=500)
checking.deposit(100)
checking.withdraw(400)  # OK, баланс = -300 (в пределах овердрафта)
print(checking.get_balance())  # -300

try:
    checking.withdraw(300)  # Превысит лимит овердрафта
except InsufficientFundsError as e:
    print(e)