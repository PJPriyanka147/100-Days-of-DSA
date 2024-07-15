#Brute Force --
def findMin(nums):
    min_element = nums[0]
    for num in nums:
        if num < min_element:
            min_element = num
    return min_element

nums = list(map(int, input("Enter array elements: ").split()))
result = findMin(nums)
print("Minimum Element:", result)

#Using Binary Search --
def findMin(nums):
    n = len(nums)
    low, high = 0, n-1

    while low < high:
        mid = (low + high )// 2

        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid 
        
    return nums[low]

nums = list(map(int, input("Enter array elements: ").split()))
result = findMin(nums)
print("Minimum Element:", result)
