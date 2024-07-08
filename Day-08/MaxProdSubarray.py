#Brute Force -- inefficient 
def max_product_subarray(nums):
    n =  len(nums)
    #Start with the smallest possible number for handling
    #negative no and zeroes
    max_product = float('-inf')
    curr_product = nums[0]

    for i in range(n):
        curr_product = 1
        for j in range(i, n):
            curr_product *= nums[j]
            if curr_product > max_product:
                max_product =  curr_product

    return max_product

nums = list(map(int, input("Enter the elements: ").split()))
result = max_product_subarray(nums)
print(result)

#Using Kadanes Algorithm -- 
def max_product_subarray(nums):
    if not nums:#for empty array
        return 0
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for i in range(1,len(nums)):
        if nums[i] < 0:
            max_product, min_product = max_product, min_product

            max_product = max(nums[i] , nums[i] * max_product)
            min_product = min(nums[i], nums[i] * min_product)

            result = max(result, max_product)
        
    return result

nums = list(map(int, input("Enter the elements: ").split()))
result = max_product_subarray(nums)
print(result)
