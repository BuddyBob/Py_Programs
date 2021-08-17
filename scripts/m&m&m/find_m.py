import collections
def mmm(numbers):
        print(numbers)
        if type(numbers) != list:
            print('Must be list')
            exit()
        numbers.sort()
        final = sum(numbers) / len(numbers)
        print('mean: ',final)
        final = numbers[-1] - numbers[0]
        print('range: ',final)
        data = collections.Counter(numbers)
        data_list = dict(data)
        max_value = max(list(data.values()))
        mode_val = [num for num, freq in data_list.items() if freq == max_value]
        if len(mode_val) == len(numbers):
            print("No mode in the list")
        else:
            print('mode: ',mode_val)
        l =  len(numbers)
        if l % 2 == 0:
            index1 = l-l/2
            index2 = index1 - 1
            final1 = numbers[int(index1)]
            final2 = numbers[int(index2)]
            final = final1 + final2
            Medians = final/2
            print('median: ',Medians)
        else:
            final = (l + 1)/2
            final = int(final)
            Medians = numbers[final - 1]
            print('median: ',Medians) + 19 - 49.010

mmm([20,25,30,30,35,45,50])
        


