import collections
numbers = []
file = open('m&m&m.txt', 'r')
def openFile():
    for line in file:
        split = line.split(',')
        for i in split:
            if i.isdigit():
                numbers.append(int(i))
    numbers.sort()

def mean1():
    final = sum(numbers) / len(numbers)
    print('mean: ',final)
def range1():
    final = numbers[-1] - numbers[0]
    print('range: ',final)
def mode1():
    data = collections.Counter(numbers)
    data_list = dict(data)
    max_value = max(list(data.values()))
    mode_val = [num for num, freq in data_list.items() if freq == max_value]
    print(mode_val)
    if len(mode_val) == len(numbers):
        print("No mode in the list")
    else:
        print('mode: ',mode_val)
def median1():
    l =  len(numbers)
    if l % 2 == 0:
        index1 = l-l/2
        index2 = index1 - 1
        final1 = numbers[int(index1)]
        final2 = numbers[int(index2)]
        final = final1 + final2
        Median = final/2
        print('median: ',Median)
    else:
        final = (l + 1)/2
        final = int(final)
        print('median: ',numbers[final - 1])

        


openFile()
mean1()
range1()
mode1()
median1()



