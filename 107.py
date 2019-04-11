# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 层序遍历，头插法
    def levelOrderBottom(self, root: 'TreeNode') -> 'List[List[int]]':
        if root is None:return []
        res = [[root.val]]
        queue = []
        queue.append(root)
        while len(queue) != 0:
            n = len(queue)
            flag = False  # 以防加入空level
            level = []
            while n > 0:
                node = queue.pop(0)
                n -= 1
                if node.left is not None:
                    level.append(node.left.val)
                    queue.append(node.left)
                    flag = True
                if node.right is not None:
                    level.append(node.right.val)
                    queue.append(node.right)
                    flag = True
            if flag:
                res.insert(0, level)
        return res

    # 递归解法
    def levelOrderBottom2(self, root: 'TreeNode') -> 'List[List[int]]':
        res = []
        self.level_order(root, -1, res)
        return res
    def level_order(self, node: 'TreeNode', level: 'int', res: 'List[List[int]]'):
        if node is None:return
        # 超出递归的长度表明是新的一层，则新添加数组
        if level < 0 and abs(level) > len(res):
            res.insert(0, [])

        # 可以理解成每个node都能对应到树的level
        res[level].append(node.val)
        if node.left is not None:
            self.level_order(node.left, level-1, res)
        if node.right is not None:
            self.level_order(node.right, level-1, res)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
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
    print(s.levelOrderBottom2(root))

