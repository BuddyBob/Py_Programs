

def search(haystack,needle):
    for i in range(len(haystack)): 
        if haystack[i:i+len(needle)] == needle: return i
print(search('hello','ll'))
