import re

file = open("input.txt", "r")
engine = file.readlines()

pattern = re.compile("[^0-9.]")


# returns string containing the number that starts in position i,j

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


def checkMatch(i, j, engine_):
    return pattern.match(str(engine_[i][j]))


def searchSymbol(row, startColumn, engine_):
    number = readNumber(row, startColumn, engine_)
    endColumn = startColumn + len(number) - 1
    leftBorder = startColumn == 0
    rightBorder = endColumn == len(engine_[0]) - 2
    upperBorder = row == 0
    lowerBorder = row == len(engine_) - 1

    # checking the 3 positions on the left  and right of  the number (lateral + diagonal)
    if (not leftBorder and (checkMatch(row, startColumn - 1, engine_) or (
            not upperBorder and checkMatch(row - 1, startColumn - 1, engine_)) or (
                                    not lowerBorder and checkMatch(row + 1, startColumn - 1, engine_)))) \
            or \
            (not rightBorder and (pattern.match(str(engine_[row][endColumn + 1]))) or (
                    not upperBorder and checkMatch(row - 1, endColumn + 1, engine_)) or (
                     not lowerBorder and checkMatch(row + 1, endColumn + 1, engine_))):
        print("laterale")
        return True
    # checking positions above and below the number
    for j in range(startColumn, endColumn + 1):
        if (not upperBorder and pattern.match(str(engine_[row - 1][j]))) or (
                not lowerBorder and pattern.match(str(engine_[row + 1][j]))):
            print("sopra o sotto")
            return True
    return False
    # print(leftBorder, rightBorder, upperBorder, lowerBorder)


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
