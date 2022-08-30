# 1
a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000) :
  for y in range(-999, 1000) :
    if (a * x) + (b * y) == (c) and (d * x) + (e * y) == f :
      print(x, y)
      break

# 2
# a, b, c, d, e, f = map(int, input().split())
# x = (c * e - b * f) // (a * e - b * d)
# y = (a * f - c * d) // (a * e - b * d)
# print(x, y)