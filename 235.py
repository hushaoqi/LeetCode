# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    由于二叉搜索树的特点是左<根<右，所以根节点的值一直都是中间值，
    大于左子树的所有节点值，小于右子树的所有节点值，那么我们可以做如下的判断，
    如果根节点的值大于p和q之间的较大值，说明p和q都在左子树中，
    那么此时我们就进入根节点的左子节点继续递归，如果根节点小于p和q之间的较小值，
    说明p和q都在右子树中，那么此时我们就进入根节点的右子节点继续递归，
    如果都不是，则说明当前根节点就是最小共同父节点，直接返回即可
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None: return
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        return root

    # 非递归的写法，用个while循环来代替递归调用
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if root.val > max(p.val, q.val):
                root = root.left
            elif root.val < min(p.val, q.val):
                root = root.right
            else:break
        return root

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
    print(s.lowestCommonAncestor2(root, root.left, root.left.right).val)