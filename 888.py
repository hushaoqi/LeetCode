class Solution:
    def fairCandySwap(self, A: 'List[int]', B: 'List[int]') -> 'List[int]':
        diff = sum(A) - sum(B)
        for numA in A:
            # if (numA - diff / 2) in B:   #try 可以替换
            try:
                index = B.index(numA - diff / 2)
                return [numA, B[index]]
            except:
                continue
        return []
    # 换为集合，速度快很多
    def fairCandySwap2(self, A: 'List[int]', B: 'List[int]') -> 'List[int]':
        diff = sum(B) - sum(A)
        SetB = set(B)
        for x in A:
            if diff / 2 + x in SetB:
                break
        return [x, int(diff / 2 + x)]

if __name__=='__main__':
    s = Solution()
    A = [2, 2, 7, 5]
    B = [2, 3, 4, 6]
    print(s.fairCandySwap2(A,B))