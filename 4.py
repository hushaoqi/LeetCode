class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        m, n = len(nums1), len(nums2)
        if m > n:
             nums1, nums2, m, n = nums2, nums1, n, m

        if n == 0:
            raise ValueError
        imin, imax, half_len = 0, m, (m + n + 1)//2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums1[i] < nums2[j - 1]:
                # i 太小了，增大,选大的那一半
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i太大了，减小，选小的那一半
                imax = i - 1
            else:
                # i 刚刚好
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2

if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 4]
    nums2 = [5, 6, 7]
    print(s.findMedianSortedArrays(nums1, nums2))


