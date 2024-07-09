class _Node:
    
    def __init__(self, data=None):
        self.data = data
        self.parent = None

class Stack:

    def __init__(self):
        self.top = None

    def push(self, data):
        node = _Node(data)
        if self.top is not None:
            node.parent = self.top
        self.top = node

    def pop(self):
        rtrn = self.top
        if rtrn is None:
            raise Exception("Stack is empty")
        self.top = self.top.parent
        return rtrn

    def top(self):
        return self.top

    def is_empty(self):
        return self.top is None
