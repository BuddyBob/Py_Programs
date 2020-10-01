class pic:
    def __init__(self,level):
        self.level = level
    def copper_pic(self):
        levels = ['level1','level2','level3','level4','level5']
        currentIndex = levels.index(self.level)
        try:
            self.level = levels[currentIndex+1]
        except IndexError:
            return level5
        return self.level
    def silver_pic(self):
        levels = ['level1','level2','level3','level4','level5']
        currentIndex = levels.index(self.level)
        try:
            self.level = levels[currentIndex+1]
        except IndexError:
            return level5
        return self.level
    def gold_pic(self):
        levels = ['level1','level2','level3','level4','level5']
        currentIndex = levels.index(self.level)
        try:
            self.level = levels[currentIndex+1]
        except IndexError:
            return level5
        return self.level
# yui = pic('level2')
# print(yui.silver_pic())
