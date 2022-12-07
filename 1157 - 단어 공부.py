word = input().upper()
word_dict = {}

for i in word:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1

word_sort = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

if len(word_sort) != 1 and word_sort[0][1] == word_sort[1][1]:
    print("?")
else:
    print(word_sort[0][0])
