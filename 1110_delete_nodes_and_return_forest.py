# https://leetcode.com/problems/delete-nodes-and-return-forest/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.output = []
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        # a root tree is hierachical and just like the link list
        node = root
        self.traverse_tree(node, to_delete, parent_exist=False)
        
        print(self.output)
        return self.output
    
    def traverse_tree(self, node, to_delete, parent_exist):
        if node.val in to_delete:
            # The deleted node keeps traversing its children and notifies its childeren their parent do not exist, so their children will be the parent now  
            if node.left:
                self.traverse_tree(node.left, to_delete, parent_exist=False)
            
            if node.right:
                self.traverse_tree(node.right, to_delete, parent_exist=False)
            
            # The deleted node needs to notify its parent that it is in the to-delete-list. Return None to remove itself from the parent. Poor guy :(
            return None
            
        else:
            if not parent_exist:
                # If no parent of this node, it is the parent node (the start of the forest)
                self.output.append(node)
            # Traverse into the children if they exist. However, they may be in the to-delete-list. If they are in, it receive None for deletion 
            if node.left:
                node.left = self.traverse_tree(node.left, to_delete, parent_exist=True)
            if node.right:
                node.right = self.traverse_tree(node.right, to_delete, parent_exist=True)
            
            # Return itself. Tell its parent that it is not in the to-delete-list and stays as it is :)
            return node


def _flatten_tree(b_tree, flatten_forest):
    flatten_forest.append(b_tree.val)
    if b_tree.left:
        _flatten_tree(b_tree.left, flatten_forest)
    if b_tree.right:
        _flatten_tree(b_tree.right, flatten_forest)



def main():
    root = [1,2,3,4,5,6,7] # how to build a binary tree?

    to_delete = [3,5]
    solution = Solution()
    tree_output = solution.delNodes(root, to_delete)

    print(tree_output)

    forests = []
    for b_tree in tree_output:
        forest = []
        _flatten_tree(b_tree, forest)
        forests.append(forest)
    
    print(forests)

if __name__ == "__main__":
    main()
