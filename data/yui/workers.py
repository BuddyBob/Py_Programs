
class lazyworker():
    def __init__(self,lazyworkers):
        self.lazyworkers = lazyworkers
    def __str__(self):
        lazyworkerCost = 10
        print(self.lazyworkers * lazyworkerCost)

class worker():
    def __init__(self,workers):
        self.workers = workers
    def __str__(self):
        workerCost = 10
        return str(self.workers * workerCost)
class hardworker():
    def __init__(self,hardworkers):
        self.håardworkers = hardworkers
    def __str__(self):
        hardworkerCost = 10
        return str(self.hardworkers * hardworkerCost)



    
    