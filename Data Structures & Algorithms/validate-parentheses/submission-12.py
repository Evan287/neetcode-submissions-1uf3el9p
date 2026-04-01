class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            #If there is nothing in the stack then return False
            elif len(stack) == 0:
                return False
            #elif statements to pair opening and closing brackets
            elif stack[-1] == "[" and char == "]":
                stack.pop()
            elif stack[-1] == "(" and char == ")":
                stack.pop()
            elif stack[-1] == "{" and char == "}":
                stack.pop()
            else:
                return False
        return not stack #Returns True if stack is empty, False otherwise
                


        

         