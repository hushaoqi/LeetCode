class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        anwser = []
        s = sum([x for x in A if x % 2 == 0])  # 求原始数组中偶数的和
        for i in range(len(queries)):
            if (A[queries[i][1]] + queries[i][0]) % 2 == 0:  # 判断val 加到 A[index] 上，是否为偶数
                if A[queries[i][1]] % 2 == 0:  # 若是为偶数，则更新偶数的和
                    s -= A[queries[i][1]]
                A[queries[i][1]] += queries[i][0]
                s += A[queries[i][1]]
                anwser.append(s)   # 将更新的和加入结果数组中
            else:   # 若不是为偶数，则更新偶数的和
                if A[queries[i][1]] % 2 == 0:  # 原始若为偶数，则需要减掉
                    s -= A[queries[i][1]]
                A[queries[i][1]] += queries[i][0]
                anwser.append(s)
        return anwser

if __name__ == '__main__':
    s = Solution()
    # A = [1, 2, 3, 4]
    # queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    # A =[1]
    # queries = [[4, 0]]
    A = [3, 2]
    queries = [[4, 0], [3, 0]]
    print(s.sumEvenAfterQueries(A,queries))
