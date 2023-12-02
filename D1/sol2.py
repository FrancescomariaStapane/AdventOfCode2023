file = open("input.txt", "r")
lines = file.readlines()
sum_ = 0
dict_ = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
for line in lines:
    first = -1
    last = -1

    for c in range(len(line)):
        if line[c].isnumeric():
            first = int(line[c])
            break
        for number in dict_.keys():
            if line[c:].startswith(number):
                first = dict_.get(number)
                break
        if first > 0:
            break
    for c in reversed(range(len(line))):
        if line[c].isnumeric():
            last = int(line[c])
            break
        for number in dict_.keys():
            if line[:c].endswith(number):
                last = dict_.get(number)
                break
        if last > 0:
            break

    sum_ += int(str(first) + str(last))
print(sum_)
