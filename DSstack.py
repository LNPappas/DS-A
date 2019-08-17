from node import Node
class Stack():

    def __init__(self):
        self.top = Node()
        self.bottom = Node()
        self.length = 0


    def peek(self):
        return self.top.get_data()

    
    def push(self, value):
        if self.length == 0:
            self.bottom.set_data(value)
        new_node = Node()
        new_node.set_nex(self.top)
        new_node.set_data(value)
        self.top = new_node
        self.length +=1


    def pop(self):
        if self.length == 0:
            raise ValueError("You have reached the bottom of the stack.")
        off = self.top.get_data()
        self.top = self.top.get_nex()
        self.length -=1
        return off


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    stack.push(3)
    stack.push(4)
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    print(stack.length)
    #print(stack.pop())