# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None:
            return None
        # 先判断根结点，是否在范围内
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)

        return root

    # 非递归
    def trimBST2(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None:
            return None
        # 处理根结点
        while root.val < L or root.val > R:
            root = root.right if root.val < L else root.left

        node = root
        while node:
            while node.left and node.left.val < L:
                node.left = node.left.right
            node = node.left

        node = root
        while node:
            while node.right and node.right.val > R:
                node.right = node.right.left
            node = node.right

        return root

    def print_tree(self, root: TreeNode):
        if root is None:
            return
        print(root.val,end=' ')
        self.print_tree(root.left)
        self.print_tree(root.right)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    root.right = TreeNode(6)
    root.right.right = TreeNode(7)

    L = 3
    R = 6
    s.print_tree(s.trimBST2(root, L, R))
    '''
        5
       / \
      3   6
     / \    \
    2   4    7

'''