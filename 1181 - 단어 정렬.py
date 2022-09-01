N = int(input())
word = set()

for _ in range(N):
    word.add(input())

word = sorted(word)
for i in sorted(word, key=lambda x: (len(x))):
    print(i)
