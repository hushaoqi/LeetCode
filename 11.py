class Solution:
    # 穷举搜索，会超时
    def maxArea(self, height: 'List[int]') -> int:
        max_water = 0
        for front in range(len(height) - 1):

            for behind in range(front+1, len(height)):
                water = min(height[front], height[behind]) * (behind - front)
                max_water = max(max_water, water)

        return max_water

    # 两个指针向中间搜索，每移动一次算一个值和结果比较取较大的
    def maxArea2(self, height: 'List[int]') -> int:
        max_water = 0
        front = 0
        behind = len(height) - 1
        while front < behind:
            max_water = max(max_water, min(height[front], height[behind]) * (behind - front))
            if height[front] < height[behind]:
                front += 1
            else:
                behind -= 1
        return max_water

if __name__=='__main__':
    s = Solution()
    nums = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea2(nums))