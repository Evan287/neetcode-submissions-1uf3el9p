class Solution:
    def check(self, nums: List[int]) -> bool:
        #Keep a count of nums that are greater than next num
        #Can only be out of order at most once
        #Use Circular array traversal using modulo arithmetic
        N = len(nums)
        count = 0
        for i in range(N):
            if nums[i] > nums[ (i+1) % N]:
                count += 1
            if count > 1:
                return False
        return True