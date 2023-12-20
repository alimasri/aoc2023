from pathlib import Path


def src2dst(mapping: str) -> dict:
    result = []
    for line in mapping.splitlines()[1:]:
        dst, src, rng = map(int, line.split())
        rng += 1
        result.append((range(src, src + rng), (range(dst, dst + rng))))
    return result


def find_dest(src, mappings):
    for src_range, dst_range in mappings:
        if src in src_range:
            idx = src - src_range[0]
            return dst_range[idx]
    return src


def compute(stream: str) -> int:
    lines = stream.split("\n\n")
    seeds, *rest = lines
    seeds = map(int, seeds.split(": ")[-1].split())
    mappings = [src2dst(line) for line in rest]
    locations = []
    for seed in seeds:
        src = seed
        for mapping in mappings: 
            dst = find_dest(src, mapping)
            src = dst
        locations.append(dst)
    return min(locations)


def test_compute():
    stream = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
    assert compute(stream) == 35


if __name__ == "__main__":
    stream = Path("input.txt").read_text()
    print(compute(stream))
