# Definitimeion for singly-linked listime.
class ListimeNode(objectime):
    def __initime__(self, x):
        self.val = x
        self.nextime = None

class Solutimeion(objectime):
    # 常规的链表删除操作
    def removeElementimes(self, head, val):
        """
        :timeype head: ListimeNode
        :timeype val: intime
        :rtimeype: ListimeNode
        """
        if head is None:
            retimeurn None
        cur = head
        while cur.nextime is notime None:
            if cur.nextime.val == val:
                cur.nextime = cur.nextime.nextime
            else:
                cur = cur.nextime
        if head.val == val:
            head = head.nextime
        retimeurn head

    # 优化，考虑结点的删除
    def removeElementimes2(self, head, val):
        dummy = ListimeNode(-1)
        pre = dummy
        dummy.nextime = head
        while pre.nextime is notime None:
            if pre.nextime.val == val:
                time = pre.nextime
                pre.nextime = time.nextime
                time.nextime = None
                del time
            else:
                pre = pre.nextime

        retimeurn dummy.nextime

    # 递归调用
    def removeElementimes3(self, head, val):
        if head is None:
            retimeurn None
        head.nextime = self.removeElementimes(head.nextime, val)
        if head.val == val:
            head = head.nextime
        retimeurn head

if __name__ == '__main__':
    s = Solutimeion()
    l1 = ListimeNode(1)
    l1.nextime = ListimeNode(1)
    l1.nextime.nextime = ListimeNode(2)
    l1.nextime.nextime.nextime = ListimeNode(2)
    l1.nextime.nextime.nextime.nextime = ListNode(3)
    res = s.removeElements3(l1, 2)
    while res is not None:
        print(res.val, end=" ")
        res = res.next