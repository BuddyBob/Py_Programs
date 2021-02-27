
import math
class circle:
    def __init__(self,radius=None,pi=3.14,circumference=None,area=None,diameter=None):
        self.radius = radius
        self.pi = pi
        try:
            self.diameter = radius*2
        except TypeError:
            self.diameter = diameter
        self.area = area
        self.circumference = circumference
    def __str__(self):
        return " radius - "+str(self.radius)+" \n diameter - "+str(self.diameter)+" \n circumference - "+str(self.circumference)+" \n area - "+str(self.area)+" \n pi - "+str(self.pi)
    def area(self):
        return 'area - '+str(self.pi*(self.radius**2))
    def circumference(self):
        return 'circumference - '+str(2*self.pi*self.radius)
    def diameter_radius_circumference(self):
        return 'radius - '+str(self.circumference/(self.pi*2))+'\ndiameter - '+str(self.circumference/self.pi)
    def diameter_radius_area(self):
        return 'radius - '+str(math.sqrt((self.area/self.pi))+'\ndiameter - '+str(math.sqrt(self.area/self.pi))*2)
        
circleObj = circle(circumference=6)
print(circleObj.diameter_radius_circumference())
