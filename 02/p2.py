import re
from functools import reduce
from pathlib import Path


def compute(stream: str) -> int:
    pattern = re.compile(r"Game\s\d+:(.*)")
    total = 0
    for line in stream.splitlines():
        game = pattern.search(line).group(1).strip()
        min_set = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for _set in game.split(";"):
            for draw in _set.split(","):
                num, color = draw.strip().split(" ")
                num = int(num)
                if num > min_set[color]:
                    min_set[color] = num
        total += reduce(lambda a, b: a * b, min_set.values())
    return total


def test_compute():
    scenario = """\
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green\
    """
    assert compute(scenario) == 2286


if __name__ == "__main__":
    stream = Path("input.txt").read_text()
    print(compute(stream))
