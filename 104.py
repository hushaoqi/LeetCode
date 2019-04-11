# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归法
    def maxDepth(self, root: 'TreeNode') -> 'int':
        if root is None:return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

    # 非递归，层序遍历,需要借助队列
    def maxDepth2(self, root: 'TreeNode') -> 'int':
        if root is None:return 0
        deep = 0
        queue = []
        queue.append(root)
        while len(queue) != 0:
            deep += 1
            n = len(queue)
            while n > 0:
                node = queue.pop(0)
                n -= 1
                # n 用来记录当前层的结点数
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return deep


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
    print(s.maxDepth2(root))