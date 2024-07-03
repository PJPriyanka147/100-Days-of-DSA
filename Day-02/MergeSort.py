#Merge Sort is a divide-and-conquer sorting algorithm that recursively
#divides an array into smaller subarrays, sorts those subarrays,
#and then merges them back together to form a sorted array.
#Steps to do merge sort --
#1.Split the array into two halves.
#2.Recursively sort the left half.
#3.Recursively sort the right half.
#4.Merge the two sorted halves into one sorted array.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    #find the middle index
    mid = len(arr) // 2

    #divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    #recursively sort the two halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    #merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged = []
    i = j = 0

    #merge the two sorted arrays into a single sorted array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    #append remaining elements of left and right array
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

arr = list(map(int, input("Enter the elements: ").split()))
sorted_array = merge_sort(arr)
print("Sorted Array: ", sorted_array)