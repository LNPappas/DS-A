class Node():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Binary():
    ''' 
        lookup(value): O(log(n))
        insert(value): O(log(n))
        delete(value): O(log(n))
    '''
    def __init__(self):
        self.root = None
        self.all = []
    
    def insert(self, value):
        node = Node(value)
        if self.root == None:
            self.root = node
        else:
            current = self.root
            while(True):
                if value <= current.value:
                    if current.left == None:
                        current.left = node
                        break
                    else:
                        current = current.left
                else:
                    if current.right == None:
                        current.right = node
                        break
                    else:
                        current = current.right
        self.all.append(value)
        
    def bfs(self):
        current = self.root
        l = []
        queue = [current]
        while len(queue) > 0:
            current = queue.pop(0)
            l.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return l
    
    def traverseInOrder(self, node, l):
        if node.left:
            self.traverseInOrder(node.left, l)
        l.append(node.value)
        if node.right:
            self.traverseInOrder(node.right, l)
        return l
    
    def traversePreOrder(self, node, l):
        l.append(node.value)
        if node.left:
            self.traversePreOrder(node.left, l)
        if node.right:
            self.traversePreOrder(node.right, l)
        return l
    
    def traversePostOrder(self, node, l):
        if node.left:
            self.traversePostOrder(node.left, l)
        if node.right:
            self.traversePostOrder(node.right, l)
        l.append(node.value)
        return l
        
    def defInorder(self):
        return self.traverseInOrder(self.root, [])
    
    def dfsPreorder(self):
        return self.traversePreOrder(self.root, [])
     
    def dfsPostorder(self):
        return self.traversePostOrder(self.root, [])
    
    
        
if __name__ == '__main__':
    tree = Binary()
    tree.insert(5)
    for n in range(9):
        tree.insert(n)
        
    #   5
    # 0   6
    #  1   7
    #   2   8
    #    3   
    #     4
    #      5
    
    print(f'bfs: {tree.bfs()}')
    print(f' dfs in-order: {tree.defInorder()}')
    print(f'  dfs pre-order: {tree.dfsPreorder()}')
    print(f'   dfs post-order: {tree.dfsPostorder()}')

    
    # nextLeft = tree.root
    # nextRight = tree.root.right
    # while(True):
    #     if nextLeft != None:
    #         print(nextLeft.value)
    #         nextLeft = nextLeft.left
    #     if nextRight != None:
    #         print(nextRight.value)
    #         nextRight = nextRight.right
    #     if nextLeft == None and nextRight == None:
    #         break
        