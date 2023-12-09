file = open("input.txt", "r")
lines = file.readlines()
sequences = []
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    sequence = lines[i].split(" ")
    int_sequence = []
    for elem in sequence:
        int_sequence.append(int(elem))
    sequences.append(int_sequence)

# print(sequences)
sum_1 = 0
sum_2 = 0

def findNext(sequence):
    if all(sequence[i] == sequence[i + 1] for i in range(len(sequence) - 1)):
        return sequence[0]
    differenceSequence = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
    return sequence[len(sequence) - 1] + findNext(differenceSequence)

# def findPrevious(sequence):
#     if all(sequence[i] == sequence[i + 1] for i in range(len(sequence) - 1)):
#         return sequence[0]
#     differenceSequence = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
#     return sequence[0] - findPrevious(differenceSequence)

for sequence in sequences:
    sum_1 += findNext(sequence)
    sum_2 += findNext([sequence[i] for i in range(len(sequence)-1,-1,-1)])
print(sum_1)
print(sum_2)
