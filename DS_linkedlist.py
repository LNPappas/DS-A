from node import Node
class Linked_list():
    
    def __init__(self, head):
        self.head = Node()
        self.head.set_data(head)
    
    def insert(self, value):
        node = Node(value)
        node.set_nex(self.head)
        self.head = node

    def remove(self, value):
        current = self.head
        previous = None
        while current:
            if current.get_data() == value:
                break
            else:
                previous = current
                current = current.get_nex()
        if current is None:
            raise ValueError(f"{value} not in list.")
        if previous is None:
            self.head = current.get_nex()
        else:
            previous.set_nex(current.get_nex())

    def print_list(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_nex()

    def size(self):
        current = self.head
        count = 0
        while current:
            count +=1
            current = current.get_nex()
        return count

    def search(self,value):
        current = self.head
        while current:
            if current.get_data() == value:
                break
            else:
                current = current.get_nex()
        if current is None:
            raise ValueError(f"{value} not in list.")
        return current

if __name__ == "__main__":
    link = Linked_list(1)
    link.insert(2)
    link.insert(3)
    link.insert(4)
    link.remove(3)
    print("This size of the list is:", link.size())
    link.print_list()
    
    
