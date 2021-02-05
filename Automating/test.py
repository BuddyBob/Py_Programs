my_dict = {
        "NaCl": 2.6,
        "NaHCO3": 2.5,
        "KCl": 1.5,
        "Sugar": 13.5,
    }
newValues = []
for key in my_dict:    
    newValues.append(my_dict[key] *  2)
print(newValues)