def solution(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


M = int(input())
N = int(input())
total_n = 0
listOfPrimeN = []

for i in range(M, N + 1):
    if solution(i):
        total_n += i
        listOfPrimeN.append(i)

if len(listOfPrimeN) == 0:
    print("-1")
else:
    print(total_n)
    print(min(listOfPrimeN))
