# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif p is not None and q is not None:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        else:
            return False
    # 非递归:迭代写法，相当于同时遍历两个数，然后每个节点都进行比较
    def isSameTree2(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        s1 = s2 = []
        if p:
            s1.append(p)
        if q:
            s2.append(q)
        while len(s1) != 0 and len(s2) != 0:
            node_p = s1.pop()
            node_q = s2.pop()
            if node_p.val != node_q: return False
            if node_p.left is not None:
                s1.append(node_p.left)
            if node_q.left is not None:
                s2.append(node_q.left)

            if len(s1) != len(s2):return False
            if node_p.right is not None:
                s1.append(node_p.right)
            if node_q.right is not None:
                s2.append(node_q.right)
            if len(s1) != len(s2):return False

        return len(s1) == len(s2)


if __name__=='__main__':
    s = Solution()
    '''
    输入:   1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

    输出: true
    '''
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    print(s.isSameTree(p, q))