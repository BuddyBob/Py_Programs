'''This is a interview problem solved by a 12 year old for AMAZON!
There is a target number and two lists. You need to go through every number in the first list and and add it to every number in the second
list. You need to check which sum is closest to the target number'''
import random
#function to check for closest number
def closest(another_random_list, target):
    return another_random_list[min(range(len(another_random_list)), key = lambda i: abs(another_random_list[i]-target))] 
#set target and three list. The first one is the first list of numbers the second is the second list of numbers.
#The last list is to check for the closest number to the target
target = 22
list1 = []
list2 = []
another_random_list = []
#choosing a random number for each element in the list(most homemade thing)
for i in range(0,10):
    n = random.randint(1,50)
    list1.append(n)
print(list1)
#choosing a random number for each element in the list2(most homemade thing)
for i in range(0,10):
    n = random.randint(1,50)
    list2.append(n)
print(list2)
'''This is the actual script. First I check for each number in the first list. Then I check for each number in the second list.
It looks at element 1 list one then multiplies by element 1 list 2. Then multiplies by element 2 list2 and so on. Once it reaches the end of
list 2 it looks a element 2 list one and repeats this process until there are no more numbers to be multiplied'''
for numbers in list1:
    for i in list2:
        sum1 = numbers+i
        print(sum1)
        another_random_list.append(sum1)
print('----------------')
print(another_random_list)
print('----------------')
print(closest(another_random_list, target))
check = (closest(another_random_list, target)) 
if check == target:
    print("RIGHT ON POINT")
#Here we try and check if a number has repeated or not
count = 0
for i in another_random_list:
    if (i == target):
        count+=1
if count >= 2:
    total = count - 1
    total = str(total)
    print("There are "+total+" more")