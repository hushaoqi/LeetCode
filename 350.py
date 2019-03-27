class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        Intersection = set_nums1 & set_nums2
        Intersection_list = []
        for num in Intersection:
            Intersection_list.extend([num] * min(nums1.count(num), nums2.count(num)))
        return Intersection_list

    # 如果给定的数组已经排好序呢？你将如何优化你的算法？
    def intersect2(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        p1, p2 = 0, 0
        res = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1, p2 = p1+1, p2+1
                continue
            if nums1[p1] < nums2[p2]:
                p1 += 1
                continue
            if nums1[p1] > nums2[p2]:
                p2 += 1
                continue
        return res

# if __name__ == '__main__':
#     s = Solution()
#     nums1 = [4, 9, 9, 5]
#     nums2 = [9, 4, 9, 8, 4]
#     print(s.intersect(nums1, nums2))

if __name__=='__main__':
    s = Solution()
    nums1 = [4,5,9,9]
    nums2 = [4,4,8,9,9,9]
    print(s.intersect2(nums1, nums2))
