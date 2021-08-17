nums = [1,2]
def find(nums):
    correctNums = []
    n = len(nums)
    for i in range(len(nums)):
        if nums.count(nums[0])>n/3:
            correctNums.append(nums[0])
            nums = list(filter(lambda a: a != nums[0], nums))
    return correctNums
print(find(nums))
    