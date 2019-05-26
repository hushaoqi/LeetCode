# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head
        cur = head.next
        len = 2
        # 找到链表尾，连接成环，并且保存链表长度
        while cur.next:
            cur = cur.next
            len += 1
        cur.next = head
        # 计算向右旋转，后头指针的位置
        pre_head = cur
        step = len - (k % len)
        while step > 0:
            head = head.next
            pre_head = pre_head.next
            step -= 1
        # 分割头尾
        pre_head.next = None
        return head

if __name__=='__main__':
    s = Solution()
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    result = s.rotateRight(root, 3)
    while result:
        print(result.val, end=' ')
        result = result.next


