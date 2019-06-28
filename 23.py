# Definition for singly-linked list.
import sys
from queue import PriorityQueue
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    遍历所有链表，将所有节点的值放到一个数组中。
    将这个数组排序，然后遍历所有元素得到正确顺序的值。
    用遍历得到的值，创建一个新的有序链表。
    '''
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        res_array = []
        for node in lists:
            while node:
                res_array.append(node.val)
                node = node.next

        head = ListNode(0)
        point = head
        for num in sorted(res_array):
            point.next = ListNode(num)
            point = point.next
        return head

    '''
        比较 k 个节点（每个链表的首节点），获得最小值的节点。
        将选中的节点接在最终有序链表的后面。
    '''
    def mergeKLists2(self, lists: 'List[ListNode]') -> 'ListNode':
        n = len(lists)
        res = point = ListNode(0)
        while 1:  # 超时，该如何判断链表合并完成更优呢？
            min_value = sys.maxsize
            min_node = None
            count = 0
            for i in range(n):
                if lists[i] == None:
                    count += 1
                if lists[i]:
                    if lists[i].val < min_value:
                        min_value = lists[i].val
                        min_node = i
            if count == n:
                return res.next
            lists[min_node] = lists[min_node].next
            point.next = ListNode(min_value)
            point = point.next

    '''
     比较环节 用 优先队列 进行了优化。
    '''

    def mergeKLists3(self, lists: 'List[ListNode]') -> 'ListNode':
        import heapq
        l = []
        size = len(lists)
        for index in range(size):
            if lists[index]:
                heapq.heappush(l, (lists[index].val, index))
        dummy_node = ListNode(-1)
        cur = dummy_node
        while l:
            _, index = heapq.heappop(l)
            head = lists[index]
            cur.next = head
            cur = cur.next
            if head.next:
                heapq.heappush(l, (head.next.val, index))
                lists[index] = head.next
                head.next = None
        return dummy_node.next


if __name__=='__main__':
    s = Solution()
    root1 = ListNode(1)
    root1.next = ListNode(5)
    root1.next.next = ListNode(8)

    root2 = ListNode(3)
    root2.next = ListNode(5)
    root2.next.next = ListNode(9)

    root3 = ListNode(2)
    root3.next = ListNode(6)
    root3.next.next = ListNode(7)

    lists = [root1, root2, root3]
    result = s.mergeKLists3(lists)
    while result:
        print(result.val)
        result = result.next