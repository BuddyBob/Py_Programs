import random
class Boss:
    def __init__(self,name,employees,networth,rating):
        self.employees = employees
        self.networth = networth
        self.rating = rating
        self.name = name
    def nameFunc(self):
        return self.name
    def networthFunc(self):
        return self.networth
    def employeesFunc(self):
        return self.employees
    def ratingFunc(self):
        return self.rating
    def allFunc(self):
        return  'Name: '+self.name+' | empCount: '+str(self.employees) +' | networth: '+str(self.networth)+' | rating: '+str(self.rating)
name = ['Bob','Richard','Ammy','Robert','Armstrong','Thavas','Jamie','Liam','Job','Thor']
for i in range(10):
    n = random.choice(name)
    name.remove(n)
    emp = random.randint(1,10000)
    net = random.randint(1e6,100e6)
    r = random.randint(1,5)
    r = str(r)+'/5'
    Person = Boss(n,emp,net,r)
    print('---------------------------------------------------------------')
    print('')
    print('')
    print('')
    if Person.nameFunc() == 'Thavas':
        print(Person.allFunc())


