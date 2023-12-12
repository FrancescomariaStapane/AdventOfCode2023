file = open("input.txt", "r")
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

damagedMap=[]
numericalMap=[]

for line in lines:
    parts=line.split(" ")
    damagedMap.append(parts[0])
    numericalMap.append(parts[1].split(","))
print()