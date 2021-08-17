import timeit
import matplotlib.pyplot as plt
exList = [1,2,3,4,5]
times = []
def indexIt(lst,ind):
    return lst[ind]
for i in range(len(exList)):
    avg = [timeit.Timer(lambda: indexIt(exList,i)).timeit() for x in range(20)]        
    times.append(sum(avg)/len(avg))
plt.plot(list(range(len(exList))), times)  # Plot the chart
plt.show()  