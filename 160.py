# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 利用集合
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        save = set()
        curA, curB = headA, headB
        while curA is not None or curB is not None:
            if curA is not None:
                if curA in save:
                    return curA
                else:
                    save.add(curA)
                    curA = curA.next
            if curB is not None:
                if curB in save:
                    return curB
                else:
                    save.add(curB)
                    curB = curB.next
        return None
    # 利用双指针，也可以利用快慢指针
    def getIntersectionNode2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 定义两个指针, 第一轮让两个到达末尾的节点指向另一个链表的头部, 最后如果相遇则为交点(在第一轮移动中恰好抹除了长度差)
        # 两个指针等于移动了相同的距离, 有交点就返回, 无交点就是各走了两条指针的长度
        curA, curB = headA, headB
        # 在这里第一轮体现在pA和pB第一次到达尾部会移向另一链表的表头, 而第二轮体现在如果pA或pB相交就返回交点,
        # 不相交最后就是null == null
        while curA != curB:
            if curA is None:
                curA = headB
            else:
                curA = curA.next
            if curB is None:
                curB = headA
            else:
                curB = curB.next
        return curA

    # 法3: 求出两个链表A和B的长度, 长链表先走|len(A)-len(B)|步, 然后同时遍历返回第一个公共节点.
    def getIntersectionNode3(self, headA, headB):

        a = headA
        b = headB
        a_num = 0
        b_num = 0
        while a:
            a = a.next
            a_num += 1
        while b:
            b = b.next
            b_num += 1

        if a_num >= b_num:
            gap = a_num - b_num
            while gap:
                headA = headA.next
                gap -= 1
            while headA and headB:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next
            return
        else:
            gap = b_num - a_num
            while gap:
                headB = headB.next
                gap -= 1
            while headA and headB:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next
            return

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(0)
    l1.next = ListNode(9)
    l1.next.next = ListNode(1)
    l1.next.next.next = ListNode(2)
    l1.next.next.next.next = ListNode(4)

    l2 = ListNode(3)
    l2.next = l1.next.next.next
    print(s.getIntersectionNode3(l1, l2).val)