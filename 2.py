# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        res = ListNode(0) #链表和
        crr = ListNode(0)
        crr = res
        p = ListNode(0)
        p = l1
        q = ListNode(0)
        q = l2
        carry = 0 # 初始进位为0
        while(p != None or q != None):
            if (p != None):x = p.val
            else:x = 0
            if (q != None):y = q.val
            else:y = 0
            sum = carry + x + y
            carry = int(sum / 10)
            crr.next = ListNode(sum % 10)
            crr = crr.next
            if(p != None):p = p.next
            if(q != None):q = q.next
        if(carry > 0 ):
            crr.next = ListNode(carry)
        return res.next
if __name__ == "__main__":
    AddSum = Solution()
    l1 = ListNode(0)
    l2 = ListNode(0)
    # 逐个为 data 内的数据创建结点, 建立链表
    data1 = [7,6,5]
    data2 = [4,6,8,9]
    p = l1
    for num in data1:
        node = ListNode(num)
        p.next = node
        p = p.next
    p.next = None
    q = l2
    for num in data2:
        node = ListNode(num)
        q.next = node
        q = q.next
    q.next = None
    result = AddSum.addTwoNumbers(l1,l2)
    while(result.next != None):
        result = result.next
        print(result.val,end='')#输出不换行