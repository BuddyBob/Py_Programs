x= [2, 4, 0, 100, 4, 11, 2602, 36]
odd = False
if len([numbers for numbers in [assume for assume in x[:3]] if numbers % 2 == 0]) < len([numbers for numbers in [assume for assume in x[:3]] if numbers % 2 != 0]):odd = True
if odd == True:print([evens for evens in x if evens % 2 == 0][0])
else:print([odds for odds in x if odds % 2 != 0][0])
