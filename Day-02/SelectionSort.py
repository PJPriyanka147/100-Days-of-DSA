#Selection sort is a sorting algorithm that repeatedly selects the smallest (or largest)
#element from an unsorted portion of the list and swaps it with the first unsorted element.
#This process continues until the entire list is sorted.
#Steps to do Selection sort -
#1.Select minimum element from the Collection
#2.Place selected element in appropriate position
#3.Apply this technique on the remaining element

def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]

    return arr

arr = list(map(int, input("Enter the elements of the list: ").split()))
result = selection_sort(arr)
print(result)