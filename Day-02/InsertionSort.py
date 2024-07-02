#Insertion sort is a straightforward sorting algorithm where each element is taken from 
#the unsorted part of the array and inserted into its correct position in the sorted part
#by shifting larger elements to the right.This process continues until the entire array is sorted.
#Steps to do Insertion sort-
#1.select one element at a time from the left of the collection
#2.Inserst the element at proper positon
#3.After insertion, every element to its left will be sorted

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        #Moving elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = list(map(int, input("Enter the elements: ").split()))
insertion_sort(arr)
print(arr)