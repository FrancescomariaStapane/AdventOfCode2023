import math

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
periods = {}
transitories = {}
for i in range(len(paths)):
    visited.append({})
    currentNode = paths[i] + instructions[0]

    counterInstructions = 0
    counterPeriods = 0
    while currentNode not in visited[i].keys():
        for j in range(len(instructions)):
            if currentNode in visited[i].keys():
                break
            visited[i][currentNode] = counterInstructions
            if nodes[currentNode[:-1]]["R"] == nodes[currentNode[:-1]]["L"]:
                visited[i][currentNode[:-1] + "R"] = counterInstructions
                visited[i][currentNode[:-1] + "L"] = counterInstructions

            currentNode = nodes[currentNode[:-1]][instructions[j]] + instructions[(j + 1) % len(instructions)]
            counterInstructions += 1
        counterPeriods += 1
    # print("path ", paths[i], ":")
    periodo = counterInstructions - visited[i][currentNode]
    transitorio = visited[i][currentNode]
    periods[paths[i]] = periodo
    transitories[paths[i]] = transitorio
    # print("periodo: ", periodo)
    # print("transotorio: ",)
print(periods)
print(transitories)

zetas=[]
for i in range(len(paths)):
    path=paths[i]
    for j in range(100000):
        if j >transitories[paths[i]]:
            if path[-1]=="Z":
                zetas.append(j)
                break
            # print(i," ",path)
        path=nodes[path][instructions[j % len(instructions)]]

lcm=zetas[0]

for zeta in zetas:
    lcm=math.lcm(lcm, zeta)
print(lcm)

# for i in range(20, 600, 47):
#     print(getNode("HMA", i))
#


# periodo=67
# currentNode="NPA"
# counter = 0
# j=4
# for i in range(1000):
#     for instruction in instructions:
#         currentNode = nodes[currentNode][instruction]
#         counter += 1
#         if counter % periodo ==j :
#             print(currentNode)
# for j in range(periodo):
#     stamp = ""
#     currentNode="NPA"
#     counter = 0
#     for i in range(1000):
#         for instruction in instructions:
#             currentNode = nodes[currentNode][instruction]
#             counter += 1
#             if counter % periodo ==j :
#                 if counter>0 and currentNode!= stamp:
#                     print(currentNode, " ",j)
#                 stamp = currentNode

# for i in range(18, 500, 47):
#     node = getNode("HMA", i)
#     print(node, " ", nodes[node]["L"], " ", nodes[node]["R"], " ", instructions[i % len(instructions)])
