# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 常规的链表删除操作
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        cur = head
        while cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        if head.val == val:
            head = head.next
        return head

    # 优化，考虑结点的删除
    def removeElements2(self, head, val):
        dummy = ListNode(-1)
        pre = dummy
        dummy.next = head
        while pre.next is not None:
            if pre.next.val == val:
                t = pre.next
                pre.next = t.next
                t.next = None
                del t
            else:
                pre = pre.next

        return dummy.next

    # 递归调用
    def removeElements3(self, head, val):
        if head is None:
            return None
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            head = head.next
        return head

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(2)
    l1.next.next.next.next = ListNode(3)
    res = s.removeElements3(l1, 2)
    while res is not None:
        print(res.val, end=" ")
        res = res.next