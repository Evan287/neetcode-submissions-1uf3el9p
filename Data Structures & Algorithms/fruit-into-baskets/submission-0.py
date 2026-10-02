class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        L, total, maxFruit = 0, 0, 0
        count = defaultdict(int)
        for R in range(len(fruits)):
            count[fruits[R]] += 1
            total += 1

            while len(count) > 2:
                f = fruits[L]
                count[f] -= 1
                total -= 1
                L += 1
                if not count[f]:
                    count.pop(f)
            maxFruit = max(maxFruit, total)
        return maxFruit