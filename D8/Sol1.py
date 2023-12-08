file = open("input.txt", "r")
lines = file.readlines()

instructions = lines[0][:-1]

nodes = {}

for i in range(2, len(lines)):
    nodes[lines[i][:3]] = {}
    nodes[lines[i][:3]]["L"] = lines[i][7:10]
    nodes[lines[i][:3]]["R"] = lines[i][12:15]
print(nodes)

currentNode = "AAA"
counter = 0
while True:
    for instruction in instructions:
        currentNode = nodes[currentNode][instruction]
        counter += 1
    if currentNode == "ZZZ":
        break
print("part 1:", counter)

