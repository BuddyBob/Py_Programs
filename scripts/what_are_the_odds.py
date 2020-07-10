from random import randint
# Here I am setting two list for each number generated
for i in range(2):
    two = []
    one = []
    #these list are for later when I find out how many two's and one's were generated in each session
    #For example, if there are 4 one's and 6 two's in a single session, I will append those stats to these list
    final1 = []
    final2 = []
    #this process will reapeat five times
    for i in range(5):
        one.clear()
        two.clear()
        # I need to to clear the list so they dont add up
        #Here we will choose a number either 1 or 2 ten times. If 1 chosen it will be appended to list one. 
        #If 2 is chosen it will be appended to list 2
        #There are 5 sessions of this.
        for i in range(1000):
            num = randint(1,2)
            if num == 1:
                one.append(num)
            else:
                two.append(num)
        print('----------------')
        #I need to find out how many one's are in the list and how many two's are in the list
        length_one = len(one)
        length_two = len(two)
        # I will append that two a list so that later I can figure out how many 2's and 1's were generated each session
        # also later I will be finding the average of them
        final1.append(length_one)
        final2.append(length_two)
    # here I am printing each rounds stats it looks a bit like this: 
    # there were seven 1's and three 2's generated in the first round etc.
    '''
    one: [7, 3, 4, 7, 6]
    two: [3, 7, 6, 3, 4] 
    '''
    print('one\'s : '+str(final1))
    print('two\'s : '+str(final2))
    # I must sort the numbers so that I am able to divide correctly when finding the average of 1's and 2's
    final1.sort()
    final2.sort()
    # the first step of finding average is adding all numbers up
    added_1 = sum(final1)
    added_2 = sum(final2)
    print('sum1: '+str(added_1))
    print('sum2: '+str(added_2))
    # I need to know how many 1's and 2's were generated

    #the last step of finding the average is dividing the sum by the amount of numbers there are in the data.
    average_one = added_1/len(final1)
    average_two = added_2/len(final2)
    print('average 1: '+str(average_one))
    print('average 2: '+str(average_two))
    #the average will look something like this: 
    '''
    average 1: 5.0
    average 2: 5.0
    '''