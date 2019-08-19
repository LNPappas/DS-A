class Stackqueue():

    def __init__(self):
        self.first = []
        self.last = []


    def enqueue(self, value):
        length = len(self.first)
        while length > 0:
            self.last.append(self.first.pop())
            length -=1
        self.last.append(value)


    def dequeue(self):
        length = len(self.last)
        while length > 0:
            self.first.append(self.last.pop())
            length -=1
        return self.first.pop()

    
    def peek(self):
        if len(self.last) > 0:
            return self.last[0]
        else:
            return self.first[len(self.first)-1]


if __name__ == "__main__":
    q = Stackqueue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.peek())
    print(q.dequeue())
    q.enqueue(3)
    print(q.dequeue())
    print(q.peek())

