from typing import List


def disallow_negatives(num: int) -> int:
    if max(0,num):
        return num
    else: 
        return 0


def max_difference(nums: List[int]) -> int:
    #two pointer
    #keep track of largest difference
    greatestDiff = 0
    for num1, num2 in zip(nums, nums[1:]):
        if num2 - num1 > greatestDiff:
            greatestDiff = num2 - num1
    return greatestDiff

# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))
