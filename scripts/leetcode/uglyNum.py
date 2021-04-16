import math
def primeFactors(n):
    primeNum = []
    if n < 0:
        return [14]
    while n % 2 == 0:
        primeNum.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            primeNum.append(i)
            n = n / i
    if n > 2:primeNum.append(n)
    return primeNum
def ugly(primes):
    for numbers in primes:
        if numbers not in [2,3,5]:
            return False
    return True
ugly = ugly(primeFactors(-10))
print(ugly)
