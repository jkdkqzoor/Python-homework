"""String formatting utilities."""

import re


def to_snake_case(text: str) -> str:
    """Convert CamelCase to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def to_camel_case(text: str) -> str:
    """Convert snake_case to CamelCase."""
    return ''.join(word.capitalize() for word in text.split('_'))


def truncate(text: str, length: int = 10) -> str:
    """Truncate string to a specific length."""
    return text if len(text) <= length else text[:length] + "..."


if __name__ == "__main__":
    print(to_snake_case("HelloWorld"))
    print(to_camel_case("hello_world"))
    print(truncate("Hello Python World", 8))