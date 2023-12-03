import re

file = open("input.txt", "r")
engine = file.readlines()

pattern = re.compile("[^0-9.]")


def readNumber(i, j, engine_):
    i_ = i
    j_ = j
    num = ""
    char = str(engine_[i_][j_])
    while char.isnumeric():
        num += char
        j_ += 1
        char = str(engine_[i_][j_])
    return num


def checkValidPos(row, col, engine_):
    return 0 <= row < len(engine_) and 0 <= col < len(engine_[row]) - 1



import re

file = open("input.txt", "r")
engine = file.readlines()

pattern = re.compile("[^0-9.]")


def readNumber(i, j, engine_):
    i_ = i
    j_ = j
    num = ""
    while checkValidPos(i_, j_ - 1, engine_) and engine_[i_][j_ - 1].isnumeric():
        j_ -= 1
    char = str(engine_[i_][j_])
    while char.isnumeric():
        num += char
        j_ += 1
        char = str(engine_[i_][j_])
    return num


def checkValidPos(row, col, engine_):
    return 0 <= row < len(engine_) and 0 <= col < len(engine_[row]) - 1


def getRatioeEd(row, col, engine_):
    for i_ in range(row - 1, row + 2):
        for j_ in range(col - 1, col + 2):
            return 1
    return 0


sum_ = 0
i = 0
while i < len(engine):
    j = 0
    while j < len(engine[i]):
        if engine[i][j]=="*":
            sum_+=getRatioeEd(i,j,engine)
        j += 1
    i += 1

print(sum_)
