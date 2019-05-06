# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归，但不用新建树，将原树重排
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        root.right = self.increasingBST(root.right)
        if root.left:
            node = root.left
            root.left = None
            head = node
            while node.right:
                node = node.right
            node.right = root
            return self.increasingBST(head)
        else:
            return root

    # 递归遍历
    def increasingBST2(self, root: TreeNode) -> TreeNode:
        self.res = TreeNode(0)
        ans = self.res
        self.dfs(root)
        return ans.right

    def dfs(self, node: TreeNode):
        if node:
            self.dfs(node.left)
            self.res.right = TreeNode(node.val)
            self.res.left = None
            self.res = self.res.right
            self.dfs(node.right)
    # yield 优化
    def increasingBST3(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right

    # 非递归
    def increasingBST4(self, root: TreeNode) -> TreeNode:
        t = root
        tem = []
        head = None
        r = None
        while tem or t:
            if not t:
                t = tem.pop()
                if not head:
                    head = t
                    r = t
                else:
                    head.right = t
                    head = head.right
                    head.left = None
                t = t.right
            if t:
                tem.append(t)
                t = t.left
        return r
    # 打印树
    def print_tree(self, root: TreeNode):
        if root is not None:
            print(root.val, end=' ')
        if root.left:
            self.print_tree(root.left)
        if root.right:
            self.print_tree(root.right)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    root.right = TreeNode(6)
    root.right.right = TreeNode(8)
    root.right.right.left = TreeNode(7)
    root.right.right.right = TreeNode(9)
    s.print_tree(s.increasingBST(root))
    '''
        5
       / \
      3   6
     / \    \
    2   4    8
   /        / \
  1        7   9

    '''