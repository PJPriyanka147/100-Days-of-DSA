#Find First and Last Position of Element in Sorted Array(Leetcode)
from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    def first_occurrence(nums, target):
        left, right = 0, len(nums) - 1
        first_pos = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                first_pos = mid
                right = mid - 1  # Continue searching to the left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return first_pos

    def last_occurrence(nums, target):
        left, right = 0, len(nums) - 1
        last_pos = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                last_pos = mid
                left = mid + 1  # Continue searching to the right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return last_pos

    first = first_occurrence(nums, target)
    last = last_occurrence(nums, target)

    return [first, last]

# Taking input from user
nums = list(map(int, input().split()))
target = int(input())

# Searching for the range
result = searchRange(nums, target)
print(f"The range of the target {target} is: {result}")
