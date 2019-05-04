# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    preNum = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        self.convertBST(root.right)
        root.val += self.preNum
        self.preNum = root.val
        self.convertBST(root.left)
        return root

    # 右-根-左 的顺序遍历，并累加根结点的和
    def convertBST1(self, root: TreeNode) -> TreeNode:
        self.unpreOder(root)
        return root

    def unpreOder(self, node: TreeNode):
        if node is None:
            return
        self.unpreOder(node.right)
        node.val += self.preNum
        self.preNum = node.val
        self.unpreOder(node.left)

    # 非递归
    def convertBST2(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        stack = []
        node = root
        while node is not None or len(stack) != 0:
            while node is not None:
                stack.append(node)
                node = node.right
            node = stack.pop()
            node.val += self.preNum
            self.preNum = node.val

            if node.left is not None:
                node = node.left
            else:
                node = None
        return root
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
    root.left = TreeNode(2)
    root.right = TreeNode(13)
    node = s.convertBST(root)
    s.print_tree(node)
    '''
    输入: 二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13
    '''