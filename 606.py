# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
        res = str(t.val)
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)

        if left == '' and right == '':  # 如果左右字节点为空，直接返回
            return res
        elif left == '':  # 如果左节点为空，则需要为左节点添加空括号，然后括号+右子树
            res += '()' + '(' + right + ')'
        elif right == '':  # 如果右结点为空，则只需括号+左子树
            res += '(' + left + ')'
        else:  # 如果左右子树都不为空，则添加左右子树
            res += '(' + left + ')' + '(' + right + ')'
        return res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
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
    print(s.tree2str(root))