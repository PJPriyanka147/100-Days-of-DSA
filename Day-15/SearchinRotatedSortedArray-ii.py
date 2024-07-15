#Brute force --
def search(nums, target):
    for num in nums:
        if num == target:
            return True
    return False

nums = list(map(int,input("Enter the elements: ").split()))
target = int(input("Enter target: "))
result = search(nums, target)
print(result)

#Optimized using Binary Search --
def search(nums, target):
    low, high = 0, len(nums) - 1

    while low <  high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return True
        
        #If we encounter duplicates, just move the pointers
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1

        elif nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False

nums = list(map(int,input("Enter the elements: ").split()))
target = int(input("Enter target: "))
result = search(nums, target)
print(result)