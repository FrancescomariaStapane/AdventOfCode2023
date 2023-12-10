import math

file = open("input.txt", "r")
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
matrix = []
for line in lines:
    chars = []
    for c in line:
        chars.append(c)
    matrix.append(chars)


def checkValidPos(row, col, matrix_):
    return 0 <= row < len(matrix_) and 0 <= col < len(matrix_[row])


# returns i, j of first accourence of the start char
def findStart(matrix_, startChar):
    for i in range(len(matrix_)):
        for j in range(len(matrix_[i])):
            if matrix_[i][j] == startChar:
                return i, j


def areConnected(pipe1, pipe2, matrix_):
    connectsFromNorth = {"|", "L", "J", "S"}
    connectsFromSouth = {"|", "F", "7", "S"}
    connectsFromWest = {"-", "J", "7", "S"}
    connectsFromEast = {"-", "L", "F", "S"}

    # posizioni illegali
    if not checkValidPos(pipe1[0], pipe1[1], matrix_) or not checkValidPos(pipe2[0], pipe2[1], matrix_):
        return False
    if matrix[pipe1[0]][pipe1[1]] == "." or matrix_[pipe2[0]][pipe2[1]] == ".":
        return False
    # sovrapposte
    if pipe1 == pipe2:
        return False
    # posizioni lontane
    if abs(pipe1[0] - pipe2[0]) > 1 or abs(pipe1[1] - pipe2[1]) > 1:
        return False

    # posizioni diagonali
    if not (pipe1[0] - pipe2[0] == 0 or pipe1[1] - pipe2[1] == 0):
        return False
    # vicino all'inizio
    # if matrix[pipe1[0]][pipe1[1]] == "S" or matrix[pipe2[0]][pipe2[1]] == "S":
    #     return True
    # pipe1 south, pipe2 north
    if pipe1[0] > pipe2[0] and matrix_[pipe1[0]][pipe1[1]] in connectsFromNorth and matrix[pipe2[0]][
        pipe2[1]] in connectsFromSouth:
        return True

    # pipe1 north, pipe2 south
    if pipe1[0] < pipe2[0] and matrix_[pipe1[0]][pipe1[1]] in connectsFromSouth and matrix[pipe2[0]][
        pipe2[1]] in connectsFromNorth:
        return True

    # pipe1 east, pipe2 west
    if pipe1[1] > pipe2[1] and matrix_[pipe1[0]][pipe1[1]] in connectsFromWest and matrix[pipe2[0]][
        pipe2[1]] in connectsFromEast:
        return True

    # pipe1 west, pipe2 east
    if pipe1[1] < pipe2[1] and matrix_[pipe1[0]][pipe1[1]] in connectsFromEast and matrix[pipe2[0]][
        pipe2[1]] in connectsFromWest:
        return True
    return False


def appendDirections(stack, pipe):
    for i_ in range(4):
        offset_col = round(math.cos(math.radians(90 * i_)))
        offset_row = -1 * round(math.sin(math.radians(90 * i_)))
        if areConnected(pipe, [pipe[0] + offset_row, pipe[1] + offset_col], matrix):
            stack.append([pipe[0] + offset_row, pipe[1] + offset_col])


def getNextCoordinate(pipe, matrix_):
    for i_ in range(4):
        offset_col = round(math.cos(math.radians(90 * i_)))
        offset_row = -1 * round(math.sin(math.radians(90 * i_)))
        if areConnected(pipe, [pipe[0] + offset_row, pipe[1] + offset_col], matrix_):
            return [pipe[0] + offset_row, pipe[1] + offset_col]
    return []


startCoordinates = [findStart(matrix, "S")[0], findStart(matrix, "S")[1]]

startPossibilities = []
appendDirections(startPossibilities, startCoordinates)

path=[]
for direction in startPossibilities:
    path = []
    depth = 0
    coordinates = startCoordinates
    copyMatrix = []
    for row in matrix:
        rowcopy = []
        for c in row:
            rowcopy.append(c)
        copyMatrix.append(rowcopy)
    while coordinates != startCoordinates or depth == 0:
        if depth == 2:
            copyMatrix[startCoordinates[0]][startCoordinates[1]] = "S"
        copyCoordinates = coordinates
        path.append(copyCoordinates)
        coordinates = getNextCoordinate(coordinates, copyMatrix)
        copyMatrix[copyCoordinates[0]][copyCoordinates[1]] = "."

        if not coordinates:
            break
        depth += 1

    if coordinates == startCoordinates:
        print(depth / 2)
# path.pop()


internals = []
previousPosition = [-1, -1]


def areComplementary(corner1, corner2):
    return (corner1 == "F" and corner2 == "L") or (corner1 == "7" and corner2 == "J") or (
            corner1 == "L" and corner2 == "F") or (corner1 == "J" and corner2 == "7")


def isCorner(corner):
    return corner in ["J", "F", "L", "7"]


path.append(path[0])
lastCorner = ""
counter=0
while path[0][1]==path[-1][1]:
    path.remove(path[0])
for position in path:
    if position == [1, 4]:
        print("stop")
    # if position[1] != previousPosition[1]:
    pipe = matrix[position[0]][position[1]]
    if areComplementary(pipe, lastCorner):
        for i in range(position[0], len(matrix)):
            subPosition = [i, position[1]]
            if subPosition in internals:
                internals.remove(subPosition)
            elif subPosition not in path:
                internals.append(subPosition)
    elif isCorner(pipe):
        lastCorner = pipe
    if previousPosition[1] != position[1]:
        for i in range(position[0], len(matrix)):
            subPosition = [i, position[1]]
            if subPosition in internals:
                internals.remove(subPosition)
            elif subPosition not in path:
                internals.append(subPosition)

    previousPosition = position
    counter+=1
    if counter%200==0:
        print(counter)
print(len(internals))
