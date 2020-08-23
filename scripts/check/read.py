word_list2 = open('text.txt').read().split()
print('You have three tries to guess a word in the file')
count = 0
while count <= 3:
    a = (input(': '))
    if a in word_list2:
        print('good')
        again = (input('would you like to go again[y/n]: '))
        again = again.lower()
        if again == 'y':
            count == 0
            xxxinue
        else:
            count == 4
            break
    else:
        count += 1
        if count == 3:
            print('you loose')
            break
