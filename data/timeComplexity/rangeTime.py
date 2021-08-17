import timeit
import matplotlib.pyplot as plt
import numpy as np
def main(num):
    return range(1,num)
def timeThem(n):
    start = timeit.default_timer()
    main(n)
    stop = timeit.default_timer()
    return stop - start
y = [timeThem(i) for i in range(1,50000)]
x = list(range(1,50000))
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Range Time Complexity #O(1)')
plt.plot(x, y)
plt.show()