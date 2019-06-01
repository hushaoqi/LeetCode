import itertools
class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        if nums is None: return []
        if len(nums) == 1: return [nums]
        res = []
        for x in nums:
            ys = nums + []  # 如果不加ys指针会指向和nums相同地址然后remove操作会remove掉nums里面的值
            # ys = nums[:]  # 或者直接用切片,返回新数组，ys.remove时不会改变nums
            ys.remove(x)
            for y in self.permute(ys):
                res.append([x] + y)
        return res
    # 组合迭代器

    def permute2(self, nums: 'List[int]') -> 'List[List[int]]':
        return list(itertools.permutations(nums))

    # 深度优先搜索方法

    def permute3(self, nums: 'List[int]') -> 'List[List[int]]':
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        path = []
        res = []
        self.dfs(nums, path, res)
        return res

    def dfs(self, nums, path, res):
        if len(path) == len(nums):
            res.append(path)
            return

        for i in nums:
            if i not in path:
                path.append(i)
                b = path[:]
                self.dfs(nums, b, res)
                path.pop()

    # 回溯算法
    def permute4(self, nums: 'List[int]') -> 'List[List[int]]':
        res = []

        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res

    def permute5(self, nums: 'List[int]') -> 'List[List[int]]':
        if not nums:
            return [[]]
        res = []
        self.helper(nums, 0, res)
        return res

    def helper(self, nums, start, res):
        if start == len(nums) - 1:
            res.append(nums[:])
            return
        else:
            for i in range(start, len(nums)):
                if i == start:
                    self.helper(nums, start + 1, res)
                else:
                    nums[start], nums[i] = nums[i], nums[start]
                    self.helper(nums, start + 1, res)
                    nums[start], nums[i] = nums[i], nums[start]


if __name__=='__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.permute(nums))


