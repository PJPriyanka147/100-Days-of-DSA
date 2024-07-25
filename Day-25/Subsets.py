#Brute force --
def subsets(nums):
    res = [[]]
    for num in nums:
        new_subsets = []
        for subset in res:
            new_subsets.append(subset + [num])
        res.extend(new_subsets)
    return res

nums = list(map(int, input("Enter array: ").split()))
result = subsets(nums)
print(result)