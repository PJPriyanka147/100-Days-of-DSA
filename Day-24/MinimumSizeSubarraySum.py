#brute force --
def minSubarrayLen(nums, target):
    n = len(nums)
    min_length = float('inf')
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum >= target:
                min_length = min(min_length, j - i + 1)
                break
    return min_length if min_length != float('inf') else 0         

nums = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target: "))
result = minSubarrayLen(nums, target)
print(result)