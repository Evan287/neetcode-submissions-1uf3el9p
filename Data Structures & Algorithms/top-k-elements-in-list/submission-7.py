class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCnt = Counter(nums)
        res = []
        while k > 0:
            max_num = max(numCnt, key=numCnt.get)
            res.append(max_num)
            numCnt[max_num] = -1
            k -= 1
        return res