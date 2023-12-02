file = open("input.txt", "r")
lines = file.readlines()
sum_ = 0
dict_ = {
    "red": 12,
    "green": 13,
    "blue": 14
}
for line in lines:
    flag = False
    line = line[5:-1]
    game = int(line.split(":")[0])
    line = line.split(":")[1]
    draws = line.split(";")
    for draw in draws:
        if flag:
            break
        cubes = draw.split(",")
        for cube in cubes:
            if flag:
                break
            cubeInfo = cube[1:].split(" ")
            if int(cubeInfo[0]) > dict_.get(cubeInfo[1]):
                flag = True
                break
    if not flag:
        sum_ += game

print(sum_)
