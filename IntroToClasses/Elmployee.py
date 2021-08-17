class Employee:
    def __init__(self,name,salary,rating):
        self.name = name
        self.salary = salary
        self.rating = rating
    def DisplayStats(self):
        return self.name +': Workers Salary: %d'%self.salary+'\n'+self.name +': Workers Rate: %d'%self.rating
Sarah = Employee("Sarah",100000,9/9)
BoB = Employee("Bob",2,1/100)
print(Sarah.DisplayStats())
print('---------------------')
print(BoB.DisplayStats())
