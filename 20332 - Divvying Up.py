input()
n = list(map(int, input().split()))

prize = sum(n)

if prize % 3 == 0:
    print("yes")
else:
    print("no")