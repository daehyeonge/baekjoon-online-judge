card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for _ in range(10):
    n, m = map(int, input().split())
    n -= 1
    t = 0

    reverse_card = list(reversed(card[n:m]))

    for i in range(n, m):
        card.pop(i)
        card.insert(i, reverse_card[t])
        t += 1

for i in card:
    print(i, end=" ")
