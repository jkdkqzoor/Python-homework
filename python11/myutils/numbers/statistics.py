"""Basic statistics functions."""

import math
from collections import Counter


def mean(data):
    """Calculate mean value."""
    return sum(data) / len(data)


def median(data):
    """Calculate median value."""
    data = sorted(data)
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    return data[mid]


def mode(data):
    """Calculate mode value."""
    counts = Counter(data)
    return counts.most_common(1)[0][0]


def std_dev(data):
    """Calculate standard deviation."""
    m = mean(data)
    variance = sum((x - m) ** 2 for x in data) / len(data)
    return math.sqrt(variance)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(mean(nums))
    print(median(nums))
    print(mode(nums))
    print(std_dev(nums))