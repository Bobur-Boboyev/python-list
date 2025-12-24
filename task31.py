nums = [3, 5, 3, 2, 5, 5, 1]
most_frequent = nums[0]

for n in nums:
    if nums.count(n) > nums.count(most_frequent):
        most_frequent = n

print(most_frequent)