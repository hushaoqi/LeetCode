# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 进行层序遍历
    def averageOfLevels(self, root: 'TreeNode') -> 'List[float]':
        stact = ans = []
        stact.append(root)
        while len(stact) != 0:
            size = len(stact)
            Sum = 0
            next_stact = []
            while len(stact) != 0:
                node = stact.pop()
                Sum += node.val
                if node.left is not None:
                    next_stact.append(node.left)
                if node.right is not None:
                    next_stact.append(node.right)

            ans.append(Sum / size)
            stact = next_stact
        return ans

    def averageOfLevels2(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        利用递归形式的先序遍历，但是根据判断当前层数level跟结果res中已经初始化的层数之间的关系对比，
        能把当前结点值累计到正确的位置，而且该层的结点数也自增1，这样我们分别求了两个数组，
        一个数组保存了每行的所有结点值，另一个保存了每行结点的个数，这样对应位相除就是我们要求的结果了
        """
        result = []

        def dfs(node, depth=0):
            if node:
                if len(result) <= depth:
                    result.append([0, 0])
                result[depth][0] += node.val
                result[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        dfs(root)
        return [s / float(v) for s, v in result]

    # 非递归形式
    def averageOfLevels3(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []

        if not root:
            return res.append(0.0)

        queue = []
        queue.append(root)

        while queue:
            tmp = 0
            length, temp = len(queue), len(queue)

            for i in range(length):
                value = queue.pop(0)
                tmp += value.val

                if value.left:
                    queue.append(value.left)
                if value.right:
                    queue.append(value.right)

            res.append(tmp / temp)

        return res

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    '''
    输入:
        3
       / \
      9  20
        /  \
       15   7
    输出: [3, 14.5, 11]
    '''
    print(s.averageOfLevels3(root))