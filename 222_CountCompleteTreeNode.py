

class Solution:
    # This is about Binary Tree (BT). The number of the nodes in a complete BT is 2 to power level minus 1 
    # (2^level) - 1.
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_num = self.left(root.left)
        right_num = self.right(root.right)
        
        if left_num == right_num:
            return (2**left_num) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def left(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.left(root.left)
    
    def right(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.right(root.right)
    
    def getLeftHeight(self, root):
        count=1
        while root.left:
            count += 1
            root = root.left
        return count
    
    def getRightHeight(self, root):
        count=1
        while root.right:
            count += 1
            root = root.right
        return count


if __name__ == '__main__':
    main()
