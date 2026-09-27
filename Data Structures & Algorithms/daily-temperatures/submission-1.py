class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Stack
        stack = []
        #Fixed size array of len(temperatures)
        res = [0] * len(temperatures)
        #Look at each index and temp of temperatures
        for i, temp in enumerate(temperatures):
        #Loop while the stack is non empty and the temp is > top of stack  
            while stack and temp > temperatures[stack[-1]]:    
                #if condition met, store top of stack, add popped val - index to res[poppedIndex]
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            #if its not then push the index onto the stack
            stack.append(i)
        return res