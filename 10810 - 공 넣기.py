n, m = map(int, input().split())
nList = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())

    for ballN in range(i - 1, j):
        nList[ballN] = k

print(*nList)
