#Brute Force--
def TwoSum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return -1     

arr = list(map(int, input("Enter the elements: ").split()))
target = int(input("Enter Target: "))
print(TwoSum(arr, target))

#Using two pointer technique--
def two_sum(nums, target):
    #Create a list of tuples where each tuple is (value, index)
    nums_with_indices = [(num, index) for index, num in enumerate(nums)]

    nums_with_indices.sort()

    #initialize two pointers
    left , right = 0, len(nums) - 1

    #move the pointes until they meet
    while left < right:
        current_sum = nums_with_indices[left][0] + nums_with_indices[right][0]

        if current_sum == target:
            return[nums_with_indices[left][1], nums_with_indices[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

arr = list(map(int, input("Enter the elements: ").split()))
target = int(input("Enter Target: "))
print(two_sum(arr, target))