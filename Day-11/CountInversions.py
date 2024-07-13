#Brute force --
def inversionCount(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                count += 1
        
    return count

arr = list(map(int, input("Enter the elements: ").split()))
result = inversionCount(arr)
print("Total inversions:", result)