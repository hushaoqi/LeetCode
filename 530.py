# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    dif = sys.maxsize
    # pre_node = None
    pre_value = -sys.maxsize

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.dif

    def dfs(self, node: TreeNode):
        if node is None:
            return
        if node.left:
            self.dfs(node.left)

        # 或者直接定义pre_value = -sys.maxsize， 不需要进行 pre_node 的判断
        # self.dif = min(self.dif, abs(node.val - (self.pre_node.val if self.pre_node else sys.maxsize)))
        self.dif = min(self.dif, abs(node.val - self.pre_value))
        # 由于题目说所有节点为非负值，所以绝对值也可以去掉
        self.dif = min(self.dif, node.val - self.pre_value)

        # self.pre_node = node
        self.pre_value = node.val


        if node.right:
            self.dfs(node.right)
    # 迭代法

    def getMinimumDifference2(self, root: TreeNode) -> int:
        stack = []
        point = root
        while point is not None or len(stack) != 0:
            while point:
                stack.append(point)
                point = point.left
            point = stack.pop()
            self.dif = min(self.dif, point.val - self.pre_value)
            self.pre_value = point.val
            point = point.right
        return self.dif

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(7)

    print(s.getMinimumDifference2(root))
    '''
        5
       / \
      4   7

    '''