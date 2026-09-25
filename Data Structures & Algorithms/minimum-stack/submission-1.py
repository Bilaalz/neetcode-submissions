class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None: #storing tuple of (val, min val seen)
        if not self.stack:
            self.stack.append((val, val))
        
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop()[0]
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
