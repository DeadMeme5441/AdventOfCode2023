import time

def part_one():
    lines = []

    with open("input.txt", "r") as f:
        lines = f.readlines()

    total = 0
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for line in lines:
        numbers = []
        for n in num:
            left = line.find(n)
            right = line.rfind(n)
            if left != -1:
                numbers.append((left, int(n)))
            if right != -1 and right != left:
                numbers.append((right, int(n)))

        numbers.sort()

        total += numbers[0][1] * 10 + numbers[-1][1]


    return total

def part_two():
    lines = []

    with open("input.txt", "r") as f:
        lines = f.readlines()

    total = 0

    num_dict = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9
    }

    for line in lines:
        numbers = []
        for n in num_dict:
            left = line.find(n)
            right = line.rfind(n)
            if left != -1:
                numbers.append((left, num_dict[n]))
            if right != -1 and right != left:
                numbers.append((right, num_dict[n]))

        numbers.sort()

        total += numbers[0][1] * 10 + numbers[-1][1]

    return total

if __name__ == '__main__':
    start = time.time()
    print("Part one: {}".format(part_one()))
    print("Time: {} ms".format(round((time.time() - start) * 1000, 3)))

    start = time.time()
    print("Part two: {}".format(part_two()))
    print("Time: {} ms".format(round((time.time() - start) * 1000, 3)))
