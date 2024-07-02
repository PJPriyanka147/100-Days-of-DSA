#Binary search is an efficient algorithm that finds the position of a target element
#in a sorted list by repeatedly dividing the search interval in half, comparing the 
#target to the middle element, and narrowing the search to the left or right half accordingly.

def binary_search(arr, target):
    left, right = 0 , len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

arr = list(map(int, input("Enter the elements in sorted order: ").split()))
target = int(input("Enter the element to search: "))
result = binary_search(arr, target)

if result != -1:
    print(f"Element is found at index : {result}")
else:
    print("Element not found")





