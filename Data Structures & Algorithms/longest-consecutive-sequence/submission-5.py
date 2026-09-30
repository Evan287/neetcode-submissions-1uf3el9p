class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length = 1
        count = 0
        longest = 0
        for i, n in enumerate(nums):
            if (n - 1) not in numSet:
                while(n + length) in numSet:    
                    count += 1
                    length += 1
                longest = max(longest, length)
                length = 1
        return longest

                    