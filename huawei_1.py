input_str = input().strip()
# 输入格式转换
# A:[2,3,4,5,6],B:[3,4,4,6,8,9],R:3
for i in range(len(input_str)):
    if input_str[i] == 'B':  # 循环遍历，找字符为B的位置
        A_str = input_str[3:i-2]  # 然后把A数列剪切出来
        input_str = input_str[i:]  # 去除A串部分
        A = list(map(int, A_str.split(',')))  # 将A序列用列表保存
        break
# 同理，找到B串，R
for i in range(len(input_str)):
    if input_str[i] == 'R':
        B_str = input_str[3:i-2]
        R_str = input_str[i+2:]
        B = list(map(int, B_str.split(',')))
        R = int(R_str)
# 数对生成
i = 0
while i < len(A):  # 依次遍历
    j = 0
    flag = False  # 判断是否存在满足的条件A[i] <= B[j] and B[j] - A[i] <= R:的数对，如果不满足，则需要找出最近的B[j]
    while j < len(B):
        if A[i] <= B[j] and B[j] - A[i] <= R:  # 找出满足条件的数对，并按照输出格式处理，不能直接使用Python元祖，(2, 3)中间会有空格
            # out = '(' + str(A[i]) + ',' + str(B[j]) + ')'
            print('(' + str(A[i]) + ',' + str(B[j]) + ')', end='')
            flag = True
            if B[j] - A[i] > R:
                break
        j += 1
    if flag is False:  # 不存在满足的条件A[i] <= B[j] and B[j] - A[i] <= R:的数对，需要找出最近的B[j]
        k = 0
        while k < len(B):
            if A[i] <= B[k]:
                print('(' + str(A[i]) + ',' + str(B[k]) + ')', end='')
                # out = '(' + str(A[i]) + ',' + str(B[k]) + ')'
                break
            k += 1

    i += 1

