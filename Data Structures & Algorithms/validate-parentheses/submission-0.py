class Solution:
    def isValid(self, s: str) -> bool:


        stack = []

        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for ch in s:
            if ch in pairs: #we have a closing bracket
                if stack and stack[-1] == pairs[ch]: #matching open parenthesis and we cannot add closing bracket to empty stack
                    stack.pop()
                else:
                    return False # brackets did not match or first element in stack
            
            else:
                stack.append(ch)
        
        return True if stack == [] else False