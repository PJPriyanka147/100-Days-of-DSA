#Using Brute force -- inefficient for large datasets
def three_sum_brute_force(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplet = [arr[i], arr[j], arr[k]]
                    triplet.sort()
                    if triplet not in result:
                        result.append(triplet)

    return result

arr  = list(map(int, input("Enter the elements: ").split()))
print(three_sum_brute_force(arr))

#Using two pointer --
def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue #To Skip duplicates of the first element
        
        target = -nums[i]
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return  result
                
arr  = list(map(int, input("Enter the elements: ").split()))
triplet = three_sum(arr)        
print(triplet)   
