# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    # 递归
    def postorder(self, root: 'Node') -> 'List[int]':
        res = []
        self.Ntree_posoder(root, res)
        return res
    def Ntree_posoder(self, node :'Node', res: 'List[int]'):
        if node:
            if node.children:
                for child in node.children:
                    self.Ntree_posoder(child, res)
            # 先处理孩子，再处理根节点

            res.append(node.val)

    # 非递归
    def postorder2(self, root: 'Node') -> 'List[int]':
        res = []
        if root is Node:
            return res
        stack = [root]
        while len(stack) != 0:
            node = stack.pop()
            if node:
                res.append(node.val)
                if node.children:
                    for child in node.children:
                        stack.append(child)
        res.reverse()  # 将前序逆序，即为后序
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
    print(s.postorder2(root))
