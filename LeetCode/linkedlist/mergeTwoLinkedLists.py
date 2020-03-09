class Node():
    '''
    Nodes held by linkedlist
    '''
    def __init__(self, v):
        self.val = v
        self.nex = None

class LinkedList():
    '''
    linked list takes array and makes linkedlist
    '''
    def __init__(self, data):
        self.head = Node(data[0])
        temp = self.head
        for i in range(1, len(data)):
            temp.nex = Node(data[i])
            temp = temp.nex

def merge(l1, l2):
    '''
    combines two sorted linked lists into one
    '''
    # if l1 empty/None return l2 and vice versa
    if not l1 or not l2:
        return l2 or l1
    # if l1 value is less the l2 value
    if l1.val < l2.val:
        # set l1.next to the next val or whichever is less, l1 or l2
        l1.nex = merge(l1.nex, l2)
        return l1
    else:
        # otherwise l2 is less, so do the same with l2
        l2.nex = merge(l1, l2.nex)
        return l2

if __name__ == "__main__":
    l1 = LinkedList([1,2,4])
    l2 = LinkedList([1,3,4])
    l3 = merge(l1.head, l2.head)
    while True:
        print(l3.val)
        l3 = l3.nex
        if l3 == None:
            break



