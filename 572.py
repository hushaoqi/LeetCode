# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Recursive formulae can be:
    # isIdentical(s,t)= s.val==t.val AND isIdentical(s.left,t.left) AND isIdentical(s.right,t.right)
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return False
        if self.isIdentical(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isIdentical(self, s:TreeNode, t: TreeNode)->bool:
        if not s and not t:  # t 遍历完
            return True
        if not s or not t:  # 有一个没有遍历完
            return False

        if s.val != t.val:
            return False
        return self.isIdentical(s.left, t.left) and self.isIdentical(s.right, t.right)

    # 606题：https://blog.csdn.net/hushaoqiqimingxing/article/details/89445358
    # 采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。
    # 如果t的字符串是s的子串的话，就说明t是s的子树
    def isSubtree2(self, s: TreeNode, t: TreeNode) -> bool:
        s_tree = self.tree2str(s)
        t_tree = self.tree2str(t)
        # print(s_tree)
        # print(t_tree)
        # 如果是子串，则返回index，如果不是子串，则返回-1
        index = s_tree.find(t_tree)
        if index == -1:
            return False
        else:
            return True

    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
        # 需要注意的是，为了避免出现[12], [2], 这种情况，虽然2也是12的子串，
        # 但是[2]却不是[12]的子树，所以我们再序列化的时候要特殊处理一下，
        # 就是在每个结点值前面都加上一个字符，用()来分隔开，那么[12]
        # 序列化后就是"(12)()()"，而[2]序列化之后就是(2)()()"
        res = '(' + str(t.val) + ')'
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)

        # 注意：这里当结点为叶结点的时候，一定要加空括号，避免下面图示这种情况
        if left == '' and right == '':  # 如果左右字节点为空，两个空括号
            res += '()()'
            return res
        elif left == '':  # 如果左节点为空，则需要为左节点添加空括号，然后空括号+右子树
            res += '()' + '(' + right + ')'
        elif right == '':  # 如果右结点为空，则括号+左子树+空括号
            res += '(' + left + ')' + '()'
        else:  # 如果左右子树都不为空，则添加左右子树
            res += '(' + left + ')' + '(' + right + ')'
        return res

'''
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：

   4
  / \
 1   2
'''

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(0)
    root.right = TreeNode(5)

    node = TreeNode(4)
    node.left = TreeNode(1)
    node.right = TreeNode(2)
    print(s.isSubtree2(root, node))
    '''
    给定的树 s:
    
         3
        / \
       4   5
      / \
     1   2
    给定的树 t：
    
       4 
      / \
     1   2
    返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。
    '''