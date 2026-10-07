class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        total_cost = 0

        while len(sticks) > 1:
            new_stick = heapq.heappop(sticks) + heapq.heappop(sticks)
            total_cost += new_stick
            heapq.heappush(sticks, new_stick)

        return total_cost