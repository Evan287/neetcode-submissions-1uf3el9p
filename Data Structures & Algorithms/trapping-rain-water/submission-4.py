class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[0], height[len(height) - 1]
        water = 0
        while l < r:
            if height[l] <= height[r]:
                if maxL - height[l] > 0:
                    water += maxL - height[l]
                maxL = max(maxL, height[l])
                l += 1
            else:
                if maxR - height[r] > 0:
                    water += maxR - height[r]
                maxR = max(maxR, height[r])
                r -= 1
        return water

