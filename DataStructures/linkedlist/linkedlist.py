# create node that contains value and 
# points to the next node
class Node():
    def __init__(self, v, n=None):
        self.value = v
        self.nextNode = n

# create linked list, initialize with given data and 
# set as head and tail
class LinkedList():
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    # add to end of list, set to tail
    def append(self, data):
        newNode = Node(data)
        self.tail.nextNode = newNode
        self.tail = newNode

    # print list as string
    def __repr__(self):
        temp = self.head
        s = ''
        while temp != None:
            s = s + str(temp.value) + ' '
            temp = temp.nextNode
        return s

    # remove a value from the linked list
    def remove(self, v):
        # keep track of previous value and curren value
        pre = temp = self.head
        while temp.value != v:
            pre = temp
            temp = temp.nextNode
            # if value not in list return False
            if temp.nextNode == None:
                return False
        # set previous Node to next Node removing data
        pre.nextNode = temp.nextNode
        return True

    # insert a value at a given index
    def insert(self, i, v):
        # keep track of index of linked list
        count = 0
        # set temp node to the start of linked list
        prev = temp = self.head
        # iterate through node until index is reached
        while count != i:
            prev = temp
            temp = temp.nextNode
            count +=1
            # if the index is higher then the number of nodes
            # break and add to end of linked list
            if temp == None:
                break
        # create new node pointing to node at current index
        newNode = Node(v, temp)
        # have the previous node point to the new node
        # if the new node isn't the head
        if i != 0:
            prev.nextNode = newNode
        # if it is, reasign pointer to head
        else:
            self.head = newNode
        # if newnode inserted at end, make it the tail
        if temp == None:
            self.tail = newNode

    # returns start/head of linkedList
    def start(self):
        return self.head.value

    # returns end/tail of linked list
    def end(self):
        return self.tail.value

    # returns bool if value in linked list
    def lookup(self, v):
        temp = self.head
        while temp != None:
            if temp.value == v:
                return True
            else:
                temp = temp.nextNode
        return False
             

if __name__ == "__main__":
    l1 = LinkedList('apple')
    l1.append(2)
    l1.append('frogs')
    l1.append(2.76)
    print(l1)
    print('remove(1): ',l1.remove(1))
    print('remove(2): ', l1.remove(2))
    print(l1)
    l1.insert(0, 'sticks')
    l1.insert(100, 5000)
    l1.insert(2, 2)
    print("l1.insert(0, 'sticks'), l1.insert(100, 5000), l1.insert(2, 2):")
    print(l1)
    print('Start/Head: ', l1.start())
    print('End/Tail: ',l1.end())
    print('lookup(47): ',  l1.lookup(47))
    print('lookup("frogs"): ',l1.lookup('frogs'))

        

    
    