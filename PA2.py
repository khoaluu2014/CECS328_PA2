from math import ceil, floor, inf


def maxSubArrayDivideAndConquer(nums: list[int]) -> int:
    p = 0
    r = len(nums)
    
    #0 element
    if p == r:
        return int(-inf)
    #base case 1 element
    if r == 1:
        return nums[0]
    #recursive case
    q = int((p+r)/2)
    #max sum on the left
    leftSum = maxSubArrayDivideAndConquer(nums[p:q])
    #max sum on the right
    rightSum = maxSubArrayDivideAndConquer(nums[q+1, r])
    #max sum in the middle
    midSum = maxSpan(nums, p, q, r)
    #max subarray
    return max(leftSum, rightSum, midSum)


def maxSpan(nums: list[int], p, q, r) -> int:
    #Find max sum to the left
    leftSum = -inf
    sum = 0
    for i in range(p, q, -1):
        sum = sum + nums[i]
        if sum >= leftSum:
            leftSum = sum
    #Find max sum to the right
    rightSum = -inf
    sum = 0
    for i in range(q+1, r, 1):
        sum = sum + nums[i]
        if sum >= rightSum:
            rightSum = sum
    maxSum = leftSum + rightSum
    return maxSum



def maxSubArrayKadane(nums: list[int]) -> int:
    pass

print(maxSubArrayDivideAndConquer([0,1,2,3,4]))
