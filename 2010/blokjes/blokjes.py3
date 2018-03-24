total = int(input())
for i in range(1,total+1):
    n = int(input())
    sum = 0
    for c in range(1,n+1):
        sum = sum + c**3
    print(str(sum))
