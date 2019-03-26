# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        return list1 == list1[::-1]

    # 一，find mid node 使用快慢指针找到链表中点。
    # 二，reverse 逆序后半部分。
    # 三，check 从头、中点，开始比较是否相同。
    def middleNode(self, head):# 函数返回中间节点，若中间节点有两个，则返回后一个
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, slow):
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        return node

    def isPalindrome2(self, head):
        mid_node = self.middleNode(head)
        node = self.reverseList(mid_node)
        while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True


    def isPalindrome3(self, head):
        """
        判断一个链表是否是回文的，很自然的想法就是两个指针，一个指针从前往后走，一个指针从后往前走，判断元素值是否相同，这里要分几个步骤来进行求解：
        1、找到链表长度的一半，用追赶法，一个指针一次走两步，一个指针一次走一步
        2、将后一半数组转置
        3、判断链表是否是回文链表
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt

        while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(2)
    l1.next.next.next.next = ListNode(1)
    res = s.isPalindrome2(l1)
    print(res)