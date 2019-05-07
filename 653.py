# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    def findTarget(self, root: TreeNode, k: int) -> bool:
        table = {}
        return self.dfs(root, table, k)

    def dfs(self, root: TreeNode, table: 'dict', target: 'int')->bool:
        if root is None:
            return False

        if target - root.val in table:
            return True

        if root.val not in table:
            table[root.val] = 1
        else:
            table[root.val] += 1

        return self.dfs(root.left, table, target) or self.dfs(root.right, table, target)

    # 非递归

    def findTarget2(self, root: TreeNode, k: int) -> bool:
        table = set()
        stack = [root]
        while len(stack) != 0:
            node = stack.pop(0)
            if k - node.val in table:
                return True
            table.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False

    # 上面两种方法好像都没有用到二次搜索数的性质，但是应该怎么改呢？
    # 这样似乎是为了利用性质而利用，性能并没有比上面的好
    def findTarget3(self, root: TreeNode, k: int) -> bool:
        self.table = []
        self.dfs2(root)
        print(self.table)
        i = 0
        j = len(self.table)-1
        while i < j:
            if self.table[i] + self.table[j] == k:
                return True
            if self.table[i] + self.table[j] < k:
                i += 1
            else:
                j -= 1
        return False


    def dfs2(self, root: TreeNode):
        if root is None:
            return
        if root.left:
            self.dfs2(root.left)

        self.table.append(root.val)

        if root.right:
            self.dfs2(root.right)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    root.right = TreeNode(6)
    root.right.right = TreeNode(7)

    target = 6
    print(s.findTarget3(root, target))
    '''
        5
       / \
      3   6
     / \    \
    2   4    7
 
'''