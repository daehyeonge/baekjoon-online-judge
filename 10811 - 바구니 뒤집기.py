n, m = map(int, input().split())
nList = [a for a in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())

    temp = nList[i - 1:j]
    temp.reverse()

    nList[i - 1:j] = temp

print(*nList)
