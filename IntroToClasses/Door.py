class door:
    def __init__(self,name,color,locked,Open):
        self.name = name
        self.color = color
        self.locked = locked
        self.open = Open
    def info(self):
        if self.locked == True:
            locked = "Locked"
        else:
            locked = "Unlocked"
        if self.open == True:
            Open = "Open"
        else:
            Open = "Closed"
        if self.locked == True and self.open == True:
            return "Incorect info was given for "+str(self.name)
        
        else:
            return self.name+" is "+self.color+", "+str(locked)+" and "+str(Open)
door1 = door(name="door1",color="red",locked=True,Open=True)
print(door1.info())
