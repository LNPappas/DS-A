# Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


INT_MAX = 4294967296
INT_MIN = -4294967296

class Solution(object):
    def isValidBST(self, node):
        """
        :type node: TreeNode
        :rtype: bool
        """

        # Returns true if the given tree is a BST and its values 
        # >= min and <= max 
        def isBSTUtil(node, mini, maxi): 

            # An empty tree is BST 
            if node is None: 
                return True

            # False if this node violates min/max constraint 
            if node.val < mini or node.val > maxi: 
                return False

            # Otherwise check the subtrees recursively 
            # tightening the min or max constraint 
            return (isBSTUtil(node.left, mini, node.val -1) and
                  isBSTUtil(node.right, node.val+1, maxi)) 

        return (isBSTUtil(node, INT_MIN, INT_MAX)) 


