class Solution:
    def merge(self, nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j = 0,0
        length = m
        while i < length and j < n:
            if nums2[j] < nums1[i]:
                k = length
                while k > i:
                    nums1[k] = nums1[k-1]
                    k -= 1
                nums1[i] = nums2[j]
                length += 1
                i += 1
                j += 1
            else:
                i += 1
        while j < n:
            nums1[i] = nums2[j]
            length += 1
            i += 1
            j += 1


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0,0,0]
    m = 3
    nums2 = [0,2,4 ,5 ,6]
    n = 5
    s.merge(nums1,m,nums2,n)
    print(nums1)
