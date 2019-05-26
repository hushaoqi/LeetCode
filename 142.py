# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head: ListNode)-> ListNode:
        if head is None:
            return None

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        # 若fast或fast.next 为空，则没有环，否则，相遇，有环
        if fast is None or fast.next is None:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast

    def detectCycle2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = {None}
        while head not in s:
            s.add(head)
            head = head.next
        return head


if __name__=='__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = head.next.next
    '''
    [1]-[2]-[3]-【4】
             \   |
              \  |
               \[5]
    slow 每次走一步，fast 每次走两步 ， 相遇在[4]，slow总共走了3步，fast走了6步
    1 2 3 4 
    1 2 3 4 5 3 4  可以看出fast比slow多走了5 3 4 这个环，
    f = 2 * s ; s + w = f = 2 * s ; -> w = s head到环的起点+环的起点到他们相遇的点的距离 与 环一圈的距离相等
    -->  head运行到环起点 和 相遇点到环起点 的距离也是相等的
           
    '''
    print(s.detectCycle(head).val)



