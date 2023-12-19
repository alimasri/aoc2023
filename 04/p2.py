from pathlib import Path


def compute(stream: str) -> int:
    lines = stream.splitlines()
    nb_cards = len(lines)
    copies = {} 
    for card_id, line in enumerate(lines, 1):
        copies[card_id] = copies.get(card_id, 0) + 1
        card_info = line.split(": ")[1]
        winning_cards, my_cards = card_info.split(" | ")
        winning_cards = set(winning_cards.split())
        my_cards = set(my_cards.split())
        nb_matches = len(winning_cards.intersection(my_cards))
        for i in range(
            card_id + 1,
            min(nb_cards + 1, card_id + nb_matches + 1)
        ):
            copies[i] = copies.get(card_id, 1) + copies.get(i, 0)
    return sum(copies.values())

def test_compute():
    stream = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11\
"""
    assert compute(stream) == 30


if __name__ == "__main__":
    stream = Path("input.txt").read_text()
    print(compute(stream))
