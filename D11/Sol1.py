file = open("input.txt", "r")
lines = file.readlines()

space = []
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

for line in lines:
    chars = []
    for c in line:
        chars.append(c)
    space.append(chars)

i = 0
while i < len(space):
    if "#" not in space[i]:
        space.insert(i, space[i].copy())
        i += 1
    i += 1

i = 0
while i < len(space[0]):
    if not any(space[j][i] == "#" for j in range(len(space))):
        for j in range(len(space)):
            space[j].insert(i, ".")
        i += 1
    i += 1
xs = []
ys = []
for i in range(len(space)):
    for j in range(len(space[i])):
        if space[i][j] == "#":
            xs.append(i)
            ys.append(j)
xs.sort()
ys.sort()

sum_x=0
sum_y=0
# xs=[2,3,4,5]
# ys=[1,3,4,5]
for i in range(len(xs)):
    sum_x+=xs[i]*i
    sum_y+=ys[i]*i

for i in range(len(xs)-1):
    sum_x-= (i+1)*xs[len(xs)-(i+2)]
    sum_y-= (i+1)*ys[len(ys)-(i+2)]

print(sum_x+sum_y)