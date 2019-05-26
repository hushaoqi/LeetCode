# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 归并排序（T：O(nlgn)， S:O(1)）
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        # 寻找中间结点
        slow = head
        fast = head
        pre = head
        while fast is not None and fast.next is not None:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None  # 这一步就是将整个链表从中间分开 失去这一步 后面将无限循环

        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, L1: ListNode, L2: ListNode)-> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        while L1 is not None and L2 is not None:
            if L1.val <= L2.val:
                cur.next = L1
                L1 = L1.next
            else:
                cur.next = L2
                L2 = L2.next
            cur = cur.next
        # 将剩余结点直接连接
        if L1:
            cur.next = L1
        if L2:
            cur.next = L2
        return dummy.next

    # 转换为list，空间复杂度O(n)不满足要求
    def sortList2(self, head: ListNode) -> ListNode:

        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        nums.sort()
        cur = head
        for i in nums:
            cur.val = i
            cur = cur.next
        return head

if __name__=='__main__':
    s = Solution()
    # 输入: 4->2->1->3
    # 输出: 1->2->3->4
    root = ListNode(4)
    root.next = ListNode(2)
    root.next.next = ListNode(1)
    root.next.next.next = ListNode(3)

    result = s.sortList(root)
    while result:
        print(result.val, end=' ')
        result = result.next