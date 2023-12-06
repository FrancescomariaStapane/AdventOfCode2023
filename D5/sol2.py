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
def findPrevious(end, map_):
    for row in map_:
        destination_start = row[0]
        source_start = row[1]
        range_ = row[2]
        if destination_start <= end <= destination_start + range_:
            return source_start + end - destination_start
    return end


def findNext(start, map_):
    for row in map_:
        destination_start = row[0]
        source_start = row[1]
        range_ = row[2]
        if source_start <= start <= source_start + range_:
            return destination_start + start - source_start
    return start


def locationForSeed(seed):
    start = seed
    for map_ in maps:
        start = findNext(start, map_)
    return start


def seedFromLocation(location):
    previous = location
    for j in range(len(maps) - 1, -1, -1):
        previous = findPrevious(previous, maps[j])
    return previous


# parsing
line_index = 3
for map_ in maps:
    line_index = parseMap(lines, line_index, map_)

# casting strings to ints
for map_ in maps:
    for i in range(len(map_)):
        map_[i] = [int(j) for j in map_[i]]

for i in range(len(maps[-1]) - 1):
    posmin = i
    for j in range(i + 1, len(maps[-1])):
        if maps[-1][j][0] < maps[-1][posmin][0]:
            posmin = j
    if (posmin != i):
        tmp = maps[-1][i]
        maps[-1][i] = maps[-1][posmin]
        maps[-1][posmin] = tmp


def solve():
    inizio1=0
    inizio2=79874950
    inizio=inizio2
    location = inizio
    trovato = False
    for row in maps[-1]:
        print(row)
        i = inizio

        while i < row[0] + row[2]:
            if i > location:
                previous = location +1
                i -= 1
            else:
                previous = i
            location = previous
            if location == 79874950:
                pass
            # flag=False
            # if lastNumberVisited == 86:
            #     flag = True
            for j in range(len(maps) - 1, -1, -1):
                previous = findPrevious(previous, maps[j])

            # if flag:
            #     print(previous)
            for j in range(0, len(seeds), 2):
                if seeds[j] <= previous <= seeds[j] + seeds[j + 1]:
                    print(location)
                    trovato = True
                    break
            if trovato:
                break
            i += 1
        if trovato:
            break


solve()
# print(seedFromLocation(82))
# print(seedFromLocation(43))
# print(seedFromLocation(86))
print(seedFromLocation(79874952))
print(seedFromLocation(79874951))

# print(locationForSeed(79))
# print(locationForSeed(14))
# print(locationForSeed(55))
