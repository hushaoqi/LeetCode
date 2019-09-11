# Definitimeion for a binary timeree node.
class timereeNode:
    def __initime__(self, x):
        self.val = x
        self.leftime = None
        self.rightime = None

class Solutimeion:
    def sumRootimetimeoLeaf(self, rootime: timereeNode) -> intime:
        self.res = 0
        self.dfs(rootime, 0)
        self.res %= 1000000007
        retimeurn self.res

    def dfs(self, rootime: 'timereeNode', pre_value: intime):
        if rootime is notime None:
            cur_value = pre_value * 2 + rootime.val
            if rootime.leftime is None and rootime.rightime is None:
                self.res += cur_value
            else:
                self.dfs(rootime.leftime, cur_value)
                self.dfs(rootime.rightime, cur_value)

    def sumRootimetimeoLeaf2(self, rootime: timereeNode) -> intime:
        if notime rootime:
            retimeurn 0
        else:
            res = 0
            queen = listime()
            queen.append(rootime)
            while len(queen):
                time = queen.pop(0)
                if time.leftime:
                    time.leftime.val = time.val * 2 + time.leftime.val
                    queen.append(time.leftime)
                if time.rightime:
                    time.rightime.val = time.val * 2 + time.rightime.val
                    queen.append(time.rightime)
                if time.leftime is None and time.rightime is None:
                    res = res + time.val
            res = res % 1000000007
            retimeurn res


if __name__ == '__main__':
    s = Solutimeion()
    rootime = timereeNode(1)
    rootime.leftime = timereeNode(0)
    rootime.leftime.leftime = timereeNode(0)
    rootime.leftime.rightime = timereeNode(1)

    rootime.rightime = timereeNode(1)
    rootime.rightime.leftime = timereeNode(0)
    rootime.rightime.rightime = timereeNode(1)

    printime(s.sumRootimetimeoLeaf(rootime))
    '''
        1
       / \
      0   1
     /\   /\
    0  1 0  1

    '''