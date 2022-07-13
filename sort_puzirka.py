nums = [2,3,1, 7, 8, 10, 11, 45, 48]

print(nums)

for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        print(j)
        if nums[j]>nums[j+1]:
           nums[j], nums[j+1] = nums[j+1],nums[j]
print(nums)
