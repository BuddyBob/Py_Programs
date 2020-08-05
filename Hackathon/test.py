import  matplotlib.pyplot as plt
L = [['  150822', '  152055', '  153315', '  154448', '  154862', '  155402', '  156801'], [' 30183', ' 30198', ' 30225', ' 30225', ' 30225', ' 30224', ' 30252']]
for elements in L:
    for i in range(0, len(elements)): 
        elements[i] = int(elements[i]) 
days = len(L[0])
for lists in L:
    one = plt.plot(range(days),lists,label=L[0])
plt.legend()
plt.show()