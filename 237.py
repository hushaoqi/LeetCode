# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 和我们平时解题的思路不一样，给我们的这个node就是链表的一部分，
        # 直接在上面操作就可以了，不要纠结为什么没有head
        # 将node的下一个结点复制到node，并删除node的下一个结点
        node.val = node.next.val
        node.next = node.next.next

if __name__ == '__main__':

    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    node = l1.next.next
    l1.next.next.next = ListNode(2)
    l1.next.next.next.next = ListNode(1)
    s.deleteNode(node)
    res = l1
    while res is not None:
        print(res.val, end=" ")
        res = res.next