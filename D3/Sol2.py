import re
import math

file = open("input.txt", "r")
engine = file.readlines()

pattern = re.compile("[^0-9.]")


def checkValidPos(row, col, engine_):
    return 0 <= row < len(engine_) and 0 <= col < len(engine_[row]) - 1


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


def getRatioEd(row, col, engine_):
    parts = []
    up = False
    down = False
    # cross
    for i_ in range(4):
        offset_col=round(math.cos(math.radians(90*i_)))
        offset_row=-1*round(math.sin(math.radians(90*i_)))
        row_ =row + offset_row
        col_ =col + offset_col
        if checkValidPos(row_, col_,engine_) and engine_[row_][col_].isnumeric():
            if i_ == 1:
                up = True
            elif i_ == 3:
                down = True
            parts.append(int(readNumber(row_, col_, engine_)))
    # diagonals
    for i_ in range(2):
        offset_row = (-1 + 2 * i_)
        for j_ in range(2):
            offset_col = (-1 + 2 * j_)
            row_ =row+ offset_row
            col_ =col +offset_col
            if checkValidPos(row_, col,engine_) and engine_[row_][col_].isnumeric() and ((not up and i_ == 0) or (not down and i_ == 1)):
                parts.append(int(readNumber(row_, col_, engine_)))
    if len(parts) == 2:
        return parts[0] * parts[1]
    else:
        return 0


sum_ = 0
i = 0
while i < len(engine):
    j = 0
    while j < len(engine[i]):
        if engine[i][j] == "*":
            sum_ += getRatioEd(i, j, engine)
        j += 1
    i += 1

print(sum_)
