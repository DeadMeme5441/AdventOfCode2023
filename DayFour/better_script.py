import time

def check_if_winning(winning_numbers, test_numbers):
    count = 0

    for n in winning_numbers:
        if n in test_numbers:
            count = count + 1

    return count

def part_two():

    lines = []

    with open('input.txt', 'r') as f:
        lines = f.readlines()

    cards = {}
    sum_one = 0

    for i in range(1, len(lines) + 1):
        cards[i] = 1

    for line in lines:
        num = int(line.split(':')[0].split(' ')[-1])
        count = 0

        winning_numbers = [int(x) for x in line.split(':')[1].split('|')[0].strip().split(' ') if x!= '']

        test_numbers = [int(x) for x in line.split(':')[1].split('|')[1].strip().split(' ') if x != '']

        count = check_if_winning(winning_numbers, test_numbers)

        if count:
            sum_one += 2 ** (count - 1)

        for i in range(0, count):
            cards[num + i + 1] += cards[num]

    return sum_one, sum([x for x in cards.values()])


if __name__ == '__main__':
    start = time.time()
    out = part_two()
    print("Part one: {}".format(out[0]))
    print("Part two: {}".format(out[1]))
    print("Time: {} ms".format(round((time.time() - start) * 1000, 3)))
