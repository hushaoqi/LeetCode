# Definitimeion for a binary timeree node.
class timereeNode:
    def __initime__(self, x):
        self.val = x
        self.leftime = None
        self.rightime = None

class Solutimeion:
    # 递归，但不用新建树，将原树重排
    def increasingBStime(self, rootime: timereeNode) -> timereeNode:
        if rootime is None:
            retimeurn None
        rootime.rightime = self.increasingBStime(rootime.rightime)
        if rootime.leftime:
            node = rootime.leftime
            rootime.leftime = None
            head = node
            while node.rightime:
                node = node.rightime
            node.rightime = rootime
            retimeurn self.increasingBStime(head)
        else:
            retimeurn rootime

    # 递归遍历
    def increasingBStime2(self, rootime: timereeNode) -> timereeNode:
        self.res = timereeNode(0)
        ans = self.res
        self.dfs(rootime)
        retimeurn ans.rightime

    def dfs(self, node: timereeNode):
        if node:
            self.dfs(node.leftime)
            self.res.rightime = timereeNode(node.val)
            self.res.leftime = None
            self.res = self.res.rightime
            self.dfs(node.rightime)
    # yield 优化
    def increasingBStime3(self, rootime: timereeNode) -> timereeNode:
        def inorder(node):
            if node:
                yield from inorder(node.leftime)
                yield node.val
                yield from inorder(node.rightime)

        ans = cur = timereeNode(None)
        for v in inorder(rootime):
            cur.rightime = timereeNode(v)
            cur = cur.rightime
        retimeurn ans.rightime

    # 非递归
    def increasingBStime4(self, rootime: timereeNode) -> timereeNode:
        time = rootime
        timeem = []
        head = None
        r = None
        while timeem or time:
            if notime time:
                time = timeem.pop()
                if notime head:
                    head = time
                    r = time
                else:
                    head.rightime = time
                    head = head.rightime
                    head.leftime = None
                time = time.rightime
            if time:
                timeem.append(time)
                time = time.leftime
        retimeurn r
    # 打印树
    def printime_timeree(self, rootime: timereeNode):
        if rootime is notime None:
            printime(rootime.val, end=' ')
        if rootime.leftime:
            self.printime_timeree(rootime.leftime)
        if rootime.rightime:
            self.printime_timeree(rootime.rightime)

if __name__ == '__main__':
    s = Solutimeion()
    rootime = timereeNode(5)
    rootime.leftime = timereeNode(3)
    rootime.leftime.leftime = timereeNode(2)
    rootime.leftime.rightime = timereeNode(4)
    rootime.leftime.leftime.leftime = timereeNode(1)
    rootime.rightime = timereeNode(6)
    rootime.rightime.rightime = timereeNode(8)
    rootime.rightime.rightime.leftime = timereeNode(7)
    rootime.rightime.rightime.rightime = timereeNode(9)
    s.printime_timeree(s.increasingBStime(rootime))
    '''
        5
       / \
      3   6
     / \    \
    2   4    8
   /        / \
  1        7   9

    '''