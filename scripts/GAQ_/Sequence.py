
def sequence(seq):
    def quadSEQUENCE(seq):
        print('quardratic')
        compare = []
        count = 0
        seq = [str(i)for i in seq]
        for i in seq:
            i.split(',')
        seq = [float(i)for i in seq]
        #FIND THE DIFFERENCE BETWEEN EACH NUMBER
        difference = [j-i for i, j in zip(seq[:-1], seq[1:])]
        difference2 = [j-i for i, j in zip(difference[:-1], difference[1:])]
        list2 = []
        list3 = []
        for i in range(1,len(seq)+1):
            list2.append(difference2[1]/2 * i ** 2)
            firstEq = str(difference2[1]/2)+'(n ^ 2)'
        for i in range(len(list2)):
            list3.append(seq[i]-list2[i])
        difference3 = [j-i for i, j in zip(list3[:-1], list3[1:])]
        previousNum = list3[0] - difference3[1]
        if previousNum > 0:
            previousNum = '+'+str(previousNum)
        secondEq = str(difference3[1])+'n - '+str(previousNum)
        return firstEq + ' + ' + secondEq




    def arethmaticSEQUENCE(seq):
        print('Arithmatic')
        compare = []
        count = 0
        seq = [str(i)for i in seq]
        for i in seq:
            i.split(',')
        seq = [float(i)for i in seq]
        #FIND THE DIFFERENCE BETWEEN EACH NUMBER
        difference = [j-i for i, j in zip(seq[:-1], seq[1:])]
        while True:
            for i in range(1,len(seq)+1):
                compare.append(i*difference[0])
            if compare[0] == seq[0]:
                return 'n'+str(difference[0])
                break
            difference = difference[0]
            for i in range(0,1000,1):
                i = i / 10.0
                total = 1*float(difference)+float(i)
                if total == seq[0]:
                    return 'n('+str(difference)+')'+'+'+str(i)
                    break
            for i in range(0, 1000, 1):
                i = i / 10.0
                total = 1*difference-i
                if total == seq[0]:
                    return 'n('+str(difference)+')'+'-'+str(i)
                    break

    def geometricSequence(seq):
        print('Geometric')
        multiply = None
        final =[]
        seq = [str(i)for i in seq]
        for i in seq:
            i.split(',')
        seq = [float(i)for i in seq]
        #FIND THE DIFFERENCE BETWEEN EACH NUMBER
        Base = seq[0]
        for i in range(1,900000,1):
            i = i/10
            if seq[0] * i == seq[1] and seq[1] * i == seq[2]:
                multiply = True
            if seq[0]/i == seq[1]and seq[1] / i == seq[2]:
                multiply = False
        if multiply == True:
            difference = seq[1]/seq[0]
            count = 0
            for ps in range(1,len(seq)+1):
                total = (difference ** count)
                final.append(Base*total)
                count+=1
            return 'Base * '+str(difference)+ ' ^ (n-1)'
            exitI()
        if multiply == False:
            difference = seq[1]/seq[0]
            count = 0
            for ps in range(1,len(seq)+1):
                total = (difference ** count)
                final.append(Base/total)
                count+=1
            return 'Base / '+str(difference)+ ' ^ (n-1)'
    
    
    
    seq = [str(i)for i in seq]
    for i in seq:
        i.split(',')
    seq = [float(i)for i in seq]
    #FIND THE DIFFERENCE BETWEEN EACH NUMBER
    difference = [j-i for i, j in zip(seq[:-1], seq[1:])]
    if all(x == difference[0] for x in difference) == True:
        print(arethmaticSEQUENCE(seq))
    geo = False
    multiply = None
    for i in range(1,900000):
        if seq[0] * i == seq[1] and seq[1] * i == seq[2] or seq[0]/i == seq[1]and seq[1] / i == seq[2]:
            multiply = True
            print(geometricSequence(seq))
    seq = [str(i)for i in seq]
    for i in seq:
        i.split(',')
    seq = [float(i)for i in seq]
    #FIND THE DIFFERENCE BETWEEN EACH NUMBER
    difference = [j-i for i, j in zip(seq[:-1], seq[1:])]
    difference2 = [j-i for i, j in zip(difference[:-1], difference[1:])]
    if all(x == difference2[0] for x in difference2) == True:
        print(quadSEQUENCE(seq))
