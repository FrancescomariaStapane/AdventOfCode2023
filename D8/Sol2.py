file = open("input.txt", "r")
lines = file.readlines()

instructions = lines[0][:-1]

nodes = {}


def getNode(startNode, offset):
    currentNode = startNode
    for i in range(offset):
        currentNode = nodes[currentNode][instructions[i % len(instructions)]]
    return currentNode


for i in range(2, len(lines)):
    nodes[lines[i][:3]] = {}
    nodes[lines[i][:3]]["L"] = lines[i][7:10]
    nodes[lines[i][:3]]["R"] = lines[i][12:15]

paths = []
for node in nodes.keys():
    if node[2] == "A":
        paths.append(node)

visited = []
for i in range(len(paths)):
    visited.append({})
    currentNode = paths[i]+instructions[0]

    counterInstructions = 0
    counterPeriods = 0

    while currentNode not in visited[i].keys():
        for j in range(len(instructions)):
            if currentNode in visited[i].keys():
                break
            visited[i][currentNode] = counterInstructions
            if nodes[currentNode[:-1]]["R"]==nodes[currentNode[:-1]]["L"]:
                visited[i][currentNode[:-1]+"R"] = counterInstructions
                visited[i][currentNode[:-1]+"L"] = counterInstructions

            currentNode = nodes[currentNode[:-1]][instructions[j]]+ instructions[(j + 1)%len(instructions)]
            counterInstructions += 1
        counterPeriods += 1
    print("path ", paths[i], ":")
    periodo = counterInstructions - visited[i][currentNode]
    print("periodo: ", periodo)
    print("transotorio: ", visited[i][currentNode])

# for i in range(13, 600, 67):
    # print(getNode("NPA", i))
