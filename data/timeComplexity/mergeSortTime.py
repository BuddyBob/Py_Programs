import timeit
import matplotlib.pyplot as plt
import numpy as np
def main(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        main(left)
        main(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              myList[k] = left[i]
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1
    return myList
def timeThem(n):
    start = timeit.default_timer()
    main(np.random.randint(1,10, size=n))
    stop = timeit.default_timer()
    return stop - start
y = [timeThem(i) for i in range(1,2000)]
x = list(range(1,2000))
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Merge Sort Time Complexity #O(n)')
plt.plot(x, y)
plt.show()