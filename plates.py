
class Stack(object):
    """ stack class """
    def __init__(self, threshold):
        self.stack=[]
        self.threshold = threshold

    def push(self.item):
        if len(self.stack) >= threshold:
            break
        else:
            self.stack.append(item)

    def pop(self):
        self.stack.pop()

class SetofStacks(Stack()):
    """creates a set of stacks"""
    def __init__(self, threshold):
        super().__init__(self,threshold):
        self.stack_set=[]
        self.stack_num=1
        self.threshold=threshold

    def push(self, item):
        if len(self.stack_set) == threshold:
            stack = Stack()
            self.stack_set.append(stack)
        else:
            self.stack_set.append(item)




