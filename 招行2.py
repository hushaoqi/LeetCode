# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> TreeNode:
        assert len(preorder) == len(inorder)
        size = len(preorder)

        self.preorder = preorder
        self.inorder = inorder
        return self.__dfs(0, size - 1, 0, size - 1)

    def __dfs(self, pre_l, pre_r, in_l, in_r):
        if pre_l > pre_r or in_l > in_r:
            return None
        val = self.preorder[pre_l]  # 前序遍历的第一结点就是根结点
        root = TreeNode(val)
        # 在中序遍历中找到根结点的索引，得到左右子树的划分
        pos = self.inorder.index(val)
        root.left = self.__dfs(pre_l + 1, pre_l + pos - in_l+1, in_l, pos - 1)
        root.right = self.__dfs(pre_r + pos - in_r+1, pre_r, pos + 1, in_r)
        return root
if __name__=="__main__":
    s = Solution()
    # 前序遍历
    preorder = [3, 9, 20, 15, 7]
    # 中序遍历
    inorder = [9, 3, 15, 20, 7]
    root = s.buildTree(preorder, inorder)
