#Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, 
#compares adjacent elements, and swaps them if they are in the wrong order. This
#process is repeated until the list is sorted.
#steps to to  bubble sort --
#1.Start at the beginning of the array.
#2.Compare adjacent elements.
#3.Swap if the first element is greater than the second.
#4.Move to the next pair and repeat.
#5.Complete one pass to place the largest unsorted element at the end.
#6.Repeat the process for the remaining unsorted portion of the array.
#7.Stop when no swaps are needed in a pass.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapped = True
        if not swapped:
            break
    return arr

arr = list(map(int, input("Enter the Elements: ").split()))
result = bubble_sort(arr)
print("Sorted array: ", result)
