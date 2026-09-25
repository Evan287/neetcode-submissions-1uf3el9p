class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        maxSequence = 0 
        for num in unique:
            if (num - 1) not in unique:
                curr = num
                length = 1
                while curr + 1 in unique:
                    curr += 1
                    length += 1 
                maxSequence = max(maxSequence, length)
        return maxSequence
            
