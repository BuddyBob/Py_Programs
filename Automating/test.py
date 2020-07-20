lst = [] 

print(lst)
print('The queue is now empty...')

MaxQueue = int(input('\nSet The Maximum Queue to: '))

for i in range(0, MaxQueue): 
    print(lst)
    inn = input('Enter Name: ')
    lst.append(inn)  
print('')   
print(lst) 
print('The Queue is full..')   

def get_answer(prompt):
    while True:
        answer = input(prompt)
        if answer not in ('yes','no'):
            answer = input(prompt)        
        if answer in ('yes'):
            break         
        if answer in ('no'):
            exit()
    
print(get_answer('Do you want to start seriving? '))

for i in range(MaxQueue):
    print(lst)
    de = input('press (enter) to serve')
    print(lst.pop(0))