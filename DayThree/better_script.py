import time

def check_valid(lines, positions):

    for pos in positions:
        i = pos[0]
        j = pos[1]

        x_pos = [x for x in range(i-1, i+2) if x >= 0 and x < len(lines)]
        y_pos = [x for x in range(j-1, j+2) if x >= 0 and x < len(lines)]

        for x in x_pos:
            for y in y_pos:
                if lines[x][y] != '.' and not lines[x][y].isdigit():
                    if lines[x][y] == '*':
                        return (x,y)
                    else:
                        return True

    return False

def part_one():
    lines = []

    with open('input.txt', 'r') as f:
        for line in f:
            temp = []
            for i in line.strip():
                temp.append(i)
            lines.append(temp)


    sum = 0

    gears = {}

    for i in range(len(lines)):
        digit = ""
        pos = []
        j = 0
        while j < len(lines[i]):

            if lines[i][j].isdigit():
                digit += lines[i][j]
                pos.append((i, j))
                j += 1

            else:
                if len(digit) > 0:
                    out = check_valid(lines, pos)
                    if out:
                        sum += int(digit)

                    if type(out) != bool:
                        if out not in gears:
                            gears[out] = []
                        gears[out].append(int(digit))

                    digit = ""
                    pos = []
                j += 1

            if j == len(lines[i]):
                if len(digit) > 0:
                    out = check_valid(lines, pos)
                    if out:
                        sum += int(digit)

                    if type(out) != bool:
                        if out not in gears:
                            gears[out] = []
                        gears[out].append(int(digit))

                    digit = ""
                    pos = []

    gears_sum = 0
    for gear in gears:
        if len(gears[gear]) > 1:
            gears_sum += gears[gear][0] * gears[gear][1]

    return sum, gears_sum


if __name__ == '__main__':
    start = time.time()
    out = part_one()
    print("Part one: {}".format(out[0]))
    print("Part two: {}".format(out[1]))
    print("Time: {} ms".format(round((time.time() - start) * 1000, 3)))

