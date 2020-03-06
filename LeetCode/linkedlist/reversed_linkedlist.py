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

    def __repr__(self):
        temp = self.head
        s = ''
        while temp != None:
            s = s + str(temp.val) + ' '
            temp = temp.nex
        return s
        

    def reverse(self, n, prev=None):
        '''
        returns the reverse of the given linked list
        '''
        # if list is empty return None
        # if end of list, return head
        if not n:
            return prev
        # example [1,2,3]
        # current node becomes head's(1's) next node (2) # 2nd time current node becomes 2's next node 3
        # heads next node (2) becomes prev (None) # n.nex becomes prev(2)
        curr, n.nex = n.nex, prev
        # run again with curr(2) becoming n(1) and n becoming prev # run again with 3, 2, then None, 3 end (returns 3->2->1->None)
        return self.reverse(curr, n)

if __name__ == "__main__":
    l = LinkedList([1,2,3,4,5])
    print(l)
    l.head = l.reverse(l.head)
    print(l)