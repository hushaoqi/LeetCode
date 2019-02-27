class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        length = len(digits)
        i = length - 1
        while i >= 0:
            if (digits[i] < 9):
                digits[i] += 1
                i -= 1
                return digits
            else:
                digits[i] = 0
                i -= 1

            #扩展一位
        exdigits = [1] + digits
        return exdigits

if __name__ == '__main__':
    s = Solution()
    digits = [1,2,3]
    print(s.plusOne(digits))

