def persistence(n):
    count = 0
    while len(str(n)) != 1:
        digits = [int(i) for i in str(n)]
        prev = digits[0]
        for dig in digits[1:]:prev *= dig
        n = prev
        count += 1
    return count