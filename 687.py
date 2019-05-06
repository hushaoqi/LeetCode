# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        self.length(root)
        return self.res

    def length(self, root:TreeNode)->'int':
        if root is None:
            return 0
        left = self.length(root.left)
        right = self.length(root.right)

        left_len = right_len = 0
        if root.left and root.left.val == root.val:
            left_len = left + 1

        if root.right and root.right.val == root.val:
            right_len = right + 1

        self.res = max(self.res, left_len + right_len)
        return max(left_len, right_len)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.left.left.left = TreeNode(1)
    root.right = TreeNode(6)
    root.right.right = TreeNode(8)
    root.right.right.left = TreeNode(7)
    root.right.right.right = TreeNode(9)

    print(s.longestUnivaluePath(root))
    '''
        5
       / \
      1   6
     / \    \
    1   1    8
   /        / \
  1        7   9
'''