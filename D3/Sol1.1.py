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


def searchSymbol(row, startColumn, engine_):
    number_ = readNumber(row, startColumn, engine_)
    endColumn = startColumn + len(number_) - 1
    for i_ in range(row - 1, row + 2):
        for j_ in range(startColumn - 1, endColumn + 2):
            if checkValidPos(i_, j_, engine_) and pattern.match(str(engine_[i_][j_])):
                return True
    return False


sum_ = 0
i = 0
while i < len(engine):
    j = 0
    while j < len(engine[i]):
        if engine[i][j].isnumeric() and searchSymbol(i, j, engine):
            number = readNumber(i, j, engine)
            print(number)
            sum_ += int(number)
            j += len(number)
        else:
            j += 1
    i += 1

print(sum_)
