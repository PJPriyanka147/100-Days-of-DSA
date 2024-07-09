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

#Using Hashmap(dictionary)
def subarray_sum(nums, k):
    freq_map = {0:1}
    current_sum = 0
    count_subarrays = 0

    for num in nums:
        current_sum += num
        #Check if there exists a cumulative sum which makes the current     sum equal to k
        if current_sum - k in freq_map:
            count_subarrays += freq_map[current_sum - k]
            
        #Update frequency map with current cumulative sum
        if current_sum in freq_map:
            freq_map[current_sum] += 1
        else:
            freq_map[current_sum] = 1

    return count_subarrays

nums = list(map(int,input("Enter the elements: ").split()))
k = int(input("Enter K: "))
result = subarray_sum(nums, k)
print(result)