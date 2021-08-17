strs = ["dog","racecar","car"]
def find(prf):
    prefix = []
    tempPref = []
    count = 0
    while True:
        for words in prf:
            tempPref.append(words[count])
        if len(set(tempPref)) == 1:
            prefix.append(tempPref[0])
            tempPref.clear()
        else:
            return ''.join(prefix)
        count += 1

print(find(strs))