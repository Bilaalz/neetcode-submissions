class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            
            if token in "+-/*":
                latest = int(stack.pop())
                prev = int(stack.pop())

                if token == "+":
                    stack.append(latest + prev)
                
                if token == "-":
                    stack.append(prev - latest)
                
                if token == "*":
                    stack.append(latest * prev)
                
                if token == "/":
                    stack.append(int(prev / latest))
            
            else:
                stack.append(token)
            
        return int(stack.pop())
            
            

        