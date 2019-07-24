class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ran = {}
        mag = {}
        for r in ransomNote:
            if r in ran:
                ran[r] += 1
            else:
                ran[r] = 1
        for m in magazine:
            if m in mag:
                mag[m] += 1
            else:
                mag[m] = 1
        for rr in ran.keys():
            if (rr not in mag) or (ran[rr] > mag[rr]) :
                return False

        return True

if __name__== '__main__':
    so = Solution()
    ransom = 'a'
    magazine = 'b'
    print(so.canConstruct(ransom, magazine))