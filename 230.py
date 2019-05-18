# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """ 利用堆栈中序遍历"""
        # if root == None:
        #     return False
        count = 0
        stack = []
        node = root
        while node or stack:
            while node:  # 从根结点开始，寻找左子树，把它压入栈中
                stack.append(node)
                node = node.left
            node = stack.pop()  # while 结束代表前一个节点没有了左子树
            count += 1
            if count == k:
                return node.val
            # print(node.val, end=' ')
            node = node.right  # 然后开始寻找右子树

    # 分治法
    '''
    由于BST的性质，我们可以快速定位出第k小的元素是在左子树还是右子树，
    我们首先计算出左子树的结点个数总和cnt，如果k小于等于左子树结点总和cnt，
    说明第k小的元素在左子树中，直接对左子结点调用递归即可。如果k大于cnt+1，
    说明目标值在右子树中，对右子结点调用递归函数，
    注意此时的k应为k-cnt-1，应为已经减少了cnt+1个结点。
    如果k正好等于cnt+1，说明当前结点即为所求，返回当前结点值即可
    '''
    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        def count(node: 'TreeNode'):
            if node is None:
                return 0
            return 1 + count(node.left) + count(node.right)
        cnt = count(root.left)
        if k <= cnt:
            return self.kthSmallest2(root.left, k)
        elif k > cnt + 1:
            return self.kthSmallest2(root.right, k - cnt - 1)
        return root.val

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)


    '''
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3   
    '''
    print(s.kthSmallest2(root, k=5))