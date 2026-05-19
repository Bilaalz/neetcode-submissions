class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        result = 0

        for token in tokens:
            if token in '+-*/':
                latest = int(stack.pop())
                first = int(stack.pop())

                if token == '+':
                    result = first + latest
                    stack.append(result)
                
                if token == '-':
                    result = first - latest
                    stack.append(result)
                
                if token == '*':
                    result = first * latest
                    stack.append(result)
                
                if token == '/':
                    result = int(first / latest)
                    stack.append(result)
            else:
                stack.append(token)
                
                

        return int(stack.pop())
                       