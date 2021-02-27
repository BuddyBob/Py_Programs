s = "leetcode"
words = ["leet", "code"]
def wordSplit(s,words):
	TakenWord = []
	wordCountL = []
	countWords = 0
	for word in words:
		wordCountL.append(len(word))
		wordCountL = [sum(wordCountL)]
		TakenWord.append(s[countWords:wordCountL[0]])
		countWords += len(word)
	if TakenWord == words:
		return True
	else:
		return False
print(wordSplit(s,words))