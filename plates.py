
class Stack(object):
    def __init__(self):
        self.stack=[]

class SetofStacks(object):
    def __init__(self, threshold):
        self.stack_set=[]
        self.stack_num=1
        self.threshold=threshold

    def push(self, item):
        if len(self.stack_set) == threshold:
            stack = Stack()
            self.stack_set.append(stack)
        else:
            self.stack_set.append(item)

    