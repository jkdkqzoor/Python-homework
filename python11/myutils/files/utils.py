"""File read/write utilities."""

import json
import csv


def read_json(path):
    """Read JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path, data):
    """Write JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def read_csv(path):
    """Read CSV file."""
    with open(path, newline='', encoding="utf-8") as f:
        return list(csv.reader(f))


def write_csv(path, rows):
    """Write CSV file."""
    with open(path, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


if __name__ == "__main__":
    write_json("test.json", {"name": "Alice"})
    print(read_json("test.json"))