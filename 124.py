# Definition for a binary tree node.
import sys
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            # 左子树和右子树结点的最大和
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # 开始一个新的路径，node为最高结点
            price_newpath = node.val + left_gain + right_gain

            # 更新最大路径和
            max_sum = max(max_sum, price_newpath)

            # 递归，返回最大和或者继续更新原路径
            return node.val + max(left_gain, right_gain)
        max_sum = -sys.maxsize
        max_gain(root)
        return max_sum


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    '''
    示例: 
    给定如下二叉树

                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \      \
            7    2      1
    '''
    print(s.maxPathSum(root))