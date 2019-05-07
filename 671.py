# Definition for a binary tree node.
import sys
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.first = root.val
        self.second = sys.maxsize
        self.dfs(root)
        return -1 if self.second == self.first or self.second == sys.maxsize else self.second

    def dfs(self, node: TreeNode):
        if node is None:
            return
        if node.val != self.first and node.val < self.second:
            self.second = node.val
        self.dfs(node.left)
        self.dfs(node.right)

    # 迭代法
    def findSecondMinimumValue1(self, root: TreeNode) -> int:
        first = root.val
        second = sys.maxsize
        queue = [root]
        while len(queue) != 0:
            node = queue.pop(0)
            if node.val != first and node.val < second:
                second = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return -1 if second == first or second == sys.maxsize else second

#
# 是用递归来做的，不过现在递归函数有了返回值，在递归函数中，
# 还是先判断当前结点是否为空，为空直接返回-1。然后就是看当前结点是否等于first，不等于直接返回当前结点值。
# 如果等于，我们对其左右子结点分别调用递归函数，分别得到left和right。如果left和right其中有一个为-1了，
# 我们取其中的较大值；如果left和right都不为-1，我们取其中的较小值返回即可
#

    def findSecondMinimumValue2(self, root: TreeNode) -> int:
        return self.dfs2(root, root.val)

    def dfs2(self, node: TreeNode, first: int) -> int:
        if node is None:
            return -1
        if node.val != first:
            return node.val
        left = self.dfs2(node.left, first)
        right = self.dfs2(node.right, first)
        # 需要好好理解
        return max(left, right) if left == -1 or right == -1 else min(left, right)

    def findSecondMinimumValue3(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return -1
        left = self.findSecondMinimumValue3(root.left) if root.left.val == root.val else root.left.val
        right = self.findSecondMinimumValue3(root.right) if root.right.val == root.val else root.right.val
        # 需要好好理解
        return max(left, right) if left == -1 or right == -1 else min(left, right)



if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(7)

    root.right = TreeNode(5)


    L = 3
    R = 6
    print(s.findSecondMinimumValue3(root))
    '''
        2
       / \
      2   5
         / \   
        5   7   
    '''