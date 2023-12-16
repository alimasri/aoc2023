from pathlib import Path
import re

letter2digit = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

PAT = fr'(\d|{("|".join(letter2digit))})'
REVERSED_PAT = fr'(\d|{("|".join(letter2digit)[::-1])})'

def compute(stream: str) -> int:
    total = 0
    for line in stream.splitlines():
        first = re.search(PAT, line)[0]
        last = re.search(REVERSED_PAT, line[::-1])[0][::-1]
        first_digit = int(letter2digit.get(first, first))
        last_digit = int(letter2digit.get(last, last))
        total += first_digit * 10 + last_digit
    return total


def test_compute():
    data = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
1twone\
    """
    assert compute(data) == 292


def main():
    input_file = Path(__file__).parent / "input.txt"
    input_data = input_file.read_text()

    print(compute(input_data))

    return 0


if __name__ == '__main__':
    main()
