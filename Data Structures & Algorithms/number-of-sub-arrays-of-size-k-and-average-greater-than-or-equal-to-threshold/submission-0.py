class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L, res = 0, 0
        windowSum = 0

        for R in range(len(arr)):
            target = k * threshold
            windowSum += arr[R]
            if R - L + 1 > k:
                windowSum -= arr[L]
                L += 1
            if R - L + 1 == k:
                if windowSum >= target:
                    res += 1
        return res


