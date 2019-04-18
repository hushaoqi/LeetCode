# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 由于叶子结点的坡度为0，根结点的坡度为左右结点各自的和之差，所以符合后序遍历的特点
    # 注意这里采用列表res[0]，可变对象作为“传址调用”或者用"self.res"
    def findTilt(self, root: TreeNode) -> int:
        res = [0]
        self.post_order_trans(root, res)
        return res[0]

    def post_order_trans(self, node: 'TreeNode', res: 'List[int]')->'int':
        if node is None:return 0
        left_sum = self.post_order_trans(node.left, res)
        right_sum = self.post_order_trans(node.right, res)
        res[0] += abs(left_sum - right_sum)
        print('(',left_sum, right_sum,left_sum + right_sum + node.val, res[0], ')', end= ' ')
        return left_sum + right_sum + node.val


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
    print(s.findTilt(root))
