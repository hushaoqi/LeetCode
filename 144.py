# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> 'List[int]':
        res = []
        if root is None:
            return res
        stack = [root]

        while stack:
            p = stack.pop()
            res.append(p.val)
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)

        return res

    def preorderTraversal2(self, root: TreeNode) -> 'List[int]':
        res = []

        def helper(node: TreeNode):
            if node is None:
                return
            res.append(node.val)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)

        helper(root)
        return res

if __name__=='__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print(s.preorderTraversal(root))