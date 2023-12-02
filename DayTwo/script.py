import time

def process_hands(hands):
    cond = {
        "red" : 12,
        "green" : 13,
        "blue" : 14,
    }

    for hand in hands:
        balls = hand.split(',')
        for ball in balls:
            temp = ball.strip().split(' ')
            if int(temp[0]) > cond[temp[1]]:
                return False

    return True

def part_one():
    valid_hands = 0

    with open('input.txt') as file:
        for line in file:
            hand_id,hands = line.split(':')

            if process_hands(hands.split(';')):
                valid_hands += int(hand_id.split(" ")[1])

    return valid_hands

def process_hands_two(hands):
    cond = {
        "red" : 0,
        "green" : 0,
        "blue" : 0,
    }

    for hand in hands:
        balls = hand.split(',')
        for ball in balls:
            temp = ball.strip().split(' ')
            if int(temp[0]) > cond[temp[1]]:
                cond[temp[1]] = int(temp[0])

    return cond["red"] * cond["green"] * cond["blue"]

def part_two():
    valid_hands = 0

    with open('input.txt') as file:
        for line in file:
            hands = line.split(':')[1].split(";")
            valid_hands += process_hands_two(hands)

    return valid_hands

if __name__ == '__main__':
    start = time.time()
    print("Part one: {}".format(part_one()))
    print("Time: {} ms".format(round((time.time() - start) * 1000, 6)))

    start = time.time()
    print("Part two: {}".format(part_two()))
    print("Time: {} ms".format(round((time.time() - start) * 1000, 6)))

