pattern = "abba"
words = "dog cat cat dog"
def is_pattern(pattern,words):
    words = words.split(' ')
    def createLetters(words):
        letts = {}
        letterCount = ['a','b']
        count = 0
        for word in words:
            if word not in letts:
                letts[words] = letterCount[count]
                count += 1
        return letts
    print(createLetters(words))

is_pattern(pattern, words)