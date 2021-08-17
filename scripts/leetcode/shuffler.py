s = "aaiougrt"
indices = [4,0,2,6,7,3,1,5]
replace = list('*'*len(s))
for letters,index in zip(s,indices):replace[index] = letters
print(''.join(replace))