#Using Brute force -- 
def rotate_array(nums, k):
    n = len(nums)
    k = k % n

    for i in range(k):
        last_element = nums[-1]

        for j in range(n-1, 0, -1):
            nums[j] = nums[j - 1]

        nums[0] = last_element

    return nums

arr = list(map(int, input("Enter the elements: ").split()))
k = int(input("Enter K: "))
result = rotate_array(arr, k)
print(result)

#Using Reversal Technique --
def rotate_array(nums, k):
    n = len(arr)
    k = k % n

    #Reverse the entire array
    nums.reverse()

    #Reverse the first k elements
    nums[:k] = reversed(nums[:k])

    #Reverse the last n-k elements
    nums[k:] = reversed(nums[k:])

    return nums

arr = list(map(int, input("Enter the elements: ").split()))
k = int(input("Enter K: "))
result = rotate_array(arr, k)
print(result)

#Using extra space --
def rotate_array(nums, k):
    n = len(nums)
    k = k % n

    #create a new array to store the last k elements
    new_nums = nums[-k:]




#Using cyclic replacement--