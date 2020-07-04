
def fact(number):
    count = number
    total = None
    down_count = count-1
    num = 0
    while down_count >= 1:
        while num == 0:
            total = count * down_count
            down_count -= 1
            count = total
            if number <= 2:
                break
            num+=1
        if number <= 2:
            break
        total = total * down_count
        down_count -= 1
    return total
total = 0
number = int(input(': '))
final = fact(number)
print(final)
#42 * 5
#210
#210 * 4