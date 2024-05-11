n, x = map(int, input().split())
iList = list(map(int, input().split()))

for i in iList:
    if i < x:
        print(i, end=" ")
