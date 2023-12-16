CONSTRAINTS = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def game_valid(game: str) -> bool:
    for s in game.split(";"):
        counter = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for item in s.split(","):
            num, color = item.strip().split(" ")
            counter[color] += int(num)
            if counter[color] > CONSTRAINTS[color]:
                return False
    return True

def compute(stream: str) -> int:
    import re
    pattern = re.compile(r"Game\s\d+:(.*)")
    total = 0
    for idx, line in enumerate(stream.splitlines(), 1):
        game = pattern.search(line).group(1).strip()
        if game_valid(game):
            total += idx
    return total
        

def test_compute():
    scenario = """\
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green\
    """
    assert compute(scenario) == 8


if __name__ == "__main__":
    from pathlib import Path
    stream = Path("input.txt").read_text()
    print(compute(stream))
