# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
class Solution:
    MAX = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxDepth(root)
        return self.MAX
    # 递归法
    def maxDepth(self, root: 'TreeNode') -> 'int':
        if root is None: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # 这条路径可能穿过根结点（left + right）,也有可能不穿过根结点（self.MAX）
        self.MAX = max(self.MAX, left + right)
        return max(left, right) + 1

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    '''
    输入:
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    '''
    print(s.diameterOfBinaryTree(root))