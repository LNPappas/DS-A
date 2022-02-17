from TreeNode import TreeNode

class BinaryTree():
    def __init__(self, value=None):
        self.root = TreeNode(value)
        self.all = []
    
    def insert(self, value):
        node = TreeNode(value)
        if self.root == None:
            self.root = node
        else:
            current = self.root
            while(True):
                if current.value < value:
                    if current.right == None:
                        current.right = node
                        break
                    else:
                        current = current.right

                else:
                    if current.left == None:
                        current.left = node
                        break
                    else:
                        current = current.left

            self.all.append(value)
    def breadth_first_search(self, value):
        current = self.root
        breadth_list = []
        queue = [current]
        
        while len(queue) >0:
            current = queue.pop(0)
            breadth_list.append(current.value)
            if value == current.value:
                break
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return breadth_list
    
    def inorder(self, node, l):
        if node.left:
            self.inorder(node.left, l)
        l.append(node.value)
        if node.right:
            self.inorder(node.right, l)
        return l
        
    def preorder(self, node, l):
        l.append(node.value)
        if node.left:
            self.preorder(node.left, l)
        if node.right:
            self.preorder(node.right, l)
        return l

    def postorder(self, node, l):
        if node.left:
            self.postorder(node.left, l)
        if node.right:
            self.postorder(node.right, l)
        l.append(node.value)
        return l
    
    def depth_first_search(self, type):
        if type == 'inorder':
            return self.inorder(self.root, [])
        elif type == 'preorder':
            return self.preorder(self.root, [])
        else:
            return self.postorder(self.root, [])
                    
                        
                
                
if __name__ == '__main__':
    bt = BinaryTree(5)
    bt.insert(4)
    bt.insert(7)
    bt.insert(6)
    bt.insert(3)
    bt.insert(5)
    bt.insert(9)
    bt.insert(10)
    bt.insert(8)
    bt.insert(11)
    
    
    #      5
    #     / \
    #    4   7
    #   / \ / \
    #  3  5 6  9
    #         / \
    #        8   10
    #             \
    #              11
    
    print(f'All Nodes: {bt.all}')
    print(f'BFS 3: {bt.breadth_first_search(3)}')
    print(f'BFS 4: {bt.breadth_first_search(4)}')
    print(f'BFS 6: {bt.breadth_first_search(6)}')
    print(f'BFS 11: {bt.breadth_first_search(11)}')
    print(f'BFS 8: {bt.breadth_first_search(8)}')
    
    
    
    print(f'DFS InOrder 3: {bt.depth_first_search("inorder")}')
    print(f'DFS PreOrder 4: {bt.depth_first_search("preorder")}')
    print(f'DFS PostOrder 6: {bt.depth_first_search("postorder")}')

    
        