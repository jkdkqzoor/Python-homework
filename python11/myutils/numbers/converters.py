"""Number conversion utilities."""

ROMAN_MAP = [
    (1000, 'M'), (900, 'CM'),
    (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'),
    (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'),
    (5, 'V'), (4, 'IV'),
    (1, 'I')
]


def to_roman(num: int) -> str:
    """Convert integer to Roman numeral."""
    result = ""
    for value, symbol in ROMAN_MAP:
        while num >= value:
            result += symbol
            num -= value
    return result


def from_roman(s: str) -> int:
    """Convert Roman numeral to integer."""
    roman_dict = dict(ROMAN_MAP)
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in roman_dict:
            num += roman_dict[s[i:i+2]]
            i += 2
        else:
            num += roman_dict[s[i]]
            i += 1
    return num


def to_binary(num: int) -> str:
    """Convert integer to binary string."""
    return bin(num)[2:]


if __name__ == "__main__":
    print(to_roman(42))
    print(from_roman("XLII"))
    print(to_binary(10))