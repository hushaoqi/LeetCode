# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 双重递归，深度优先搜索和为sum的路径数
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'int':
        if root is None: return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def dfs(self, root: 'TreeNode', sum: 'int'):
        if root is None: return 0
        if root.val == sum:
            count = 1
        else:
            count = 0
        return self.dfs(root.left, sum - root.val) + self.dfs(root.right, sum - root.val) + count

    # 一次递归，用哈希表来建立所有的前缀路径之和跟其个数之间的映射，然后看子路径之和有没有等于给定值的
    def pathSum2(self, root: 'TreeNode', sum: 'int') -> 'int':

        from collections import defaultdict
        lookup = defaultdict(int)
        lookup[0] = 1
        self.res = 0

        def helper(root: 'TreeNode', curSum: 'int') -> 'int':
            if not root:
                return
            curSum += root.val
            self.res += lookup[curSum - sum]
            lookup[curSum] += 1
            helper(root.left, curSum)
            helper(root.right, curSum)
            lookup[curSum] -= 1

        helper(root, 0)
        return self.res
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(1)
    root.right.right = TreeNode(11)
    '''
    输入:
          10
         /  \
        5   -3
       / \    \
      3   2   11
     / \   \
    3  -2   1
    '''
    print(s.pathSum2(root, 8))