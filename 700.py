# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


    def searchBST2(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        if root.val == val:
            return root
        while (root != None and root.val != val):
            if root.val > val:
                root = root.left
            else:
                root = root.right
        return root


    def print_tree(self, root: TreeNode):
        if root is None:
            return
        print(root.val, end=' ')
        self.print_tree(root.left)
        self.print_tree(root.right)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    root.right = TreeNode(7)


    s.print_tree(s.searchBST2(root, 2))
    '''
        4
       / \
      2   7
     / \   
    1   3   
    '''