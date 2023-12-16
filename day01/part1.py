from pathlib import Path

def compute(s: str) -> int:
    total = 0
    lines = s.splitlines()
    for line in lines:
        digits = [c for c in line if c.isdigit()]
        total += int(digits[0]) * 10 + int(digits[-1])
    return total


def test_compute():
    data = """\
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet\
    """
    assert compute(data) == 142

def main():
    input_file = Path(__file__).parent / "input.txt"
    input_data = input_file.read_text()

    print(compute(input_data))

    return 0

if __name__ == "__main__":
    exit(main())
