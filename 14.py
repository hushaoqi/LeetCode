import sys
class Solution:
    #方法一：水平扫描法
    def longestCommonPrefix1(self, strs: 'List[str]') -> 'str':
        if len(strs) == 0:
            return ""
        ex = strs[0]
        for i in range(1,len(strs)):
            while strs[i].find(ex, 0) != 0:
                ex = ex[0:len(ex) - 1]
        if ex == "":
            return ""
        else:
            return ex
    #法二：列扫描
    def longestCommonPrefix2(self, strs: 'List[str]') -> 'str':
        if (strs == None or len(strs) == 0) :return ""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for j in range(1,len(strs)):
                if(i == len(strs[j]) or strs[j][i] != ch):
                    return strs[0][0:i]
        return strs[0]

    #法三：分治
    def longestCommonPrefix3(self, strs: 'List[str]') -> 'str':
        if (strs == None or len(strs) == 0): return ""
        return Solution.longestCommonPrefix(strs, 0, len(strs)-1)

    def longestCommonPrefix(self, strs: 'List[str]', l: 'int', r: 'int') -> 'str':
        if l == r: return strs[l]
        else:
            mid = (l + r) // 2
            lcpLeft = Solution.longestCommonPrefix(strs,l,mid)
            lcpRight = Solution.longestCommonPrefix(strs,mid +1,r)
            return Solution.commonPrefix(lcpLeft,lcpRight)
    def commonPrefix(self, left:'str', right :'str') ->'str':
        min = min(len(left),len(right))
        for i in range(min):
            if (left[i] != right[i]):
                return left[0:i]
        return left[0:min]

    #法四：二分查找法
    def longestCommonPrefix4(self, strs: 'List[str]') -> 'str':
        if (strs == None or len(strs) == 0): return ""
        minLen = sys.maxsize
        for str in strs:
            minLen = min(minLen,len(str))
        low = 1
        high = minLen
        while(low <= high):
            middle = (low + high) // 2
            if (self.isCommonPrefix(strs,middle)):
                low = middle + 1
            else:
                high = middle - 1

        return strs[0][0:(low + high)//2]
    def isCommonPrefix(self,strs:'str', len:'int' )->'bool':
        str1 = strs[0][len]
        for i in range(1,len(strs)):
            if (not strs[i].startswith(str1)):
                return False
        return True

if __name__=='__main__':
    s = Solution()
    commonPrefix = ["fliower","fliow","flight"]
    print(s.longestCommonPrefix4(commonPrefix))