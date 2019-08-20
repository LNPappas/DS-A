class Node():

    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value


class BST():

    def __init__(self):
        self.root = None
        self.all = []


    def insert(self, value):
        
        new = Node()
        current = Node()
        new.value = value
        if self.root == None:
            self.root = new
            self.all.append(value)
        else:
            current.value = self.root.value
            while(True):
                if new.value < current.value:
                    if current.left == None:
                        current.left = value
                        break
                    else:
                        current = current.left
                else:
                    if current.right == None:
                        current.right = value
                        break
                    else:
                        current = current.right
            self.all.append(value)
    

    def lookup(self, value):
        current = Node()
        current.value = self.root.value
        while True:
            if current.value == None:
                return False
            if value == current.value:
                return True
            if value < current.value:
                current.value = current.left
            elif value > current.value:
                current.value = current.right
        return False


    def delete(self, value):
        pass


    def traverse(self):
        print(self.all)
            



if __name__ == "__main__":
    tree = BST()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)
    print(tree.lookup(9))
    print(tree.lookup(1))
    print(tree.lookup(100))
    tree.traverse()
