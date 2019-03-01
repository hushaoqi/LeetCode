class Solution:
    #法一：循环遍历，计数，取最大
    def majorityElement(self, nums: 'List[int]') -> 'int':
        count = {}
        for num in nums:
            if num in count:
                times = count[num] + 1
                count[num] = times
            else:
                count[num] = 1
        MAX = 0
        for num in count:
            if count[num] > MAX:
                MAX = count[num]
        if MAX >= len(nums)//2:
            for k, v in count.items():
                if v == MAX:
                    return k

    #方法二：摩尔投票法(动态规划算法)：注意到这样一个现象——在任何数组中，出现次数大于该数组长度一半的值只能有一个
    '''
    摩尔投票法的基本思想很简单，在每一轮投票过程中，
    从数组中找出一对不同的元素，将其从数组中删除(或者次数抵消）。
    这样不断的删除直到无法再进行投票，如果数组为空，
    则没有任何元素出现的次数超过该数组长度的一半。
    如果只存在一种元素，那么这个元素则可能为目标元素。
    '''
    def majorityElement2(self, nums: 'List[int]') -> 'int':
        count  = 0
        object = None
        for num in nums:
            if num == object: count += 1
            else:
                if count == 0:
                    object = num
                else:count -= 1
        return object
    #方法三：排序
    '''
    众数是指在数组中出现次数大于⌊ n/2 ⌋ 的元素。我们可以先将nums排序，
    然后返回中间元素的值即可（众数的个数大于一半，排好序的nums中间元素一定是众数）
    '''
    def majorityElement3(self, nums: 'List[int]') -> 'int':
        nums.sort()
        return nums[len(nums) // 2]
if __name__=='__main__':
    s = Solution()
    nums = [2,2,1,1,1,2,2,2,3]
    print(s.majorityElement3(nums))