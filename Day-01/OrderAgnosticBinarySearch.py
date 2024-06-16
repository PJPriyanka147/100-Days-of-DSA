#Order Agnostic binary Search - means when the order is not known(ascending or descending)

def order_Agnostic_Binary_Search(arr, target):
    start, end = 0, len(arr) - 1

    # Determine if the array is sorted in ascending or descending order
    is_ascending = arr[start] < arr[end]

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid
        
        if is_ascending:
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return -1

# Example usage:
arr = list(map(int, input().split()))
target = int(input())
result = order_Agnostic_Binary_Search(arr, target)
print(result)