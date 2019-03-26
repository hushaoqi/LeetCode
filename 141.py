# 这道题我的想法始终是要遍历一边链表O(n)才能发现是不是有回路.
# 不过题目不是说,在输入的时候有pos这个变量吗?那直接return pos != -1 不就行了??
# 用 O(1)（即，常量）内存解决此问题
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 采用双指针，p1,p2;p1为慢指针，每次走一个结点，p2为快指针，每次走两个结点
        # 记录p1,p2走的结点数，当两结点相遇时，结点数之差即为环结点数
        # 结点起始位置为 慢指针结点数 - 环结点数
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    # 巧用集合，判断是否存在交点
    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        save = set()
        cur = head
        while cur is not None:
            if cur in save:
                return True
            else:
                save.add(cur)
                cur = cur.next
        return False
if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(2)
    l1.next.next.next.next = ListNode(3)
    #l1.next.next.next.next.next = l1.next.next
    print(s.hasCycle(l1))