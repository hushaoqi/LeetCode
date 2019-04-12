# Definition for a Node.
from collections import deque
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    # 利用队，层序遍历
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        if root is None:return []
        res = [[root.val]]
        queue = [root]
        while queue:
            n = len(queue)
            level = []
            flag = False# 判断是否为空层
            while n > 0:
                node = queue.pop(0)
                n -= 1
                if node.children:
                    for child in node.children:
                        level.append(child.val)

                    # for i in range(len(node.children)):
                    #     level.append(node.children[i].val)

                    queue.extend(node.children)
                    flag = True
            if flag:
                res.append(level)
        return res

    # 递归解法
    def levelOrder2(self, root: 'Node') -> 'List[List[int]]':
        res = []
        self.trans_Tree(root, 0, res)
        return res

    def trans_Tree(self, node: 'Node', level: 'int', res: 'List[List[int]]'):
        '''
            注意，res是传址调用，由于Python中不存在参数传址和传值调用，Python参数传递全部是都是对象地址引用
            但是存在区别：
            对于可变对象（列表，字典），可以改变原参数的值，相当于传址
            对于不可变对象（数字，字符串，元祖），不会改变原参数，相当于传值
        '''

        if node is None:return
        if len(res) <= level:
            res.append([])
        res[level].append(node.val)
        if node.children:
            for child in node.children:
                self.trans_Tree(child, level + 1, res)

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
    print(s.levelOrder2(root))
