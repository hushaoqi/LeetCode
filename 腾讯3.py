T = int(input())
for _ in range(T):
    n = int(input())
    value = list(map(int, input().split()))
    A = []
    sum_a = 0
    B = []
    sum_b = 0
    sum_value = sum(value)
    mid_value = sum_value / 2
    min_index = -1
    h = 0
    while h < n:
        min_value = mid_value - value[0]
        i = 0
        while i < n:
            temp = mid_value - value[i]
            if temp <= min_value:
                min_value = temp
                min_index = i
            i += 1

        # print("出列的元素是：", value[min_index])
        # 将取出的元素放在和较小的数组里
        if sum_a <= sum_b:
            A.append(value[min_index])
            sum_a += value[min_index]
        else:
            B.append(value[min_index])
            sum_b += value[min_index]
        # 剔除已经放入分组中的元素
        value.pop(min_index)
        n -= 1
    h += 1

    # print(A)
    # print(B)
    print(min(sum_a, sum_b), max(sum_a, sum_b))
'''
1
4
5 9 4 7
8
9 13 18 10 12 4 18 3
'''