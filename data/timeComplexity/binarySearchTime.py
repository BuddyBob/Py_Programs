import timeit
import matplotlib.pyplot as plt
import numpy as np
def main(numList,number):
    numList.sort()
    minimum = 0
    maximum = len(numList)
    middle = (minimum+maximum)//2
    while numList[middle] != number:
        middle = (minimum+maximum)//2
        if number < numList[middle]:maximum = middle
        elif number > numList[middle]:minimum = middle
    return middle
def timeThem(n):
    start = timeit.default_timer()
    main(list(range(1,n+1)),list(range(1,n+1))[-1])
    stop = timeit.default_timer()
    return stop - start
y = [timeThem(i) for i in range(1,10001)]
x = list(range(1,10001))
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Binary Search Time Complexity #O(n)')
plt.plot(x, y)
plt.show()