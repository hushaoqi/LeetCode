# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    # 复杂度分析
    # 时间复杂度：O(N)，其中 N是给定列表的结点数目
    # 空间复杂度：O(1)，slow 和 fast 用去的空间


    # 按顺序将每个结点放入数组 A 中。
    # 然后中间结点就是 A[A.Length/2]，因为我们可以通过索引检索每个结点。

    def middleNode2(self, head: ListNode) -> ListNode:
        A = []
        while head:
            A.append(head.val)
            head = head.next
        return A[len(A)//2]


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(12)
    l1.next.next = ListNode(21)
    l1.next.next.next = ListNode(24)
    l1.next.next.next.next = ListNode(3)
    l1.next.next.next.next.next = ListNode(31)
    # res = s.middleNode(l1)
    res = s.middleNode2(l1)
    # print(res.val)
    print(res)