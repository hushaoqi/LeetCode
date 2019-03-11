import functools
class Solution:
    def matrixReshape(self, nums: 'List[List[int]]', r: 'int', c: 'int') -> 'List[List[int]]':
        length = len(nums[0])
        #reshape = r*[[0]*c]
        reshape = [[0]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                n = i * c + j
                reshape[i][j] = nums[n // length][n % length]
                #本以为结果是这样，[[1], [2], [3], [4]]
                #没想到是这样：[[4], [4], [4], [4]]
                #原因出现在这里：reshape = r*[[0]*c] 第一个“*”是（浅）拷贝了同一个引用，每个对象指向同一块内容
        return reshape

    def matrixReshape2(self, nums: 'List[List[int]]', r: 'int', c: 'int') -> 'List[List[int]]':
        # python3需要导入 from functools import reduce
        #二维转一维
        all_nums = functools.reduce(lambda x, y: x + y, nums)
        if (r * c > len(all_nums)):
            return nums
        return [all_nums[i:i + c] for i in range(0, len(all_nums), c)]

    def matrixReshape3(self, nums: 'List[List[int]]', r: 'int', c: 'int') -> 'List[List[int]]':
        temp = []
        #二维转一维
        for i in range(len(nums)):
            temp.extend(nums[i])
        if r * c != len(temp):
            return nums
        res = []
        for i in range(r):
            res.append(temp[c * i: c * i + c])
        return res
if __name__ == '__main__':
    s = Solution()
    nums =[[1, 2],[3, 4]]
    r = 4
    c = 1
    print(s.matrixReshape2(nums,r,c))