import sys
n, k = map(int, input().split())
a = list(map(int, input().split()))
while k > 0:
    min_value = sys.maxsize
    zero = True
    for num in a:
        if num != 0:  # 是否存在非零元素
            zero = False
            break
    if zero:  # 如果数组为全零
        print(0)
    else:
        for num in a:
            if num < min_value and num != 0:  # 找出最小非零元素
                min_value = num
        print(min_value)
        for i in range(len(a)):
            if a[i] != 0:  # 所有非零元素减去x（最小值）
                a[i] -= min_value
    k -= 1
'''
7 9
5 8 10 3 6 10 8
'''