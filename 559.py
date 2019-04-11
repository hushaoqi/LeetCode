# Definition for a Node.
#from treelib import Node
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:

    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        return 1 + max(self.maxDepth(child) for child in root.children)

# 非递归，层序遍历,需要借助队列
    def maxDepth2(self, root: 'Node') -> 'int':
        if root is None:return 0
        deep = 0
        queue = []
        queue.append(root)
        while len(queue) != 0:
            deep += 1
            n = len(queue)
            while n > 0:
                node = queue.pop(0)
                n -= 1
                # n 用来记录当前层的结点数
                if node.children is not None:
                    queue.extend(node.children)
        return deep

if __name__ == '__main__':
    s = Solution()
    root = Node(1, [])
    node2_1 = Node(3, [])
    node2_2 = Node(2, None)
    node2_3 = Node(4, None)
    root.children.extend([node2_1, node2_2, node2_3])

    node3_1 = Node(5, None)
    node3_2 = Node(5, None)
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
    print(s.maxDepth2(root))