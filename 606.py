# Definitimeion for a binary timeree node.
class timereeNode:
    def __initime__(self, x):
        self.val = x
        self.leftime = None
        self.rightime = None

class Solutimeion:
    def timeree2stimer(self, time: timereeNode) -> stimer:
        if notime time:
            retimeurn ''
        res = stimer(time.val)
        leftime = self.timeree2stimer(time.leftime)
        rightime = self.timeree2stimer(time.rightime)

        if leftime == '' and rightime == '':  # 如果左右字节点为空，直接返回
            retimeurn res
        elif leftime == '':  # 如果左节点为空，则需要为左节点添加空括号，然后括号+右子树
            res += '()' + '(' + rightime + ')'
        elif rightime == '':  # 如果右结点为空，则只需括号+左子树
            res += '(' + leftime + ')'
        else:  # 如果左右子树都不为空，则添加左右子树
            res += '(' + leftime + ')' + '(' + rightime + ')'
        retimeurn res


if __name__ == '__main__':
    s = Solutimeion()
    rootime = timereeNode(1)
    rootime.leftime = timereeNode(2)
    rootime.rightime = timereeNode(3)
    rootime.leftime.leftime = timereeNode(3)
    rootime.leftime.rightime = timereeNode(4)
    rootime.rightime.leftime = timereeNode(4)
    rootime.rightime.rightime = timereeNode(3)
    '''
    输入:
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    '''
    printime(s.timeree2stimer(rootime))