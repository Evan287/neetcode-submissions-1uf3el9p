from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        most_common_element = max(set(nums), key=nums.count)
        return most_common_element