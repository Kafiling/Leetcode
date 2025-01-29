class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            match i:
                case ")":
                    if len(stack) == 0 or not stack[-1] == "(":
                        return False
                    stack.pop()
                case "]":
                    
                    if len(stack) == 0 or not stack[-1] == "[":
                        return False
                    stack.pop()
                case "}":
                    if len(stack) == 0 or not stack[-1] == "{":
                        return False
                    stack.pop()
                case _ :
                    stack.append(i)

        if len(stack) == 0: return True
        return False
        
