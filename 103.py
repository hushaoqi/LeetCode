# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> 'List[List[int]]':
        res = []
        if root is None:
            return res
        queue = [root]
        flag = -1  # 锯齿，加一个标记变量flag
        while queue:
            n = len(queue)
            temp = []

            flag = -1 * flag  # 每遍历一层改变flag，即改变添加顺序
            while n > 0:
                node = queue.pop(0)
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                n -= 1
            if len(temp) != 0:
                if flag == -1:
                    temp = temp[::-1]
                res.append(temp)
        return res
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.zigzagLevelOrder(root))

