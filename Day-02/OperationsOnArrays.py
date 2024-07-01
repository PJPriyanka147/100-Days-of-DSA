#Basic operations on Arrays--

#Printing Elements--
def printarray(arr):
    for i in range(len(arr)):
        print(f"index {i} :", arr[i])


arr = list(map(int, input().split()))
printarray(arr)


