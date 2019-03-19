class Solution:
    #给定的字符串总是由0结束。bits[i] 总是0 或 1.
    def isOneBitCharacter(self, bits: 'List[int]') -> 'bool':
        #case1:判断前 len(bits) - 1 位：bits[i]是不是1，若是，则除结尾处，一定为：1,0；1,1；
        #                                           判断下两位
        #case2:             是0，则判断下一位
        #重点判断遍历结束位置:case1结束遍历：则需要判断后面有没有多余的1存在
        #                 case2结束遍历：则没有多余的1
        if len(bits) == 1:
            if bits[0] == 0 :return True
            else:return False
        i = 0
        case = -1
        while i < len(bits)-1:
            if bits[i] == 1 :
                i += 2
                case = 1
                continue
            if bits[i] == 0:
                i += 1
                case = 2
                continue
        if case == 1:
            if i == len(bits)-1:return True
            else:return False
        if case == 2:
            return True

    # 优化代码
    def isOneBitCharacter2(self, bits: 'List[int]') -> 'bool':
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 0: i += 1
            else: i += 2
        return i == len(bits) - 1
    # 进一步优化代码
    def isOneBitCharacter3(self, bits: 'List[int]') -> 'bool':
        i = 0
        while i < len(bits) - 1:
            i += (bits[i] + 1)   # 利用bits[i]为1,0的特点
        return i == len(bits) - 1
if __name__ == '__main__':
    s = Solution()
    bits = [1,0,0,1,0]
    #bits = [1, 0, 0]
    print(s.isOneBitCharacter3(bits))