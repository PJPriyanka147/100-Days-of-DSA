#Brute force --
def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    
    return -1

nums = list(map(int,input("Enter the elements: ").split()))
target = int(input("Enter target: "))
result = search(nums, target)
print(result)

#Optimized Using binary Search --
def search(nums, target):
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        
        #Determine if the mid element is in the rotated or sorted part
        if nums[mid] >= nums[low]:
            # If target is between the first element and mid, go left
            if nums[low] <= target <= nums[mid]:
                high = mid
            # Else, go right
            else:
                low = mid + 1

        else:
            # If target is between mid and last element, go right
            if nums[mid] < target <= nums[high]: 
                low = mid + 1
            # Else, go left
            else:
                high = mid
        
    return low if nums[low] == target else -1

nums = list(map(int,input("Enter the elements: ").split()))
target = int(input("Enter target: "))
result = search(nums, target)
print(result)