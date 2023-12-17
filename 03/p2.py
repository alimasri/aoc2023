from pathlib import Path
import re
from collections import defaultdict

def calculate_gear_ratio(index: int, candidates: list) -> int:
    adj = []
    for number in candidates:
        if index in range(number["from"] - 1, number["to"] + 1):
            if not number.get("flag", False):
                adj.append(number["value"])
                if len(adj) > 2:
                    return 0
    if len(adj) == 2:
        return adj[0] * adj[1]        
    return 0


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
            if character != "*":
                continue
            all_candidates = []
            if i > 0:
                all_candidates.extend(lookup[i - 1])
            all_candidates.extend(lookup[i])
            if i != len(lines):
                all_candidates.extend(lookup[i + 1])
            total += calculate_gear_ratio(j, all_candidates)
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
    assert compute(stream) == 467835


if __name__ == "__main__":
    stream = Path("input.txt").read_text()
    print(compute(stream))
