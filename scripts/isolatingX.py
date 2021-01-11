def makePoly(arr):
    def fn(x):
        return sum(c*x**p for p,c in enumerate(arr))
    return fn

my_func = makePoly([8, 2])
print(my_func(3))