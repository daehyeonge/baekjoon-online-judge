input()
n_list = list(input().split())
input()
check = list(input().split())
n_dict = {}

for i in n_list:
    if i in n_dict:
        n_dict[i] += 1
    else:
        n_dict[i] = 1

for i in check:
    if i in n_dict:
        print(n_dict.get(i), end=" ")
    else:
        print("0", end=" ")
