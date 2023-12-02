file = open("input.txt", "r")
lines = file.readlines()
sum_ = 0
dict_ = {
    "red": 0,
    "green": 1,
    "blue": 2
}
for line in lines:
    line = line[5:-1].split(":")[1]
    draws = line.split(";")
    rgb = [0, 0, 0]
    for draw in draws:
        cubes = draw.split(",")
        for cube in cubes:
            cubeInfo = cube[1:].split(" ")
            index=dict_.get(cubeInfo[1])
            if int(cubeInfo[0])>rgb[index]:
                rgb[index]=int(cubeInfo[0])
    sum_+=rgb[0]*rgb[1]*rgb[2]

print(sum_)
