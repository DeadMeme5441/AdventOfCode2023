import time
from collections import Counter

def score_hand(hand):

    hand_dict = Counter(hand)

    if 5 in hand_dict.values():
        return 7
    elif 4 in hand_dict.values():
        return 6
    elif 3 in hand_dict.values() and 2 in hand_dict.values():
        return 5
    elif 3 in hand_dict.values():
        return 4
    elif list(hand_dict.values()).count(2) == 2:
        return 3
    elif 2 in hand_dict.values():
        return 2
    else:
        return 1

def compare_two_hands(hand_one, hand_two):
    cards = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J","Q", "K", "A"]

    for j in range(5):
        if cards.index(hand_one[j]) > cards.index(hand_two[j]):
            return hand_one
        elif cards.index(hand_one[j]) < cards.index(hand_two[j]):
            return hand_two

    return 0

def hand_sorter(hands):
    n = len(hands)

    swapped = False

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if compare_two_hands(hands[j][0], hands[j + 1][0]) == hands[j][0]:
                hands[j], hands[j + 1] = hands[j + 1], hands[j]
                swapped = True

        if swapped == False:
            return hands

    return hands

def part_one():

    hands = []

    scores = {}

    for i in range(1, 8):
        scores[i] = []

    with open("input.txt", "r") as f:
        for line in f:
            hands.append(line.strip().split(" "))

    for hand in hands:
        scores[score_hand(hand[0])].append(hand)

    final_hands = []

    for i in range(1, 8):
        final_hands.extend(hand_sorter(scores[i]))

    score = 0

    for i in range(len(final_hands)):
        score += (i + 1) * int(final_hands[i][1])

    return score

def part_two():

    hands = []

    scores = {}

    for i in range(1, 8):
        scores[i] = []

    with open("input.txt", "r") as f:
        for line in f:
            hands.append(line.strip().split(" "))

    for hand in hands:
        max_score = 0
        for char in hand[0]:
            test = hand[0].replace("J",char)
            max_score = max(max_score, score_hand(test))

        scores[max_score].append(hand)

    final_hands = []

    for i in range(1, 8):
        final_hands.extend(hand_sorter(scores[i]))

    score = 0

    for i in range(len(final_hands)):
        score += (i + 1) * int(final_hands[i][1])

    return score


if __name__ == '__main__':
    start = time.time()
    print("Part one: {}".format(part_one()))
    print("Time: {} ms".format(round((time.time() - start) * 1000, 3)))

    start = time.time()
    print("Part two: {}".format(part_two()))
    print("Time: {} ms".format(round((time.time() - start) * 1000, 3)))
