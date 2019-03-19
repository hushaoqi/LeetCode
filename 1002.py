class Solution:
    def commonChars(self, A: 'List[str]') -> 'List[str]':
        r = []
        for i in range(26):
            c = chr(ord('a') + i)
            m = 101
            for ss in A:
                m = min(m, ss.count(c))
            r += m * [c]
        return r

    def commonChars2(self, A: 'List[str]') -> 'List[str]':
        if A == []:
            return []
        d = dict()
        for i in A[0]:  # 记录第一个字符串出现字符次数
            d[i] = d.get(i, 0) + 1

        for i in A[1:]:  # 遍历后面字符串次数
            for k, v in d.items():  # 出现次数取最小值
                if i.count(k) < v:
                    d[k] = i.count(k)
        res = []
        for k, v in d.items():  # 输出最小值大于0的字符
            for i in range(v):
                res.append(k)
        return res

    def commonChars3(self, A: 'List[str]') -> 'List[str]':
        # step1 遍历数组，将每个单词在每个元素中的次数统计出来
        dic = {}
        for item in A:
            tmp = {}
            for _str in item:
                if _str in tmp:
                    tmp[_str] += 1
                else:
                    tmp[_str] = 1
            for key in tmp.keys():
                if key not in dic:
                    dic[key] = []
                dic[key].append(tmp[key])
        # step2:遍历输出结果
        result = []
        for key in dic.keys():
            if len(dic.get(key)) != len(A):
                continue
            dic[key] = sorted(dic[key])
            for i in range(dic[key][0]):
                result.append(key)
        return result


if __name__ == '__main__':
    s = Solution()
    A = ["bella","label","roller"]
    print(s.commonChars3(A))