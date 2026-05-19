class Solution:
    def calPoints(self, operations: List[str]) -> int:
        recordStack = []

        for i in operations:
            if i == "+":
                recordStack.append((recordStack[-1]) + (recordStack[-2]) )
            elif i == "D":
                recordStack.append((recordStack[-1]) *2)
            elif i == "C":
                recordStack.pop()
            else:
                recordStack.append(int(i))

        return sum(recordStack)