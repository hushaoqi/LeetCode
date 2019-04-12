# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 一层一层的在原有层上添加
    def binaryTreePaths(self, root: TreeNode) -> 'List[str]':
        if not root:
            return []
        paths = []
        if not root.left and not root.right:
            return [str(root.val)]
        if root.left:
            for string in self.binaryTreePaths(root.left):
                paths.append(str(root.val) + '->' + string)
        if root.right:
            for string in self.binaryTreePaths(root.right):
                paths.append(str(root.val) + '->' + string)
        return paths

    # 深度优先搜索，然后回溯，这里结果result需要reference，而path是不需要引用的，不然回溯回去还要删除新添加的结点，很麻烦。

    def binaryTreePaths2(self, root: TreeNode) -> 'List[str]':
        global result
        if not root:
            return []
        result = []
        self.binaryTreePath(root, '', result)
        return result

    # DFS
    def binaryTreePath(self, root: 'TreeNode', path: 'str', result: 'List[str]'):
        if not root.left and not root.right:
            result.append(path + str(root.val))
        if root.left:
            self.binaryTreePath(root.left, path + str(root.val) + '->', result)
        if root.right:
            self.binaryTreePath(root.right, path + str(root.val) + '->', result)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    '''
    示例: 
    给定如下二叉树

                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \      \
            7    2      1
    '''
    print(s.binaryTreePaths2(root))