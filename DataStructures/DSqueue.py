from node import Node

class Queue():

    def __init__(self):
        self.first = Node()
        self.last = Node()
        self.length = 0

    def peek(self):
        return self.first.get_data()

    def push(self, value):
        new_node = Node()
        new_node.set_data(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.set_nex(new_node)
            self.last = new_node
        self.length +=1

    def pop(self):
        if self.length == 0:
            raise ValueError("The queue is empty.")
        if self.first == self.last:
            self.last == None
        off = self.first.get_data()
        self.first = self.first.get_nex()
        self.length -=1
        return off

if __name__ == "__main__":
    q = Queue()
    print(q.peek())
    q.push(1)
    q.push(2)
    print(q.peek())
    print(q.pop())
    q.push(3)
    print(q.pop())
    print(q.peek())