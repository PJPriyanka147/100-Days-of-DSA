#Brute Force --
def reverse_pairs(nums):
    count = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > 2 * nums[j]:
                count += 1

    return count
    

nums = list(map(int, input("Enter array elements: ").split()))
result = reverse_pairs(nums)
print(result)
