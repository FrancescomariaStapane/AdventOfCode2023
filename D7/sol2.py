import re
import functools

file = open("input.txt", "r")
lines = file.readlines()

hands_and_bids = {}
cards = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1
}


def getType(hand):
    differentCards = len({c for c in hand})
    if differentCards == 5:
        return 1  # high card
    if differentCards == 1:
        return 7  # five of a kind
    if differentCards == 3:  # two pair of three of a kind
        if re.match("^.*([ATJQK2-9]).*\\1.*\\1.*$", hand):
            return 4  # three of a kind
        return 3  # two pair
    if differentCards == 2:  # four of a kind or full house
        if re.match(".*([ATJQK2-9]).*\\1.*\\1.*\\1.*", hand):
            return 6  # four of a kind
        return 5  # full house
    return 2  # one pair


def getnewType(hand):
    if "J" not in hand:
        return getType(hand)
    ranks = []
    for card in cards.keys():
        ranks.append(getType(hand.replace("J", card)))
    return max(ranks)


for line in lines:
    line = line.replace("\n", "")
    hands_and_bids[line[:5]] = line[6:]
print(hands_and_bids)
hands = [h for h in hands_and_bids.keys()]


def compare(hand1, hand2):
    if getnewType(hand1) < getnewType(hand2):
        return -1
    if getnewType(hand1) > getnewType(hand2):
        return 1
    i = 0
    while hand1[i] == hand2[i]:
        i += 1
    return -1 if cards[hand1[i]] < cards[hand2[i]] else 1


orderedHands = (sorted(hands, key=functools.cmp_to_key(compare)))
for i in range(len(orderedHands)):
    print(orderedHands[i], getType(orderedHands[i]))
win = 0
for i in range(len(orderedHands)):
    win += int(hands_and_bids[orderedHands[i]]) * (i + 1)

print(win)
