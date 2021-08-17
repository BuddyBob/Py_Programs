import timeit
import matplotlib.pyplot as plt
import numpy as np
import random
def main(numList):
    #arbitrary index is O(n)
    # return numList.pop(random.choice(list(range(0,len(numList)))))
    #last index is O(1)
    return numList.pop(-1)
def timeThem(n):
    start = timeit.default_timer()
    main(n)
    stop = timeit.default_timer()
    return stop - start
y = [timeThem(list(range(1,i+1))) for i in range(1,50000)]
x = list(range(1,50000))
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Pop Time Complexity #O(1)')
plt.plot(x, y)
plt.show()