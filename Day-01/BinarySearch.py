# #Python Program for Binary Search 

# #1.Iterative Binary Search(...O(log n)...)
# #2.Recursive Binary Search(...O(log n)...)
# #3.Using Standard Library(...O(log n)...)
# #4.For Insertion Position(...O(log n)...)

# #1.Iterative
# # def binarySearch(nums, target):
# #     left,right = 0, len(nums)

# #     while left <= right:
# #         mid = left + (right - left) // 2

# #         if nums[mid] == target:
# #             return mid
# #         elif nums[mid] < target:
# #             left =  mid + 1
# #         else:
# #             right = mid - 1
# #     return -1

# # arr = list(map(int, input().split()))
# # target = int(input())
# # result = binarySearch(arr, target)
# # print(result)

# #2.Recursive
# # def binary_search_recursive(arr, target, left, right):
# #     # Base case: target is not found
# #     if left > right:
# #         return -1
# #     # Calculate the middle index
# #     mid = left + (right - left) // 2

# #     # Check if the target is at the mid position
# #     if arr[mid] == target:
# #         return mid
# #     # If the target is less than the mid element, search the left half
# #     elif arr[mid] > target:
# #         return binary_search_recursive(arr, target, left, mid - 1)
# #      # If the target is greater than the mid element, search the right half
# #     else:
# #         return binary_search_recursive(arr, target, mid + 1, right)
    
# # # Helper function to initiate the recursive search
# # def binary_search(arr, target):
# #     return binary_search_recursive(arr, target, 0, len(arr) - 1)

# # arr = list(map(int, input().split()))
# # target = int(input())
# # result = binary_search(arr, target)
# # print(result)

# # #Using standard library(bisect module)
# import bisect

# def binary_search(arr, target):
#     # Use bisect_left to find the insertion point
#     index = bisect.bisect_left(arr, target)
    
#     # Check if the target is actually present at the found index
#     if index < len(arr) and arr[index] == target:
#         return index
#     else:
#         return -1

# # Example usage
# arr = list(map(int, input().split()))
# target = int(input())
# result = binary_search(arr, target)
# print(result)

# # #4.For insertion position
# # def search_insert_position(arr, target):
# #     left, right = 0, len(arr) - 1
    
# #     while left <= right:
# #         mid = left + (right - left) // 2
        
# #         if arr[mid] == target:
# #             return mid
# #         elif arr[mid] < target:
# #             left = mid + 1
# #         else:
# #             right = mid - 1
    
# #     return left

# # # Example usage
# # arr = list(map(int, input().split()))
# # target = int(input())
# # position = search_insert_position(arr, target)
# # print(position)