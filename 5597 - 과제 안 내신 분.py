nList = [1] + [0] * 30

for _ in range(28):
    n = int(input())
    nList[n] = 1

firstN = nList.index(0)

print(firstN)
print(nList[firstN + 1:].index(0) + firstN + 1)
