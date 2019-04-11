# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:return 0
        if root.left is None:return 1 + self.minDepth(root.right)
        if root.right is None:return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    # 迭代来做，层序遍历，记录遍历的层数，一旦我们遍历到第一个叶结点，就将当前层数返回，即为二叉树的最小深度
    def minDepth2(self, root: TreeNode) -> int:
        if root is None: return 0
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
                # 遍历到第一个叶子结点，则当前深度为最小深度
                if node.left is None and node.right is None:
                    return deep
                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    #root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    #root.right.left = TreeNode(4)
    #root.right.right = TreeNode(3)
    '''
    输入:
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    '''
    print(s.minDepth2(root))