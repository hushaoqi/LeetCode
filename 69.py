class Solution:
    def mySqrt(self, x):
        if x < 0:
            raise Exception("input error")
        if x == 0:
            return 0
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-5:
                return cur

if __name__=='__main__':
    s = Solution()
    x= int(input())
    print("%.4f" % s.mySqrt(x))