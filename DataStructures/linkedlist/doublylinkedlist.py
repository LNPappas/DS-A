class Node():
    '''
    Node class to be used with Doubly Linked List
    Contains value of current Node &
    Pointers to both the next & previous Nodes
    '''
    def __init__(self, v, n=None, p=None):
        self.value = v
        self.nex = n
        self.prev = None

class DoublyLinkedList():
    '''
    Doubly Linked List keeps track of 
    next Node and previous Node
    can be iterated through in reverse
    '''
    def __init__(self, v):
        '''
        initiate list with given value
        assign Node to both head and tail of list
        sets length of list to 1
        '''
        self.head = self.tail = Node(v)
        # make self.tail.prev self.head for later insertion
        self.tail.prev = self.head
        self.length = 1

    def __len__(self):
        '''
        returns the length of the list with len()
        '''
        return self.length

    def __repr__(self):
        '''
        returns string representaion of list
        to be used with print()
        Prints list in reverse if reversed=True
        '''
        s = ''
        temp = self.head
        while temp != None:
            s += ' ' + str(temp.value)
            temp = temp.nex
        return s

    def printr(self):
        '''
        prints list in reverse order
        '''
        s = ''
        temp = self.tail
        while temp!= None:
            s += ' ' + str(temp.value)
            temp = temp.prev
        return s + ' ' + str(self.head.value)

    def append(self, v):
        '''
        adds Node to end of linked list
        sets tail as new Node
        increases length of linked list
        '''
        newNode = Node(v)
        self.tail.nex = newNode
        newNode.prev = self.tail
        self.tail = newNode
        self.length+=1

    def prepend(self, v):
        '''
        add Node to head/start of list
        sets new Node as head
        increases length by 1
        '''
        newNode = Node(v)
        self.head.prev = newNode
        newNode.nex= self.head
        self.head = newNode
        self.length+=1

    def insert(self, i, v):
        '''
        takes index, value as inputs
        inserts new Node at given index with given value
        adjust previous and next nodes to include new Node
        increases length by 1
        '''
        # if index is 0 then prepend or negative value
        # add to head of list
        if i <= 0:
            self.prepend(v)
        # if index is >= length of the linkned list 
        # then add it to the end
        elif i >= self.length:
            self.append(v)
        # otherwise iterate through the list until at correct
        # index and insert new Node()
        else:
            temp = self.head
            count = 0
            while count != i:
                count +=1
                temp = temp.nex
            newNode = Node(v, temp, temp.prev)
            temp.prev.nex = newNode
            temp.prev = newNode
            self.length+=1

    def remove(self, v):
        temp = self.head
        while temp != None:
            if temp.value == v:
                break
            temp = temp.nex
        if temp == None:
            return False
        else:
            if temp.value == self.head.value:
                self.head = temp.nex
                self.head.prev = None
            elif temp.value == self.tail.value:
                temp.prev.nex = None
            else:
                temp.prev.nex = temp.nex
        self.length-=1
        return True
    
    def lookup(self, v):
        '''
        returns boolean if value in list
        '''
        temp = self.head
        while temp != None:
            if temp.value == v:
                return True
            temp = temp.nex
        return False

    def start(self):
        '''
        returns head of linked list
        '''
        return self.head.value

    def end(self):
        '''
        returns tail of linked list
        '''
        return self.tail.value


if __name__ == "__main__":
    l = DoublyLinkedList('first_start')
    l.append('first_tail')
    print('tail: ', l.end())
    l.insert(1, 'middle')
    print(l)
    print(l.end())
    print(l.printr())
    print('length: ', len(l))
    l.prepend("now I'm first")
    print('Head: ', l.start())
    print("l.insert(0, 1) l.insert(100, 100), l.insert(3,3): ")
    l.insert(0, 1) 
    l.insert(100, 100), 
    print(l.start())
    # l.insert(3,3)
    print(l)
    print("l.lookup(3)", l.lookup(3))
    l.remove(3)
    # l.remove(100)
    # l.remove(1)
    print(l)
    # print("l.lookup(3)", l.lookup(3))
    # print(l.printr())
    


        

        

    