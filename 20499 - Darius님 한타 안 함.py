kda = list(input().split("/"))

if kda[1] == '0' or int(kda[0]) + int(kda[2]) < int(kda[1]):
    print("hasu")
else:
    print("gosu")
