amount = int(input())
for c in range(1, amount+1):
    bedrag = int(input())
    transacties = input().split()[1:]
    for i in range(0, len(transacties)):
        transacties[i] = int(transacties[i])
    list.sort(transacties)

    for transactie in transacties:
        bedrag += transactie
        if bedrag < 0:
            bedrag -= 35

    print(str(c), str(bedrag))
	