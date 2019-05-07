# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, 0)
        self.res %= 1000000007
        return self.res

    def dfs(self, root: 'TreeNode', pre_value: int):
        if root is not None:
            cur_value = pre_value * 2 + root.val
            if root.left is None and root.right is None:
                self.res += cur_value
            else:
                self.dfs(root.left, cur_value)
                self.dfs(root.right, cur_value)

    def sumRootToLeaf2(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            res = 0
            queen = list()
            queen.append(root)
            while len(queen):
                t = queen.pop(0)
                if t.left:
                    t.left.val = t.val * 2 + t.left.val
                    queen.append(t.left)
                if t.right:
                    t.right.val = t.val * 2 + t.right.val
                    queen.append(t.right)
                if t.left is None and t.right is None:
                    res = res + t.val
            res = res % 1000000007
            return res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)

    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)

    print(s.sumRootToLeaf(root))
    '''
        1
       / \
      0   1
     /\   /\
    0  1 0  1

    '''