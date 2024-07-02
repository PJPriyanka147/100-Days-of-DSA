#Linear search is a simple algorithm that sequentially checks each element
#in a list until it finds the target element or reaches the end of the list.

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

arr = list(map(int, input("Enter the elements: ").split()))
target = int(input("Enter the element to search: "))
result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")