from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if root is None:return True
        return self.is_Symmetric(root.left, root.right)

    def is_Symmetric(self, left: 'TreeNode', right: 'TreeNode') -> 'bool':
        if left is None and right is None: return True
        if (left is not None and right is None) or (left is None and right is not None) or (left.val != right.val):
            return False
        return self.is_Symmetric(left.left, right.right) and self.is_Symmetric(left.right, right.left)

    # 迭代法实现，使用队
    def isSymmetric2(self, root: 'TreeNode') -> 'bool':
        qlist = []  # 本应左右子树用两个队列存储，但由于都是一对一对的比较，所以可以简化到一个队列中
        qlist.append(root.left)
        qlist.append(root.right)
        while len(qlist) != 0:
            t1 = qlist.pop()
            t2 = qlist.pop()
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            qlist.append(t1.left)
            qlist.append(t2.right)
            qlist.append(t1.right)
            qlist.append(t2.left)
        return True

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
    print(s.isSymmetric2(root))