pattern = "abba"
words = "dog cat cat dog"
def is_pattern(pattern,words):
    words = words.split(' ')
    def createLetters(words):
        letts,letterCount,count = {},['a','b','c','d','e','f'],0
        for word in words:
            if word not in letts:
                letts[word] = letterCount[count]
                count += 1
        return letts
    seq = createLetters(words)
    sequence = [seq[word] for word in words]
    print(sequence)
    if ''.join(sequence) == pattern:
        return True
    else:
        return False
print(is_pattern(pattern, words))

