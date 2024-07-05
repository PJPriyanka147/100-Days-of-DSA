#Using Brute Force -- inefficient for large arrays
def four_sum_brute_force(arr, target):
    result = set()

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                for l in range(k+1, len(arr)):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        quadruplet = tuple(sorted([arr[i], arr[j], arr[k], arr[l]]))
                        result.add(quadruplet)
    
    return list(result)

arr = list(map(int, input("Enter the elements: ").split()))
target = int(input("Enter target: "))
print(four_sum_brute_force(arr, target))

#Using Two pointer --
def four_sum(nums, target):
    nums.sort()
    result = []
    n =  len(nums)

    for i in range(n - 3):  #First element

        if i > 0 and nums[i] == nums[i - 1]:
            continue  #Skip duplicate elements

        for j in range(i + 1, n - 2):  #Second element
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue  #Skip duplicate elements

            left, right = j + 1, n - 1  #Two-pointer technique

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:  #Check if the sum matches the target
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    
                    #Skip duplicate elements for the third and fourth elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result

    
nums = list(map(int, input("Enter the elements: ").split()))
target = int(input("Enter target: "))
print(four_sum(nums, target))