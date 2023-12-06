import time
import math
from multiprocessing import Pool

def part_one():

    lines = []

    with open('input.txt', 'r') as file:
        lines = file.read()

    blocks = lines.split('\n\n')

    seeds, rules = blocks[0], blocks[1:]

    seeds = [int(x) for x in seeds.split(':')[1].split(' ') if x != '']

    mappings = []

    for rule in rules:
        vals = map(str.split, rule.splitlines()[1:])
        temp = []

        for to_range, from_range, length in vals:
            temp.append({"lower" : int(from_range), "upper" : int(from_range) + int(length) + 1, "offset" : int(to_range) - int(from_range)})

        mappings.append(temp)

    lowest = math.inf
    for seed in seeds:
        source = seed
        for mapping in mappings:
            for m in mapping:
                if m["lower"] <= source <= m["upper"]:
                    source += m["offset"]
                    break
        lowest = min(source, lowest)

    return lowest


def multi_calc(seeds_two):
    lines = []

    with open('input.txt', 'r') as file:
        lines = file.read()

    blocks = lines.split('\n\n')

    seeds, rules = blocks[0], blocks[1:]

    seeds = list(map(int, seeds.split(':')[1].split()))

    seeds_two = zip(seeds[::2], seeds[1::2])
    mappings = []

    for rule in rules:
        vals = map(str.split, rule.splitlines()[1:])
        temp = []

        for to_range, from_range, length in vals:
            temp.append({"lower" : int(from_range), "upper" : int(from_range) + int(length) + 1, "offset" : int(to_range) - int(from_range)})

        mappings.append(temp)

    lowest = math.inf
    
    for seed, seed_range in seeds_two:
        for i in range(seed_range):
            source = seed + i
            for mapping in mappings:
                for m in mapping:
                    if m["lower"] <= source <= m["upper"]:
                        source += m["offset"]
                        break
            lowest = min(source, lowest)

    return lowest


def part_two():
    lines = []

    with open('input.txt', 'r') as file:
        lines = file.read()

    blocks = lines.split('\n\n')

    seeds, rules = blocks[0], blocks[1:]

    seeds = list(map(int, seeds.split(':')[1].split()))

    seeds_two = zip(seeds[::2], seeds[1::2])

    pool = Pool(10)

    lowest = pool.map(multi_calc, seeds_two)

    return min(lowest)
    

if __name__ == '__main__':
    start = time.time()
    print("Part one: {}".format(part_one()))
    print("Time: {} ms".format(round((time.time() - start) * 1000, 3)))

    start = time.time()
    print("Part two: {}".format(part_two()))
    print("Time: {} ms".format(round((time.time() - start) * 1000, 3)))
