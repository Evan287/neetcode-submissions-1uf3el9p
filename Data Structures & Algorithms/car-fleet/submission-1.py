class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #list comperehension, create array of pairs
        pair = [[p,s] for p,s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair, reverse=True): #Reverse Sorted Order
            stack.append((target - p) / s) #want it to be float
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()#Decreases the number of car fleets
        return len(stack) 
