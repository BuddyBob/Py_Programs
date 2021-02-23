nums = list(range(1,9000))
for numbers in nums:
    if nums.count(numbers) > 1:
        nums = list(filter(lambda x: x != numbers, x))
print(nums)
 