file = open("input.txt", "r")
lines = file.readlines()
winnings = []
cards = []
numberOfCards = [1 for i in range(len(lines))]
totCards = 0


for i in range(len(lines)):
    # input parsing and initialization
    lines[i] = lines[i].split(":")[1]
    winnings.append(lines[i].split("|")[0].split(" "))
    while "" in winnings[i]:
        winnings[i].remove("")
    cards.append(lines[i].split("|")[1].split(" "))
    cards[i][len(cards[i]) - 1] = cards[i][len(cards[i]) - 1][:-1]
    while "" in cards[i]:
        cards[i].remove("")

    #solve
    matches = 0
    for number in cards[i]:
        if number in winnings[i]:
            matches += 1
    for j in range(matches):
        numberOfCards[i + 1 + j] += numberOfCards[i]
    # print("" + str(i) + ": " + str(numberOfCards[i]))
    totCards += numberOfCards[i]
print(totCards)
