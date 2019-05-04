# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # res = []
    # count = {}
    '''
    直接点思路就是利用一个哈希表来记录数字和其出现次数之前的映射，
    然后维护一个变量mx来记录当前最多的次数值，这样在遍历完树之后，
    根据这个mx值就能把对应的元素找出来。
    那么用这种方法的话就不需要用到二分搜索树的性质了，随意一种遍历方式都可以
    '''
    def findMode(self, root: TreeNode) -> 'List[int]':
        if root is None:
            return []
        # 之前将下面两个初始化放在了Solution类里面，结果oj连续测试时，保存了上一次测试的结果，因此没通过；
        res = []
        count = {}
        self.midOder(root, count)
        cont = max(count.values())
        for k in count.keys():
            if count[k] == cont:
                res.append(k)
        return res


    def midOder(self, root: TreeNode, count:dict) -> TreeNode:
        if root is None:
            return root

        if root.left:
            self.midOder(root.left, count)

        if root.val not in count:
            count[root.val] = 1
        else:
            count[root.val] += 1

        if root.right:
            self.midOder(root.right, count)

    # 非递归
    def findMode2(self, root: TreeNode) -> 'List[int]':

        if not root: return []
        d = {root.val: 1}

        stack = [root]

        while stack:
            node = stack.pop()
            # print(node.val)
            if node.left:
                if node.left.val in d:
                    d[node.left.val] += 1
                else:
                    d[node.left.val] = 1
                stack.append(node.left)
            # print(stack, d)
            if node.right:
                if node.right.val in d:
                    d[node.right.val] += 1
                else:
                    d[node.right.val] = 1
                stack.append(node.right)

        mode = sorted(d.items(), key=lambda d: d[1])[-1][1]

        return [x for x in d if d[x] == mode]

    '''
    不用除了递归中的隐含栈之外的额外空间，那么我们就不能用哈希表了，
    二分搜索树，那么我们中序遍历出来的结果就是有序的，这样我们只要比较前后两个元素是否相等，
    就等统计出现某个元素出现的次数，因为相同的元素肯定是都在一起的。
    '''

    def findMode3(self, root: 'TreeNode') -> 'List[int]':
        res = []
        self.mx = 0  # 最大相同节点个数
        self.cnt = 0  # 当前相同节点个数
        self.pre = None
        self.inorder(root, res)
        return res

    def inorder(self, root, res: list):
        if not root:
            return
        self.inorder(root.left, res)

        if self.pre:
            self.cnt = self.cnt + 1 if (self.pre.val == root.val) else 1
        else:
            self.cnt = 1

        if self.cnt >= self.mx:
            if self.cnt > self.mx:
                res.clear()
            res.append(root.val)
            self.mx = self.cnt

        self.pre = root
        self.inorder(root.right, res)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(4)
    root.right = TreeNode(7)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(8)
    print(s.findMode3(root))
    '''
    5
   / \
  4   7
 /   /  \
4   7    8
    '''