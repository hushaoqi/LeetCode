# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 递归求每个节点的深度，然后递归遍历左右子树的深度差
    def isBalanced(self, root: 'TreeNode') -> 'bool':
        if root is None: return True
        if abs(self.get_depth(root.left) - self.get_depth(root.right)) > 1:return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_depth(self, root: 'TreeNode') -> 'int':
        if root is None: return 0
        return 1 + max(self.get_depth(root.left), self.get_depth(root.right))

    # 上面那个方法正确但不是很高效，因为每一个点都会被上面的点计算深度时访问一次，我们可以进行优化。
    # 方法是如果我们发现子树不平衡，则不计算具体的深度，而是直接返回-1。
    def isBalanced2(self, root: 'TreeNode') -> 'bool':
        if self.check_depth(root) == -1:return False
        else:return True

    def check_depth(self, root: 'TreeNode') -> 'int':
        if root is None: return 0
        left = self.check_depth(root.left)
        if left == -1:return -1
        right = self.check_depth(root.right)
        if right == -1:return -1

        diff = abs(left - right)
        if diff > 1:return -1
        else:return 1 + max(left, right)

    def isBalanced3(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def balanced(root):
            if not root:
                return 0
            left = balanced(root.left)
            right = balanced(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return balanced(root) != -1

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
    print(s.isBalanced2(root))