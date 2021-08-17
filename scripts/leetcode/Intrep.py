num = 8
def div(num):
    if num % 2 != 0:
        num += 1
    count = 0
    while num != 1:
        count += 1
        num /= 2
        
    return count
print(div(num))