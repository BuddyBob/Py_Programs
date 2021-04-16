def is_isogram(string):
    Sames = {}
    string = string.lower()
    for letter in string:
        if letter not in Sames:
            Sames[letter] = 1
        else:
            Sames[letter] += 1
    repeats = Sames.values()
    for x in repeats:
        if x >= 2:
            return False
    return True
print(is_isogram('moOse'))