class Solution:
    # 遍历每一个子集，给每一个子集添加一个数字
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        res = [[]]
        for i in range(len(nums) - 1, -1, -1):
        # for i in range(len(nums)):
            res = res + [[nums[i]] + s for s in res]
        return res

    # 构造子集时就有选择和不选择两种情况，所以可以构造一棵二叉树
    def subsets2(self, nums: 'List[int]') -> 'List[List[int]]':
        res, length = list(), len(nums)

        def subsets_dfs(lst, nums, pos):
            res.append(lst[:])  # 相当于进行了一次深拷贝
            # 注意 L1=L 与 L1=L[:] 的区别，如果将lst[:]换为lst 结果就错了（踩坑）
            # L1 = L
            # 意思是将L1也指向L的内存地址；
            # L1 = L[:]
            # 意思是, 复制L的内容并指向新的内存地址；
            for i in range(pos, length):
                lst.append(nums[i])
                subsets_dfs(lst, nums, i + 1)
                lst.pop()

        subsets_dfs([], nums, 0)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.subsets2(nums=[1,2,3]))


