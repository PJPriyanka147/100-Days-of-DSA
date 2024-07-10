#Using brute force --
def rearrange_array(nums):
    positives = []
    negatives = []

    for num in nums:
        if num > 0:
            positives.append(num)
        else:
            negatives.append(num)

    result = []
    for i in range(len(positives)):
        result.append(positives[i])
        result.append(negatives[i])
        
    return result

nums = list(map(int, input("Enter Elements of array: ").split()))
result = rearrange_array(nums)
print(result)

#using two pointer --
def rearrange_array(nums):
    result = [0] * len(nums)

    pos_index = 0
    neg_index = 1

    for num in nums:
        if num > 0:
            result[pos_index] = num
            pos_index += 2
        else:
            result[neg_index] = num
            neg_index += 2

    return result

nums = list(map(int, input("Enter Elements of array: ").split()))
result = rearrange_array(nums)
print(result)
