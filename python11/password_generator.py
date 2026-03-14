"""
Задание 2. Генератор паролей (модуль random)

Создайте гибкий генератор паролей:

import random
import string

def generate_password(
    length: int = 12,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_special: bool = True,
    exclude_chars: str = "",
    must_include: str = ""
) -> str:
    ""
    Генерирует случайный пароль.

    Args:
        length: длина пароля
        use_uppercase: использовать заглавные буквы
        use_lowercase: использовать строчные буквы
        use_digits: использовать цифры
        use_special: использовать спецсимволы
        exclude_chars: символы, которые нужно исключить
        must_include: символы, которые обязательно должны быть в пароле
    ""
    pass

def check_password_strength(password: str) -> str:
    ""
    Оценивает силу пароля.

    Returns:
        "weak", "medium", "strong" или "very strong"
    ""
    pass

# Пример использования:
pwd = generate_password(16, use_special=True)
print(pwd)  # "Kj#9xLm$2pQw&nRt"

print(check_password_strength("123456"))      # weak
print(check_password_strength("Password1"))   # medium
print(check_password_strength("Kj#9xLm$2p"))  # very strong
"""

import random
import string

def generate_password(
    length: int = 12,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_special: bool = True,
    exclude_chars: str = "",
    must_include: str = ""
) -> str:
    """
    Генерирует случайный пароль.

    Args:
        length: длина пароля
        use_uppercase: использовать заглавные буквы
        use_lowercase: использовать строчные буквы
        use_digits: использовать цифры
        use_special: использовать спецсимволы
        exclude_chars: символы, которые нужно исключить
        must_include: символы, которые обязательно должны быть в пароле
    """
    if length <= 0:
        raise ValueError("Length must be greater than 0")

    char_pool = ""

    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    char_pool = "".join(c for c in char_pool if c not in exclude_chars)

    if not char_pool:
        raise ValueError("Character pool is empty after exclusions")

    if len(must_include) > length:
        raise ValueError("must_include length cannot exceed password length")

    password_chars = list(must_include)

    while len(password_chars) < length:
        password_chars.append(random.choice(char_pool))

    random.shuffle(password_chars)
    return "".join(password_chars)


def check_password_strength(password: str) -> str:
    """
    Оценивает силу пароля.

    Returns:
        "weak", "medium", "strong" или "very strong"
    """
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_punctuation = any(c in string.punctuation for c in password)

    count = sum([has_upper, has_lower, has_digit, has_punctuation])

    if len(password) >= 10 and count == 4:
        return "very strong"
    elif count == 3 and len(password) >= 10:
        return "strong"
    elif count >= 3:
        return "medium"
    else:
        return "weak"


# Пример использования:
pwd = generate_password(16, use_special=True)
print(pwd)  # "Kj#9xLm$2pQw&nRt"

print(check_password_strength("123456"))      # weak
print(check_password_strength("Password1"))   # medium
print(check_password_strength("Kj#9xLm$2p"))  # very strong
