import re

file = open("input.txt", "r")
lines = file.readlines()

hands = {}
cards = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1
}
types = {
    ".*([ATJQK2-9]).*\1.*": 2, #almeno un 2x o 3x o 4x o 5x
    ".*([ATJQK2-9]).*\1.*\1.*": 3, #3x o 4x o 5x
    ".*([ATJQK2-9]).*\1.*\1.*\1.*": 3, #4x o 5x
    "([ATJQK2-9])\1\1\1\1": 7  #5 of a kind

}
for line in lines[:-1]:
    line = line.replace("\n", "")
    line = line[:5] + "0" + line[5:]
    hands[line[:6]] = line[7:]
print(hands)


def compare(hand1, hand2):
    pass


orderedHands = []
