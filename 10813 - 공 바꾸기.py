n, m = map(int, input().split())
ballList = [ballN for ballN in range(n + 1)]
basket = 0

for _ in range(m):
    i, j = map(int, input().split())

    ballList[i], ballList[j] = ballList[j], ballList[i]

print(*ballList[1:])
