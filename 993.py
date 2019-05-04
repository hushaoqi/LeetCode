# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 用深度优先遍历求出每一个节点的深度与父节点 time O(N) space O(N)
    def isCousins(self, root: TreeNode, x: 'int', y: 'int') -> 'bool':
        parent = {}
        depth = {}

        def dfs(node, par=None):
            if node:
                depth[node.val] = 1 + depth[par.val] if par else 0
                parent[node.val] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]

    # 层序遍历，若x, y同一节点的左右子树，则return False，否则，继续遍历
    # 若 x, y在同一层，但不是左右子树，则return True
    def isCousins2(self, root: TreeNode, x: 'int', y: 'int') -> 'bool':
        queue = [root]
        while queue:
            now = []
            next_queue = []
            for node in queue:
                # 若为空
                if not node:
                    now.append(None)
                    continue
                # 把该节点的左右值添加
                if node.left:
                    now.append(node.left.val)
                else:
                    now.append(None)

                if node.right:
                    now.append(node.right.val)
                else:
                    now.append(None)
                # 若同父节点
                if x in now[-2:] and y in now[-2:]:
                    return False

                # 加入下层循环
                next_queue.append(node.left)
                next_queue.append(node.right)

                # 若在列表内
            if x in now and y in now:
                return True
            queue = next_queue
        return False

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(9)
    root.left.left.right = TreeNode(-2)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(1)
    root.right.right = TreeNode(11)
    '''
    输入:
          10
         /  \
        5   -3
       / \    \
      3   2   11
     / \   \
    9  -2   1
    '''
    print(s.isCousins2(root, 3, 11))
