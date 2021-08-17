from random import randint
Base = 20
OneWins = 0
ties = 0
TwoWins = 0
for i in range(10):

    one = []
    two =[]
    for i in range(Base):
        number = randint(1,2)
        if number == 1:
            one.append(number)
        else:
            two.append(number)
    print('One: '+str(len(one))+str('/')+str(Base))
    print('Two: '+str(len(two))+str('/')+str(Base))
    if len(one)>len(two):
        OneWins += 1
    if len(two)>len(one):
        TwoWins += 1
    if len(two) == len(one):
        ties += 1
    print('–––––––––––––––––––––––––––')

if OneWins > TwoWins:
    winner = 'One'
if TwoWins > OneWins:
    winner = 'Two'
if TwoWins == OneWins:
    winner = 'Tie'
print()

print('< Score Board ( '+winner+' ) >')
print('–––––––––––––––')
print('NAME  WINS  TIES  LOSSES')
print('One:  ',OneWins,'   ',ties,'    ',TwoWins)
print('Two:  ',TwoWins,'   ',ties,'    ',OneWins)