def linearSearch(arr, key):
    index = 0
    for i in range(len(arr)):
        if arr[i] == key:
            return i
        index += 1
    return -1

arr = list(map(int,input().split()))
key = int(input())
result = linearSearch(arr, key)
print(result)