"""String validation utilities."""

import re


def is_email(text: str) -> bool:
    """Check if string is a valid email."""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, text))


def is_phone(text: str) -> bool:
    """Check if string is a phone number."""
    pattern = r"^\+?\d{10,15}$"
    return bool(re.match(pattern, text))


def is_url(text: str) -> bool:
    """Check if string is a URL."""
    pattern = r"^https?://[\w\.-]+\.\w+"
    return bool(re.match(pattern, text))


if __name__ == "__main__":
    print(is_email("test@example.com"))
    print(is_phone("+12345678901"))
    print(is_url("https://example.com"))