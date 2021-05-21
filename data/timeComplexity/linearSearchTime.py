import timeit
import matplotlib.pyplot as plt
import numpy as np
def main(numList,number):
    return [count  for count,num in enumerate(numList) if num == number]
def timeThem(n):
    start = timeit.default_timer()
    main(list(range(1,n+1)),list(range(1,n+1))[-1])
    stop = timeit.default_timer()
    return stop - start
y = [timeThem(i) for i in range(1,10001)]
x = list(range(1,10001))
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Linear Search Time Complexity #O(n)')
plt.plot(x, y)
plt.show()