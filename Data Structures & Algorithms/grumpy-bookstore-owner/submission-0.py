class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        L = 0
        window = max_window = 0
        satisfied = 0

        for R in range(len(customers)):
            if grumpy[R]:
                window += customers[R]
            else:
                satisfied += customers[R]
            
            if R - L + 1 > minutes:
                if grumpy[L]:
                    window -= customers[L]
                L += 1
            max_window = max(max_window, window)
        return satisfied + max_window