# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = ListNode(None)
        cur = res
        while head is not None:
            if cur.val != head.val:
                cur.next = ListNode(head.val)
                cur = cur.next
            head = head.next
        return res.next

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(2)
    l1.next.next.next.next = ListNode(3)
    res = s.deleteDuplicates(l1)
    while res is not None:
        print(res.val, end=" ")
        res = res.next