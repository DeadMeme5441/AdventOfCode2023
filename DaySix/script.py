import time

def calculate_possibilities(time,record):
    for i in range(time):
        speed = i
        inv_speed = time - i
        distance = speed * inv_speed

        if distance > record:
            return (inv_speed - speed + 1)

    return 0

def part_one():
    times = []
    distances = []

    with open('input.txt', 'r') as f:
        lines = f.readlines()
        times = [int(x) for x in lines[0].strip().split(":")[1].split()]
        distances = [int(x) for x in lines[1].strip().split(":")[1].split()]

    races = list(zip(times, distances))

    out = 1

    for race in races:
        out = out * calculate_possibilities(race[0], race[1])

    return out

def part_two():
    times = []
    distances = []

    with open('input.txt', 'r') as f:
        lines = f.readlines()
        times = [int(x) for x in lines[0].strip().split(":")[1].split()]
        distances = [int(x) for x in lines[1].strip().split(":")[1].split()]

        race = [''.join(str(x) for x in times), ''.join(str(x) for x in distances)]

    out = calculate_possibilities(int(race[0]), int(race[1]))

    return out

if __name__ == '__main__':
    start = time.time()
    print("Part one: {}".format(part_one()))
    print("Time: {} ms".format(round((time.time() - start) * 1000, 3)))

    start = time.time()
    print("Part two: {}".format(part_two()))
    print("Time: {} ms".format(round((time.time() - start) * 1000, 3)))
