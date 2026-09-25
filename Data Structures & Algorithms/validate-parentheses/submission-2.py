class Solution:
    def isValid(self, s: str) -> bool:

        stack = [] #most recent open bracket

        pairs = { #hashmap to map close to open bracket 
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for char in s:
            
            if char not in pairs: 
                #open bracket
                stack.append(char)
            
            else:
                #closed bracket
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
        
        return True if stack == [] else False

        