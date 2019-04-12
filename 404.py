# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:return 0
        if root.left and root.left.left is None and root.left.right is None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
    # 非递归
    def sumOfLeftLeaves2(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        queue = [root]
        sum_left = 0
        while queue:
            node = queue.pop(0)
            lnode = node.left
            if lnode and not lnode.left and not lnode.right:
                sum_left += lnode.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return sum_left

    def sumOfLeftLeaves(self, root: 'TreeNode') -> 'int':
        if root is None: return 0
        s = 0
        if root.left:
            if root.left.left is None and root.left.right is None:
                s += root.left.val
            else:
                s += self.sumOfLeftLeaves(root.left)
        if root.right:
            s += self.sumOfLeftLeaves(root.right)
        return s

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    '''
    示例: 
    给定如下二叉树

                   6
                 /   \
                2     8
               / \   / \
              0   4 7   9
                 / \      
                3   5    
    '''
    print(s.sumOfLeftLeaves(root))
