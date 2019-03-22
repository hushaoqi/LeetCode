class Solution:
    def nextGreaterElement(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        res = []
        for num in nums1:
            #nums1 中 num 在 nums2 中对应位置
            index = nums2.index(num)
            # 右边元素是否存在
            flag = False
            for i in range(index+1, len(nums2)):
                # 是否存在下一个更大元素
                if nums2[i] > num:
                    flag = True
                    res.append(nums2[i])
                    break
            if not flag:
                res.append(-1)

        return res

if __name__=='__main__':
    s = Solution()
    nums1 = [1,3,5,2,4]
    nums2 = [6,5,4,3,2,1,7]
    # nums1 = [4, 1, 2]
    # nums2 = [1, 3, 4, 2]
    print(s.nextGreaterElement(nums1,nums2))
