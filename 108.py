# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    在原函数中完成递归，由于原函数的参数是一个数组，
    所以当把输入数组的中间数字取出来后，
    需要把所有两端的数组组成一个新的数组，
    并且分别调用递归函数，并且连到新创建的cur结点的左右子结点上面
    '''
    def sortedArrayToBST(self, nums: 'List[int]') -> 'TreeNode':
        if len(nums) == 0:return None
        mid = len(nums)//2
        cur = TreeNode(nums[mid])
        left = nums[0:mid]
        right = nums[mid+1:len(nums)]
        cur.left = self.sortedArrayToBST(left)
        cur.right = self.sortedArrayToBST(right)
        return cur

    '''
    要将有序数组转为二叉搜索树，所谓二叉搜索树，
    是一种始终满足左<根<右的特性，如果将二叉搜索树按中序遍历的话，
    得到的就是一个有序数组了。那么反过来，我们可以得知，根节点应该是有序数组的中间点，
    从中间点分开为左右两个有序数组，在分别找出其中间点作为原中间点的左右两个子节点，
    这不就是是二分查找法的核心思想么。
    '''
    def sortedArrayToBST2(self, nums: 'List[int]') -> 'TreeNode':
        return self.converter(nums, 0, len(nums)-1)

    def converter(self, nums: 'List[int]', left: 'int', right: 'int') -> 'TreeNode':
        if left > right: return None
        mid = left + (right - left) // 2
        cur = TreeNode(nums[mid])
        cur.left = self.converter(nums, left, mid - 1)
        cur.right = self.converter(nums, mid + 1, right)
        return cur

if __name__ == '__main__':
    s = Solution()
    nums = [-10,-3,0,5,9]
    '''
    给定有序数组: [-10,-3,0,5,9],

    一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
    
          0
         / \
       -3   9
       /   /
     -10  5
    '''
    s.sortedArrayToBST(nums)
'''
另外需要注意的是，求中点不要用 int mid = (l + r)/2，有溢出风险，
稳妥的方法是 int mid = l + (r-l)/2; 如果你把除2改成右移1位，会和面试官更搭哦。
'''