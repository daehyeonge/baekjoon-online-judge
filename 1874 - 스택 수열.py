stack = []
answer = []
check = True
tmp = 1

for _ in range(int(input())):
    n = int(input())

    while tmp <= n:
        stack.append(tmp)
        answer.append("+")
        tmp += 1

    if stack[-1] == n:
        answer.append("-")
        stack.pop()
    else:
        print("NO")
        check = False
        break

if check:
    for i in answer:
        print(i)