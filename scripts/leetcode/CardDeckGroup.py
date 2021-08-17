def getGroups(deck):
    dict = {}
    if len(deck) == 1:return False
    for nums in deck:
        if nums not in dict:dict[nums] = 1
        else:dict[nums] += 1
    deckX = [[numx]*dict[numx] for numx in dict]
    prevs = [len(deckX[0])]
    for ls in deckX[1:]:
        if len(ls) not in prevs:return False
        else:prevs.append(len(ls))
    return True
print(getGroups([1]))
