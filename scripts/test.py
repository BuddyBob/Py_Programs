word_list = []
word_list2 = open('text.txt').read().split()
for item in word_list2:
    if item in word_list:
        continue
    else:
        word_list.append(item)
word_list.sort()
print(word_list)