import time


def get_sequence(sequence, part_two=False):
    next_sequence = []

    for i in range(len(sequence) - 1):
        next_sequence.append(sequence[i + 1] - sequence[i])

    if not any(next_sequence):
        return sequence[-1] + next_sequence[-1]

    value = get_sequence(next_sequence, part_two)

    if part_two:
        return sequence[0] - value

    return sequence[-1] + value


def part_one():
    lines = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            temp = [int(x) for x in line.strip().split(" ")]
            lines.append(temp)

    sum = 0

    for line in lines:
        sum += get_sequence(line)

    return sum


def part_two():
    lines = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            temp = [int(x) for x in line.strip().split(" ")]
            lines.append(temp)

    sum = 0

    for line in lines:
        sum += get_sequence(line, True)

    return sum


if __name__ == "__main__":
    start = time.time()
    print("Part one: {}".format(part_one()))
    print("Time: {} ms".format(round((time.time() - start) * 1000, 3)))

    start = time.time()
    print("Part two: {}".format(part_two()))
    print("Time: {} ms".format(round((time.time() - start) * 1000, 3)))
