input()
A = set(input().split())
input()
check = list(input().split())

for i in check:
    print("1") if i in A else print("0")
