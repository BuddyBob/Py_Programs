seq = 1,3,6,10
difference = [j-i for i, j in zip(seq[:-1], seq[1:])]
difference2 = [j-i for i, j in zip(difference[:-1], difference[1:])]
print(difference)
print(difference2)
half = 1/2 * difference[1]
for i in range(0,len(seq)):
    print(seq[i] ** 2 * half)