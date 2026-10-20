class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        for num, count in count.items():
            if count > (len(nums) / 2):
                return num
        