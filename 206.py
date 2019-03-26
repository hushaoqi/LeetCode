# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 头插法 逆序
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rev = ListNode(None)
        while head is not None:
            t = head.next
            head.next = rev
            rev = head
            head = t
        return rev
    '''
    递归解法，代码量更少，递归解法的思路是，
    不断的进入递归函数，直到head指向倒数第二个节点，
    因为head指向空或者是最后一个结点都直接返回了，
    newHead则指向对head的下一个结点调用递归函数返回的头结点，
    此时newHead指向最后一个结点，然后head的下一个结点的next指向head本身，
    这个相当于把head结点移动到末尾的操作，因为是回溯的操作，
    所以head的下一个结点总是在上一轮被移动到末尾了，
    但head之后的next还没有断开，所以可以顺势将head移动到末尾，
    再把next断开，最后返回newHead即可
    '''
    def reverseList2(self, head):
        if head is None or head.next is None:
            return head
        new_head = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return new_head



if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(12)
    l1.next.next = ListNode(21)
    l1.next.next.next = ListNode(24)
    l1.next.next.next.next = ListNode(3)
    res = s.reverseList2(l1)
    while res is not None:
        print(res.val, end=" ")
        res = res.next