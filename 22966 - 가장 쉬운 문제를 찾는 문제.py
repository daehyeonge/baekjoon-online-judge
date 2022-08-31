n = int(input())
problem_list = []

for i in range(n):
    problem = list(map(str, input().split()))
    problem_list.append((problem[0], int(problem[1])))

print(sorted(problem_list, key=lambda x: x[1])[0][0])
