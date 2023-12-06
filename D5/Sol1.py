file = open("input.txt", "r")
lines = file.readlines()
seeds = [int(i) for i in lines[0][7:-1].split(" ")]
locations = []

maps = [[], [], [], [], [], [], []]


# parses a single map and returns index of the next useful line
def parseMap(lines_, line_index, map):
    while len((lines_[line_index])) > 1:
        map.append(lines[line_index][:-1].split(" "))
        line_index += 1
    line_index += 2
    return line_index


# returns the destination of a map given the start and the map
def findNext(start, map_):
    for row in map_:
        destination_start = row[0]
        source_start = row[1]
        range_ = row[2]
        if source_start <= start <= source_start + range_:
            return destination_start + start - source_start
    return start


# parsing
line_index = 3
for map_ in maps:
    line_index = parseMap(lines, line_index, map_)

# casting strings to ints
for map_ in maps:
    for i in range(len(map_)):
        map_[i] = [int(j) for j in map_[i]]

# solve
for seed in seeds:
    start = seed
    for map_ in maps:
        start = findNext(start, map_)
    locations.append(start)
print(min(locations))
