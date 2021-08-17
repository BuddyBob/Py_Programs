x = [2, 8, 5, 4, 7]
def check(x):
    changes = 0
    for count,num in enumerate(x[1:-1]):
        if x[count+1] > x[count] and x[count+1] > x[count+2]:
            x[count+1]-= 1
            changes += 1
        elif x[count+1] < x[count] and x[count+1] < x[count+2]:
            x[count+1] += 1
            changes += 1
    if changes >= 1:return check(x)
    else:return x

print(check(x))