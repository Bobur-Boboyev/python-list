nums = []
pairs = []

for i in range(6):
    num = int(input("num: "))
    nums.append(num)

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 10:
            pairs.append((nums[i], nums[j]))

print(pairs)