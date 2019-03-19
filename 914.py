class Solution:
    def hasGroupsSizeX(self, deck: 'List[int]') -> 'bool':
        deck = sorted(deck)
        num = {}
        x, count = 1, 1
        # 统计每个元素的个数,放在字典中
        for i in range(0, len(deck)-1):
            if deck[i] == deck[i+1]:
                count += 1
            else:
                num[deck[i]] = count
                count = 1
        num[deck[-1]] = count
        # 找出个数最小的X，并判断是否>=2
        x = min(num.values())
        if x < 2:
            return False
        # 判断每个元素的个数是否都能被 2到x之间 的数整除，即是否可以分组
        for i in range(2, x + 1):
            for cot in num.values():
                if cot % i != 0:
                    break
            else:
                return True
        return False
    def hasGroupsSizeX2(self, deck: 'List[int]') -> 'bool':
        d = set(deck)
        dic = {}
        # 统计每个元素的个数(内置函数),放在字典中
        for i in d:
            dic[i] = deck.count(i)
        # 找出个数最小的X
        mn = min(dic.values())
        for i in range(2, mn + 1):
            for j in dic.values():
                if j % i != 0:
                    break
            else:
                return True
        return False

if __name__=='__main__':
    s = Solution()
    A = [1,1,1,1,2,2,2,2,2,2]
    print(s.hasGroupsSizeX(A))