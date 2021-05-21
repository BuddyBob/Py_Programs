import timeit
import matplotlib.pyplot as plt
import numpy as np
def main(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:array[i+1],array[i] = array[i],array[i+1]
    if(all(array[i] <= array[i + 1] for i in range(len(array)-1))):return array
    else:return main(array)
def timeThem(n):
    start = timeit.default_timer()
    print(n)
    main(np.random.randint(1,10, size=n))
    stop = timeit.default_timer()
    return stop - start
y = [timeThem(i) for i in range(1,1001)]
x = list(range(1,1001))
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Bubble Sort Time Complexity #O(n^2)')
plt.plot(x, y)
plt.show()