class Solution:
    def isLongPressedName(self, name: 'str', typed: 'str') -> 'bool':
        nameIdx, typedIdx = 0, 0

        while nameIdx < len(name) and typedIdx < len(typed):
            if name[nameIdx] == typed[typedIdx]:
                nameIdx += 1
                typedIdx += 1
            else:
                return False

            if nameIdx < len(name) and name[nameIdx] != name[nameIdx - 1]:
                while typedIdx < len(typed) and typed[typedIdx] == typed[typedIdx - 1]:
                    typedIdx += 1
        # 检查这种情况
        # name = "pyplrz"   typed = "ppyypllrzggg"
        # name = "pyplrz"   typed = "ppyypllrzzzz"
        while typedIdx < len(typed) and typed[typedIdx] == typed[typedIdx - 1]:
            typedIdx += 1

        return True if nameIdx == len(name) and typedIdx == len(typed) else False

    def isLongPressedName2(self, name: 'str', typed: 'str') -> 'bool':

        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)

if __name__ == '__main__':
    s = Solution()
    test = {"alex": "aaleex",            # True
            "saeed": "ssaaedd",          # False
            "leelee": "lleeelee",        # True
            "pyplrz": "ppyypllr",        # False
            "yplrz": "yypllrzggg",       # False
            "laiden": "laiden",          # ture
            "opyplrz": "oppyypllrzzzz"   # Ture
            }
    for name in test:
        print(s.isLongPressedName(name, test[name]))