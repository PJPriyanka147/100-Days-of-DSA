def binarysearch_recursive(arr, target, left, right):
    if left > right:
        return -1
    else:
        middle = left + (right - left) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            return binarysearch_recursive(arr, target, middle + 1, right)
        else:
            return binarysearch_recursive(arr, target, left, middle - 1)

arr = list(map(int, input("Enter the Elements in sorted order: ").split()))
target = int(input("Enter the element to search: "))
result = binarysearch_recursive(arr, target, 0 , len(arr) - 1)

if result != -1:
    print(f"Element is found at index: {result}")
else:
    print("Element not found")

        

    




















# def binaryseaarch_recursive(A, key, l, r):
#     if l > r:
#         return -1
#     else:
#         mid = (l + r) // 2
#         if key == A[mid]:
#             return mid
#         elif key < A[mid]:
#             return binaryseaarch_recursive(A,key,l,mid-1)
#         elif key > A[mid]:
#             return binaryseaarch_recursive(A,key,mid+1,r)

# A = [15, 21, 47, 84, 96]
# found = binaryseaarch_recursive(A,17,0,4)
# print('Result:', found)

