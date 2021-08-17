import numpy as np
import itertools
import random
import matplotlib.pyplot as plt
class calculate:
    def __init__(self,dataset,outliers=False):self.dataset,self.outliers = dataset,outliers
    def __str__(self):
        self.dataset.sort()
        earlyDataSet = self.dataset
        def outliers(self,dataset):
            q1,q2 = np.percentile(self.dataset, 25, interpolation = 'midpoint'),np.percentile(self.dataset, 75, interpolation = 'midpoint')
            highOuts,lowOuts,IQR = [],[],q2-q1
            for numbersData in self.dataset:
                if numbersData > q2 + 1.5*IQR:highOuts.append(numbersData)
                if numbersData < q1 - 1.5*IQR:lowOuts.append(numbersData)
            print(f"outliers: {highOuts+lowOuts}")
            return highOuts+lowOuts
        if self.outliers == True:
            outliersNums = outliers(self,self.dataset)
            ot = outliersNums
            [self.dataset.remove(outliersNums) for outliersNums in ot if outliersNums != None]
        else:print(outliers(self,self.dataset))
        def mean(self,dataset):return str(sum(self.dataset)/len(self.dataset))  
        def median(self,dataset):
            if len(self.dataset) % 2 == 0:return str((len(self.dataset)/2+(len(self.dataset)/2)+1)/2)
            else:return str(self.dataset[int(len(self.dataset)/2)])
        def mode(self,dataset):
            counts = {}
            for i in range(len(self.dataset)):
                currentnumber,count = self.dataset[i],0
                for l in self.dataset:
                    if l == currentnumber:count += 1
                counts[currentnumber] = count 
            return [key for m in [max(counts.values())] for key,val in counts.items() if val == m]      
        def rangex(self,dataset):return str(self.dataset[-1]-self.dataset[0])
        def mad(self,dataset):
            diffs,mad_base_mean = [],mean(self,dataset)
            for i in range(len(self.dataset)):diffs.append(abs(self.dataset[i]-float(mad_base_mean)))
            return str(sum(diffs)/len(diffs))
        fig = plt.figure(figsize =(10, 7))
        plt.boxplot(self.dataset)
        # plt.show(block=True)
        return "mean: "+str(mean(self,self.dataset)+"\nmedian: "+str(median(self,self.dataset))+"\nrange: "+str(rangex(self,self.dataset))+"\nmode: "+str(mode(self,self.dataset))+"\nmad: "+str(mad(self,self.dataset)))
#set outlier to True if you would not like it
#set outlier to False if you would like to include it in the dataset

while True:
    DataSet = input('Enter: ')
    DataSet = DataSet.split(' ')
    DataSet = list(map(float, DataSet))
    print(DataSet)
    print(calculate(DataSet, False))




