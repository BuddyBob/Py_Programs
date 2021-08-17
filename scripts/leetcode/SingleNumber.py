nums = [4,1,2,1,2]
def thing(nums):
    count = {numbers:nums.count(numbers) for numbers in set(nums)}
    print(count)
    for k,v in count.items():
        if v == 1:
            return k
print(thing(nums))