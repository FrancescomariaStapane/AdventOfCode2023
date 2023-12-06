
import re
file = open("input.txt", "r")
lines = file.readlines()
linescp=[]
for i in range(2):
    lines[i]=lines[i].split(":")[1]
    lines[i]=re.sub(" +"," ",lines[i])[1:-1]
    linescp.append(lines[i].split(" "))
    # print(linescp[i])
races=[]
for i in range(len(linescp[0])):
    races.append([linescp[0][i],linescp[1][i]])
    print(races[i])