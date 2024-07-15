#Brute Force --
def findMin(nums):
    mini_element = nums[0]
    for num in nums:
        if num < mini_element:
            mini_element = num

    return mini_element

nums = list(map(int, input("Enter array elements: ").split()))
result = findMin(nums)
print("Minimum Element:", result)

#Optimized Solution using Binary Search
def findMin(nums):
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        if nums[mid] > nums[high]:
            low = mid + 1
        elif nums[mid] < nums[high]:
            high = mid
        else: # nums[mid] == nums[high], can't decide, so decrement high by 1 to skip the duplicate and continue the search.
            high -= 1
    
    return nums[low]

nums = list(map(int, input("Enter array elements: ").split()))
result = findMin(nums)
print("Minimum Element:", result)