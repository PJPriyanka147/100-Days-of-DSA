#Brute force --
def majorityelement(nums):
    for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    count += 1

            if count > len(nums) // 2:
                return nums[i]

nums = list(map(int, input("Enter the elements: ").split()))
result = majorityelement(nums)
print(result)


#using Hashmap(Dictionary) --
def majorityelement(nums):
     counts = {}
     for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

        if counts[num] >  len(nums) // 2:
            return num

nums = list(map(int, input("Enter the elements: ").split()))
result = majorityelement(nums)
print(result)

#Using Boyer-Moore Voting Algorithm -- This algorithm maintains a count,
#which is incremented and decremented based on the current candidate. 
#It has a time complexity of O(n) and a space complexity of O(1).
def majorityelement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count ==  0:
            candidate = num
        count += (1 if num == candidate else -1)   

    return candidate       

nums = list(map(int, input("Enter the elements: ").split()))
result = majorityelement(nums)
print(result)