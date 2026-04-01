class Solution:
    def isValid(self, s: str) -> bool:
        #Initialize Stack
        stack = []
        #HashMap to pair open and closing brackets
        closeToOpen = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        #Loop through every character in s
        for c in s:
            #If the character is in closeToOpen make sure that they match
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                #If they don't match then return False
                else:
                    return False
            #If no closing bracket then append to stack
            else: 
                stack.append(c)
        #Returns True if stack is empty, False otherwise
        return not stack
        

         