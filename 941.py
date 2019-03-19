class Solution:
    def validMountainArray(self, A: 'List[int]') -> 'bool':
        if len(A) < 3:
            return False
        upmountain, downmountain = False, False
        # 判断上坡
        for i in range(len(A)-1):
            if A[i] < A[i + 1]:
                upmountain = True
            else:
                break
        # 判断下坡
        for j in range(i, len(A) -1):
            if A[j] > A[j + 1]:
                downmountain = True
            else:
                downmountain = False
                break
        # 判断是否为山脉
        if j == len(A)-2 and upmountain and downmountain:
            return True
        else:
            return False

    def validMountainArray2(self, A: 'List[int]') -> 'bool':
        if len(A) < 3:
            return False
        elif A[0] >= A[1] or A[-1] >= A[-2]:
            return False
        p = A[0]
        flag = True
        for x in A[1:]:
            # 判断上坡
            if flag:
                if x > p:
                    p = x
                elif x < p:
                    flag = False
                    p = x
                else:
                    return False
            # 判断下坡
            else:
                if x < p:
                    p = x
                else:
                    return False
        return True
    #两头双指针应该也可以实现
if __name__=='__main__':
    s = Solution()
    A = [3,5,3]
    print(s.validMountainArray(A))