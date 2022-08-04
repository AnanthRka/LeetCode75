def runningSum(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        if i>0:
            nums[i] += nums[i-1]
    return nums

print(runningSum([1,2,3,4,5]))  