# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归法
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:return False
        if root.left is None and root.right is None and sum == root.val:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    # 迭代法
    def hasPathSum2(self, root: TreeNode, sum: int) -> bool:
        if root is None:return False
        stact = [root]
        while len(stact) != 0:
            t = stact.pop()
            if t.left is None and t.right is None and sum == t.val:
                return True
            if t.left is not None:
                t.left.val += t.val
                stact.append(t.left)
            if t.right is not None:
                t.right.val += t.val
                stact.append(t.right)
        return False

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
    给定如下二叉树，以及目标和 sum = 22，
    
                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \      \
            7    2      1
    返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
    '''
    print(s.hasPathSum2(root, 22))