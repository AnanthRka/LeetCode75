def pivotIndex(nums: list[int]) -> int:
    p = 0
    
    while p < len(nums):
        if sum(nums[:p]) == sum(nums[p+1:]):
            return p
        p +=1
    return -1

print(pivotIndex([-1,1,1]))