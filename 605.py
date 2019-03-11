class Solution:
    #如果首位置是0，那么前面再加上个1,0，
    # 如果末位置是0，就在最后面再加上个0,1。
    # 这样处理之后我们就默认连续0的左右两边都是1了，这样如果有k个连续0，
    # 那么就可以通过(k-1)/2来快速计算出能放的花的数量
    def canPlaceFlowers(self, flowerbed: 'List[int]', n: 'int') -> 'bool':
        flowerbed = [1, 0] + flowerbed + [0, 1]
        count = 0
        num = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:count += 1
            else:
                if (count > 0):
                    num += ((count - 1)//2)
                    count = 0
        if num >= n :return True
        else:return False
    # 直接通过修改flowerbed的值来做，我们遍历花床，
    # 如果某个位置为0，我们就看其前面一个和后面一个位置的值，
    # 注意处理首位置和末位置的情况，如果pre和next均为0，
    # 那么说明当前位置可以放花，我们修改flowerbed的值，
    # 并且n自减1，最后看n是否小于等于0
    def canPlaceFlowers2(self, flowerbed: 'List[int]', n: 'int') -> 'bool':
        for i in range(len(flowerbed)):
            if n == 0 :return True
            if (flowerbed[i] == 0):
                next = 0 if(i == len(flowerbed)-1) else flowerbed[i + 1]
                pre = 0 if(i == 0) else flowerbed[i-1]
                if(next + pre ) == 0:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0


if __name__ == '__main__':
    s = Solution()
    n = 2
    flowerbed = [1,0,0,0,1]
    print(s.canPlaceFlowers2(flowerbed,n))