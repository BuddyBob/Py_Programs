import timeit
import matplotlib.pyplot as plt
exList = [1,2,3,4,5]
times = []
def sortIt(lst):
    return sort(lst)
for i in range(len(exList)):
    avg = [timeit.Timer(lambda: sortIt(exList)).timeit() for x in range(20)]        
    print(times)
    times.append(sum(avg)/len(avg))
plt.plot(list(range(len(exList))), times)  # Plot the chart
plt.show()  