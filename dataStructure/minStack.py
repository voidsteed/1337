class MinStack:
    # @param x, an integer
    # @return an integer
    
    def __init__(self):
        self._stack = []
        self._minstack = []
        
    def push(self, x):
        self._stack.append(x)
        if self._minstack == []:
            self._minstack.append(x)
        elif self._minstack[-1] >= x:
            self._minstack.append(x)
        else:
            self._minstack.append(self._minstack[-1])


    # @return nothing
    def pop(self):
        self._stack.pop(-1)
        self._minstack.pop(-1)
        

    # @return an integer
    def top(self):
        return self._stack[-1]
        

    # @return an integer
    def getMin(self):
        return self._minstack[-1]
