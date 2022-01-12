# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.found_node = None
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # Repeat:
    # -A subtree of a binary tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
    # - are numbers are unique? The answer is they are not unique
    # Example:
    # 1 is also the subtree of the root
    # 2 is also the subree of the root
    # 4-1-2 is also the subtree of the root
    # 5 is also the subtree of the root
    # 3-4-1-2-5 is also the subtree of the root
    
    # Approach:
    # -traverse the root-tree 
    # -check if the whole tree is same as the sub-root-tree
    # -check if the left or the right sub-tree of the root tree is same as sub-root-tree
    # corner cases: both tree are None and one of them is None
    
    # Optimsiation: 
    
    # Code:
        # corner cases
                
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False

        
        # compare whole tree
        
        if self.is_same_tree(root, subRoot):
            return True
        
        # traverse the nodes
        # compare the left subtree 
        if self.isSubtree(root.left, subRoot):
            return True
        # compare the right subtree
        if self.isSubtree(root.right, subRoot):
            return True

        return False
    
    # check if both tree are the same tree
    def is_same_tree(self, tree_1, tree_2):
        # corner cases
        if not tree_1 and not tree_2:
            return True
        
        if not tree_1 or not tree_2:
            return False

        if tree_1.val == tree_2.val:
            if self.is_same_tree(tree_1.left, tree_2.left) and self.is_same_tree(tree_1.right, tree_2.right):
                return True
            
            return False