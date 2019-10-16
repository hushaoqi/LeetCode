'''
           &
     a           b
  a     b     a    #
#  b  a  #  a  #  #  #

思路：
1、将a, b 放入一个二叉树中，左节点为a, 右节点为b
2、构建二叉树，同时根据a, b 的个数进行剪枝操作
3、中序遍历二叉树，记录访问的结点个数，即判断第K小，同时更新结点的路径
4、访问到第K个结点，即所求字符串，然后按照路径遍历得到字符串
'''
class Tree_node:
    def __init__(self, s):
        self.s = s
        self.left = None
        self.right = None

class Solution:
    def two_tree(self, root,  N, M):

        if N > 0:
            root.left = Tree_node("a")
            N -= 1

        if M > 0:
            root.right = Tree_node("b")
            M -= 1
        if N <= 0 and M <= 0:
            return root
        self.two_tree(root.left, N, M)
        self.two_tree(root.right, M, N)

    def findKthstr(self, K, path, count):
        if root == None or root.s == '&':
            return path
        path += self.findKthstr(K, path, count)
        path += root.s
        path += self.findKthstr(K, path, count)
if __name__=='__main__':
    T = Solution()
    N, M, K = map(int, input().split())  # a的数量N,b的数量M,字典序K小
    root = Tree_node("&")
    T.two_tree(root, N, M)
    # print(root.left.s)
    # print(root.right.s)
    # print(root.left.left.s)
    # print(root.left.right.s)
    path = ''
    count = 0
    T.findKthstr( K, path, count):
