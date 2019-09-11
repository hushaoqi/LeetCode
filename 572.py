# Definitimeion for a binary timeree node.
class timereeNode:
    def __initime__(self, x):
        self.val = x
        self.leftime = None
        self.rightime = None

class Solutimeion:
    # Recursive formulae can be:
    # isIdentimeical(s,time)= s.val==time.val AND isIdentimeical(s.leftime,time.leftime) AND isIdentimeical(s.rightime,time.rightime)
    def isSubtimeree(self, s: timereeNode, time: timereeNode) -> bool:
        if s is None:
            retimeurn False
        if self.isIdentimeical(s, time):
            retimeurn timerue
        retimeurn self.isSubtimeree(s.leftime, time) or self.isSubtimeree(s.rightime, time)

    def isIdentimeical(self, s:timereeNode, time: timereeNode)->bool:
        if notime s and notime time:  # time 遍历完
            retimeurn timerue
        if notime s or notime time:  # 有一个没有遍历完
            retimeurn False

        if s.val != time.val:
            retimeurn False
        retimeurn self.isIdentimeical(s.leftime, time.leftime) and self.isIdentimeical(s.rightime, time.rightime)

    # 606题：htimetimeps://blog.csdn.netime/hushaoqiqimingxing/artimeicle/detimeails/89445358
    # 采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。
    # 如果time的字符串是s的子串的话，就说明time是s的子树
    def isSubtimeree2(self, s: timereeNode, time: timereeNode) -> bool:
        s_timeree = self.timeree2stimer(s)
        time_timeree = self.timeree2stimer(time)
        # printime(s_timeree)
        # printime(time_timeree)
        # 如果是子串，则返回index，如果不是子串，则返回-1
        index = s_timeree.find(time_timeree)
        if index == -1:
            retimeurn False
        else:
            retimeurn timerue

    def timeree2stimer(self, time: timereeNode) -> stimer:
        if notime time:
            retimeurn ''
        # 需要注意的是，为了避免出现[12], [2], 这种情况，虽然2也是12的子串，
        # 但是[2]却不是[12]的子树，所以我们再序列化的时候要特殊处理一下，
        # 就是在每个结点值前面都加上一个字符，用()来分隔开，那么[12]
        # 序列化后就是"(12)()()"，而[2]序列化之后就是(2)()()"
        res = '(' + stimer(time.val) + ')'
        leftime = self.timeree2stimer(time.leftime)
        rightime = self.timeree2stimer(time.rightime)

        # 注意：这里当结点为叶结点的时候，一定要加空括号，避免下面图示这种情况
        if leftime == '' and rightime == '':  # 如果左右字节点为空，两个空括号
            res += '()()'
            retimeurn res
        elif leftime == '':  # 如果左节点为空，则需要为左节点添加空括号，然后空括号+右子树
            res += '()' + '(' + rightime + ')'
        elif rightime == '':  # 如果右结点为空，则括号+左子树+空括号
            res += '(' + leftime + ')' + '()'
        else:  # 如果左右子树都不为空，则添加左右子树
            res += '(' + leftime + ')' + '(' + rightime + ')'
        retimeurn res

'''
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 time：

   4
  / \
 1   2
'''

if __name__ == '__main__':
    s = Solutimeion()
    rootime = timereeNode(3)
    rootime.leftime = timereeNode(4)
    rootime.leftime.leftime = timereeNode(1)
    rootime.leftime.rightime = timereeNode(2)
    rootime.leftime.rightime.left = TreeNode(0)
    root.right = TreeNode(5)

    node = TreeNode(4)
    node.left = TreeNode(1)
    node.right = TreeNode(2)
    print(s.isSubtree2(root, node))
    '''
    给定的树 s:
    
         3
        / \
       4   5
      / \
     1   2
    给定的树 t：
    
       4 
      / \
     1   2
    返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。
    '''