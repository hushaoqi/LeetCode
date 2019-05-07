# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if (root.left is not None and root.val != root.left.val) or (root.right is not None and root.val != root.right.val):
            return False
        else:
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
    # 迭代法
    def isUnivalTree2(self, root: 'TreeNode') -> 'bool':
        node_list = list()
        node_list.append(root)
        val = None
        res = True
        while node_list:
            node = node_list.pop(0)
            if not val or node.val == val:
                val = node.val
                res = True
            else:
                res = False
                break
            if node.left:
                node_list.append(node.left)
            if node.right:
                node_list.append(node.right)
        return res

    # 用集合的不可重复性判断
    res = set()

    def isUnivalTree3(self, root: 'TreeNode') -> 'bool':
        if root is None: return True
        self.res.add(root.val)
        self.isUnivalTree3(root.left)
        self.isUnivalTree3(root.right)
        return len(self.res) == 1


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)

    root.right = TreeNode(1)


    print(s.isUnivalTree3(root))
    '''
        1
       / \
      1   1
     / \   
    1   1   
    '''