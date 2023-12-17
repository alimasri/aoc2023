from pathlib import Path
import re
from collections import defaultdict


def update_total(index: int, candidates: list, total: int) -> int:
    for number in candidates:
        if index in range(number["from"] - 1, number["to"] + 1):
            if not number.get("flag", False):
                total += number["value"]
                number["flag"] = True
    return total


def compute(stream: str) -> int:
    total = 0
    lookup = defaultdict(list)
    lines = stream.splitlines()
    for idx, line in enumerate(lines):
        for match in re.finditer("(\d+)", line):
            _from, _to = match.span()
            value = line[_from:_to]
            lookup[idx].append({"value": int(value), "from": _from, "to": _to})
    for i, line in enumerate(lines):
        for j, character in enumerate(line):
            if character.isdigit() or character == ".":
                continue
            # get the matches on the previous row
            if i > 0:
                total = update_total(j, lookup[i - 1], total)
            # get the matches on the same row
            total = update_total(j, lookup[i], total)
            # get the matches on the next row
            if i != len(lines):
                total = update_total(j, lookup[i + 1], total)
    return total


def test_compute():
    stream = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..\
"""
    assert compute(stream) == 4361


if __name__ == "__main__":
    stream = Path("input.txt").read_text()
    print(compute(stream))
