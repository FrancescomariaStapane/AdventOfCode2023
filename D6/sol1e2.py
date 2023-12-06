import math
import re

file = open("input.txt", "r")
lines = file.readlines()
linescp = []
for i in range(2):
    lines[i] = lines[i].split(":")[1]
    lines[i] = re.sub(" +", " ", lines[i])[1:-1]
    linescp.append(lines[i].split(" "))
    # print(linescp[i])
races = []
product = 1


def getSol(time, distance):
    sol1 = (time + math.sqrt(time ** 2 - 4 * distance)) / 2 - 0.0001
    sol2 = (time - math.sqrt(time ** 2 - 4 * distance)) / 2 + 0.0001
    sol1 = math.floor(sol1)
    sol2 = math.ceil(sol2)
    return sol1 - sol2 + 1


for i in range(len(linescp[0])):
    races.append([linescp[0][i], linescp[1][i]])
    time = float(linescp[0][i])
    distance = float(linescp[1][i])
    product *= (getSol(time, distance))
print("part 1: ", product)

newTime=float(re.sub(" ","",lines[0]))
newDistance=float(re.sub(" ","",lines[1]))
print("part 2: ",getSol(newTime,newDistance))