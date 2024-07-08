#Brute force --
def subarray_sum(nums, k):
    count = 0

    for start in range(len(nums)):
        current_sum = 0
        for end in range(start, len(nums)):
            current_sum += nums[end]
            if current_sum == k:
                count += 1
        
    return count
    
nums = list(map(int,input("Enter the elements: ").split()))
k = int(input("Enter K: "))
result = subarray_sum(nums, k)
print(result)