# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 首先来计数需要构建的二叉树数量。可能的二叉搜素数数量是一个 卡特兰数。
class Solution:
    def generateTrees(self, n: int) -> 'List[TreeNode]':
        def generate_trees(start, end):
            if start > end:
                return [None,]
            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate_trees(start, i-1)
                right_trees = generate_trees(i+1, end)
                for lt in left_trees:
                    for rt in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = lt
                        current_tree.right = rt
                        all_trees.append(current_tree)
            return all_trees
        return generate_trees(1, n) if n else []

if __name__=='__main__':
    s = Solution()
    while True:
        n = input().strip()
        if len(n) == 0:
            break
        else:
            print(s.generateTrees(int(n)))