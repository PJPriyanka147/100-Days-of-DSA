def quick_sort(arr):
    #base case: array with element 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]#choosing middle as pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return quick_sort(left) + middle + quick_sort(right)
    
arr = list(map(int, input("Enter the elements: ").split()))
print("Sorted Array: ", quick_sort(arr))