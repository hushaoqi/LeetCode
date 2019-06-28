# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> 'List[List[int]]':
        res = []
        if root is None:
            return res
        queue = [root]

        while queue:
            n = len(queue)
            temp = []
            while n > 0:
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                n -= 1
            if len(temp) != 0:
                res.append(temp)
        return res

if __name__=='__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print(s.levelOrder(root))

