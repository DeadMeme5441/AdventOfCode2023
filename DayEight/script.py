import time
from math import lcm

def find_path(nodes, start, rules):

    i = 0
    current_pos = start
    steps = 0
    while i < len(rules):
        if rules[i] == "R":
            current_pos = nodes[current_pos][1]
        elif rules[i] == "L":
            current_pos = nodes[current_pos][0]


        steps += 1

        if current_pos[-1] == "Z":
            break

        if i == len(rules) - 1:
            i = -1
        i += 1

    return steps

def part_one():

    rules = ""
    nodes = {}

    with open("input.txt", "r") as file:
        rules = file.readline().strip()
        empty = file.readline()

        for line in file.readlines():
            nodes[line.split("=")[0].strip()]= [x.replace("(","").replace(")","").strip() for x in line.split("=")[1].strip().split(",")]


    steps = find_path(nodes, "AAA", rules)
    return steps

def part_two():

    rules = ""
    nodes = {}

    with open("input.txt", "r") as file:
        rules = file.readline().strip()
        empty = file.readline()

        for line in file.readlines():
            nodes[line.split("=")[0].strip()]= [x.replace("(","").replace(")","").strip() for x in line.split("=")[1].strip().split(",")]


    current_pos = [x for x in nodes.keys() if x[-1] == "A"]
    all_steps = []
    for pos in current_pos:
        steps = find_path(nodes, pos, rules)
        all_steps.append(steps)

    return lcm(*all_steps)



if __name__ == '__main__':
    start = time.time()
    print("Part one: {}".format(part_one()))
    print("Time: {} ms".format(round((time.time() - start) * 1000, 3)))

    start = time.time()
    print("Part two: {}".format(part_two()))
    print("Time: {} ms".format(round((time.time() - start) * 1000, 3)))
