# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    # 迭代法
    def invertTree2(self, root: TreeNode) -> TreeNode:
        if root is None:return
        queue = [root]
        while len(queue) != 0:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:queue.append(node.left)
            if node.right:queue.append(node.right)
        return root

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
    s.invertTree2(root)