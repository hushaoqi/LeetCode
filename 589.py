# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    # 递归法
    def preorder(self, root: 'Node') -> 'List[int]':
        res = []
        self.Ntree_preorder(root, res)
        return res

    def Ntree_preorder(self, node: Node, res: 'List[int]'):
        if node is None: return
        res.append(node.val)
        if node.children:  # 一定要判断是否为空，否则迭代器报错
            for child in node.children:
                self.Ntree_preorder(child, res)

    # 迭代法
    def preorder2(self, root: 'Node') -> 'List[int]':
        res = []
        if root is Node:return res
        queue = [root]
        while len(queue) != 0:
            node = queue.pop()
            res.append(node.val)
            temp = []
            if node.children:
                for child in node.children:
                    temp.append(child)
            temp.reverse()  # 由于是前序，所以要逆序
            queue.extend(temp)
        return res

if __name__ == '__main__':
    s = Solution()
    root = Node(1, [])
    node2_1 = Node(3, [])
    node2_2 = Node(2, None)
    node2_3 = Node(4, None)
    root.children.extend([node2_1, node2_2, node2_3])

    node3_1 = Node(5, None)
    node3_2 = Node(6, None)
    node2_1.children.extend([node3_1, node3_2])
    '''
            1
          / | \
         /  |  \
        /   |   \
       3    2    4
      / \
     /   \
    5     6
    '''
    print(s.preorder2(root))




