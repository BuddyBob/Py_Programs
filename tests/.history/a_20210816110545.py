my_list = [('a',1), ('b',2), ('b',3), ('a',5), ('c',20), ('a',15), ('c',40)]
new_dict = {}
for tup in my_list:
    if tup[0] in list(new_dict.keys()):
        new_dict[tup[0]] = tup[1]
    else:
        new_dict[tup[0]] += tup[1]
        
print(new_dict)