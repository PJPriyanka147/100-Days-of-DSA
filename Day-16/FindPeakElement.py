#Brute force --
def findPeak(nums):
    n = len(nums)
    #for array having only one element
    if n == 1:
        return 0
    
    #Check if the first element is a peak
    if nums[0] > nums[1]:
        return 0
    
    #Check if the last element is a peak
    if nums[n-1] > nums[n-2]:
        return n-1
    
    #Iterate over the elements from the second to the second last
    for i in range(1, n-1):

        #Check if the current element is greater than both its neighbors
        if nums[i]> nums[i-1] and nums[i] > nums[i+1]:
            return i

nums = list(map(int,input("Enter array Elements:").split()))
result = findPeak(nums)
print(result)

