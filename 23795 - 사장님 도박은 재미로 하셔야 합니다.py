total = 0

while True:
    cash = int(input())

    if cash == -1:
        break
    else:
        total += cash

print(total)
