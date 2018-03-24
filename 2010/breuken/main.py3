total = int(input())
for i in range(1,total+1):
    teller,noemer = input().split(' ')
    tellerdict = {}
    noemerdict = {}
    for l in range(ord('a'),ord('z')+1):
        noemerdict[chr(l)] = 0
        tellerdict[chr(l)] = 0
    for r in range(len(noemer)):
        noemerdict[noemer[r]] = noemerdict[noemer[r]] + 1
    for r in range(len(teller)):
        tellerdict[teller[r]] = tellerdict[teller[r]] + 1

    tout = ""
    nout = ""
    for l in range(ord('a'),ord('z')+1):
        if tellerdict[chr(l)] > noemerdict[chr(l)]:
            tellerdict[chr(l)] = tellerdict[chr(l)] - noemerdict[chr(l)]
            noemerdict[chr(l)] = 0
        if tellerdict[chr(l)] < noemerdict[chr(l)]:
            noemerdict[chr(l)] = noemerdict[chr(l)] - tellerdict[chr(l)]
            tellerdict[chr(l)] = 0
        if tellerdict[chr(l)] == noemerdict[chr(l)]:
            tellerdict[chr(l)] = 0
            noemerdict[chr(l)] = 0
        tout = tout + tellerdict[chr(l)] * chr(l)
        nout = nout + noemerdict[chr(l)] * chr(l)
    

    if (tout == ""):
        tout = "1"
    if (nout == ""):
        nout = "1"

    print(tout + " " + nout)
