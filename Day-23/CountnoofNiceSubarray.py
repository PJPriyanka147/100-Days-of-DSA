#Brute force --
def numberofSubarrays(nums, k):
    count = 0
    n = len(nums)

    for start in range(n):
        odd_count = 0
        for end in range(start, n):
            if nums[end] % 2 != 0:
                odd_count += 1
            if odd_count == k:
                count += 1
            elif odd_count > k:
                break
                    
    return count


nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))
result = numberofSubarrays(nums, k)
print(result)