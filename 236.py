# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic = {root: None}

        def bfs(node):
            if node:
                if node.left: dic[node.left] = node
                if node.right: dic[node.right] = node
                bfs(node.left)
                bfs(node.right)

        bfs(root)
        l1, l2 = p, q
        while (l1 != l2):
            l1 = dic.get(l1) if l1 else q
            l2 = dic.get(l2) if l2 else p
        return l1


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    '''
    示例: 
    给定如下二叉搜索树

                   6
                 /   \
                2     8
               / \   / \
              0   4 7   9
                 / \      
                3   5    
    '''
    print(s.lowestCommonAncestor(root, root.left, root.left.right).val)