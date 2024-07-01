#Problem to find max subarry sum in O(1) complexity --Kadanes algo is used
def maxSubArray(nums):
    sum = 0
    maxi = nums[0]

    for i in range(0, len(nums)):
        sum = sum + nums[i]
        maxi = max(maxi, sum)
        if sum < 0:
            sum = 0
    return maxi

nums = list(map(int,input().split()))
result = maxSubArray(nums)
print(result)