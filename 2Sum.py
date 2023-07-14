# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

nums = [2, 7, 11, 15]
target = 9
# two pointer approach
def twoSum(nums , target):
    nums = sorted(nums)
    left = 0
    right = len(nums)-1
    while (left<right):
        if(nums[left]+nums[right] == target):
            return True
        elif(nums[left]+nums[right] > target):
            right = right-1
        else:
            left = left-1
    return  False

print(twoSum(nums,target))