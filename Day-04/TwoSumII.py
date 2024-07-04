#Using Brute force -- Gives Time Limit Error
from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]

arr = list(map(int, input("Enter the Elements: ").split()))
target = int(input("Enter target: "))
print("The indices are: ",twoSum(arr, target))


#Using two pointer --
def two_sum(numbers, target):
     left, right = 0, len(numbers) - 1

     while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
             left += 1
        else:
             right -= 1

arr = list(map(int, input("Enter the Elements: ").split()))
target = int(input("Enter target: "))
print("The indices are: ",two_sum(arr, target))
