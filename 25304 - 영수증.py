totalCost = int(input())

for _ in range(int(input())):
    cost, count = map(int, input().split())

    totalCost -= cost * count

print("Yes" if totalCost == 0 else "No")
