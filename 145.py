# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> 'List[int]':
        res = []

        def helper(node: TreeNode):
            if node is None:
                return res
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            res.append(node.val)
        helper(root)

        return res
    # “根->右->左”然后reverse
    def postorderTraversal2(self, root: TreeNode) -> 'List[int]':
        res = []
        if root is None:
            return res
        stack = [root]
        while stack:
            p = stack.pop()
            res.append(p.val)
            if p.left:
                stack.append(p.left)
            if p.right:
                stack.append(p.right)
        res = res[::-1]
        return res

if __name__=='__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print(s.postorderTraversal(root))
