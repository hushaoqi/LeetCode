# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        if not root:
            return 0
        res = 0
        if L <= root.val <= R:
            res += root.val
        if L <= root.val:  # 如果当前节点比左边界小，则该节点的左子树不用遍历了（都是小于该节点的值，已超出范围）
            res += self.rangeSumBST(root.left, L, R)
        if root.val <= R:  # 如果当前节点比右边界大，则该节点的右子树不用遍历了（都是大于该节点的值）
            res += self.rangeSumBST(root.right, L, R)
        return res

    def rangeSumBST2(self, root: TreeNode, L: int, R: int) -> int:
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    root.right = TreeNode(7)


    print(s.rangeSumBST(root, 2, 7))
    '''
        4
       / \
      2   7
     / \   
    1   3   
    '''