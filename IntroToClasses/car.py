class CarClass:
    def __init__(self,carName,Speed):
        self.car_name = carName
        self.speed = Speed
cars= []
Car1 = CarClass('Mustang','300mph')
print(Car1.car_name)
print(Car1.speed)