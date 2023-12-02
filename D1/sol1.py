file = open("input.txt", "r")
lines = file.readlines()
sum_ = 0
for line in lines:
    first = -1
    last = -1

    for c in range(len(line)):
        if line[c].isnumeric():
            first = line[c]
            break
    for c in reversed(range(len(line))):
        if line[c].isnumeric():
            last = line[c]
            break
    sum_ += int(str(first) + str(last))
print(sum_)
