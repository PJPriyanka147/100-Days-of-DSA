#Using Brute force -- 
def max_subarray(nums):
    #Initialize to the smallest possible value to handle negative numbers
    max_sum = float('-inf')
    
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]

            if curr_sum > max_sum:
                max_sum = curr_sum
    
    return max_sum

nums = list(map(int,input("Enter the elements: ").split()))
result = max_subarray(nums)
print(result)

#Problem to find max subarry sum in O(n) complexity --Kadanes algo is used
def maxSubArray(nums):
    sum = 0
    maxi = nums[0]

    for i in range(0, len(nums)):
        sum = sum + nums[i]
        maxi = max(maxi, sum)
        if sum < 0:
            sum = 0
    return maxi

nums = list(map(int,input("Enter the elements: ").split()))
result = maxSubArray(nums)
print(result)