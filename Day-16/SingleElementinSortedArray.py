#Brute force--
def singleElement(nums):
    for i in range(0, len(nums), 2):
        if i+1 >= len(nums) or nums[i] != nums[i+1]:
            return nums[i]
        
nums = list(map(int, input("Enter array elements: ").split()))
result = singleElement(nums)
print("Single Element is:", result)

