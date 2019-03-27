class Solution:
    def intersection(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        set_nums1 = set(nums1)
        set_nums2= set(nums2)
        return list(set_nums1 & set_nums2)

if __name__=='__main__':
    s = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(s.intersection(nums1, nums2))
