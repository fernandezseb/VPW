amount = int(input())
for c in range(1, amount+1):
    lijn = input()
    kolommen = int(lijn.split(' ')[0])
    rijen = int(lijn.split(' ')[1])
    kaart = []
    for i in range(0, rijen):
        kaart.append(list(input()))

    dict = []
    for i in range(0, rijen):
        for j in range(0, kolommen-1):
            if kaart[i][j] != kaart[i][j+1]:
                letters = [kaart[i][j], kaart[i][j+1]]
                list.sort(letters)
                if (letters[0], letters[1]) not in dict:
                    dict.append((letters[0], letters[1]))

    old = kaart
    kaart = list(zip(*kaart))

    for i in range(0, kolommen):
        for j in range(0, rijen-1):
            if kaart[i][j] != kaart[i][j+1]:
                letters = [kaart[i][j], kaart[i][j+1]]
                list.sort(letters)
                if (letters[0], letters[1]) not in dict:
                    dict.append((letters[0], letters[1]))

    neighbours = {}
    for i in range(0, len(dict)):
        t_list = list(dict[i])
        if t_list[0] in neighbours:
            neighbours[t_list[0]] += 1
        else:
            neighbours[t_list[0]] = 1

        if t_list[1] in neighbours:
            neighbours[t_list[1]] += 1
        else:
            neighbours[t_list[1]] = 1

    for i in range(0, rijen):
        print(c, end="")
        for j in range(0, kolommen):
            if old[i][j] in neighbours.keys():
                print(' ', end="")
                print(str(neighbours[old[i][j]]), end="")
            else:
                print(" 0", end="")
        print('')