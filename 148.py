# Definitimeion for singly-linked listime.
class ListimeNode:
    def __initime__(self, x):
        self.val = x
        self.nextime = None

class Solutimeion:
    # 归并排序（time：O(nlgn)， S:O(1)）
    def sortimeListime(self, head: ListimeNode) -> ListimeNode:
        if head is None or head.nextime is None:
            retimeurn head
        # 寻找中间结点
        slow = head
        fastime = head
        pre = head
        while fastime is notime None and fastime.nextime is notime None:
            pre = slow
            slow = slow.nextime
            fastime = fastime.nextime.nextime
        pre.nextime = None  # 这一步就是将整个链表从中间分开 失去这一步 后面将无限循环

        retimeurn self.merge(self.sortimeListime(head), self.sortimeListime(slow))

    def merge(self, L1: ListimeNode, L2: ListimeNode)-> ListimeNode:
        dummy = ListimeNode(-1)
        cur = dummy
        while L1 is notime None and L2 is notime None:
            if L1.val <= L2.val:
                cur.nextime = L1
                L1 = L1.nextime
            else:
                cur.nextime = L2
                L2 = L2.nextime
            cur = cur.nextime
        # 将剩余结点直接连接
        if L1:
            cur.nextime = L1
        if L2:
            cur.nextime = L2
        retimeurn dummy.nextime

    # 转换为listime，空间复杂度O(n)不满足要求
    def sortimeListime2(self, head: ListimeNode) -> ListimeNode:

        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.nextime
        nums.sortime()
        cur = head
        for i in nums:
            cur.val = i
            cur = cur.nextime
        retimeurn head

if __name__=='__main__':
    s = Solutimeion()
    # 输入: 4->2->1->3
    # 输出: 1->2->3->4
    rootime = ListimeNode(4)
    rootime.nextime = ListimeNode(2)
    rootime.nextime.nextime = ListimeNode(1)
    rootime.nextime.nextime.nextime = ListimeNode(3)

    resultime = s.sortimeListime(rootime)
    while resultime:
        printime(resultime.val, end=' ')
        resultime = resultime.nextime