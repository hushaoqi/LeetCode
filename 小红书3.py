n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
# 首先按照第一值大小排序，当第一个值相等，则按照第二个值排序
array.sort(key=(lambda x: (x[0], x[1])))
print(array)
dp = [0] * n
dp[0] = array[0][1]
ans = 0
# 按照第二个值，找出最大升序子序列
for i in range(1, n):
    if array[i][1] >= dp[ans]:
        ans += 1
        dp[ans] = array[i][1]
    else:  # 找到第一个大于array[i][1]的dp,更新长度为j 的末尾的元素值
        j = 0
        while dp[j] <= array[i][1]:
            j += 1
        dp[j] = array[i][1]
print(ans+1)

'''
4
2 3
1 4
1 3
2 4
'''