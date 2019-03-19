class _Node:
    def __init__(self, data = None):
        self.data = data
        self.parent = None


class Stack():
    def __init__(self):
        self.peak = None
        
    def push(self,data=None):
        new = _Node(data)
        if self.peak is not None:
            new.parent = self.peak
        self.peak = new
    
    def pop(self):
        rtrn = self.peak
        if rtrn is None:
            raise Exception('Stack is empty.')
        self.peak = self.peak.parent
        return rtrn
            
    def top(self):
        return self.peak
    
    def isEmpty(self):
        return self.peak is None
