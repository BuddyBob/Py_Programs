x = [[['car','jeep','bus'],['cat','dog','rat']]
     ,[['apple','orange','banana'],['London','New York','Paris']]
     ]
def traverse(a):
    elements = [a if not isinstance(a, list) for e in a]
    if not isinstance(a, list):yield a
    else:
        for e in a:yield from traverse(e)
strings = [e for e in traverse(x)]
aWords = [string for string in [e for e in traverse(x)] if 'a' in string]
print(aWords)