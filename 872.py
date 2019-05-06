# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 方法：深度优先搜索
    # 找出给定的两个树的叶值序列。之后，我们可以比较它们，看看它们是否相等。
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        root1_leaf = []
        root2_leaf = []
        self.dfs(root1, root1_leaf)
        self.dfs(root2, root2_leaf)
        print(root1_leaf)
        print(root2_leaf)
        if root1_leaf == root2_leaf:
            return True
        else:
            return False

    def dfs(self, root: TreeNode, leaf: 'List[int]'):
        if root is None:
            return
        if root.left is None and root.right is None:
            leaf.append(root.val)
        if root.left:
            self.dfs(root.left, leaf)
        if root.right:
            self.dfs(root.right, leaf)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    root.right = TreeNode(6)
    root.right.right = TreeNode(8)
    root.right.right.left = TreeNode(7)
    root.right.right.right = TreeNode(9)

    root2 = TreeNode(6)
    root2.left = TreeNode(7)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)
    root2.right = TreeNode(6)
    root2.right.right = TreeNode(8)
    root2.right.right.left = TreeNode(7)
    root2.right.right.right = TreeNode(9)
    print(s.leafSimilar(root, root2))
    '''
        5
       / \
      3   6
     / \    \
    2   4    8
   /        / \
  1        7   9


        6
       / \
      7   6
     / \    \
    2   4    8
   /        / \
  1        7   9
    '''