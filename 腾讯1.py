case = int(input())  # 用例数
tel = []
for _ in range(case):
    n = int(input())  # the length of tel-number
    number = input()  # tel-number
    tel.append([n, number])
# print(tel)
# 从字符串中删除若干个字符，是否能构成企鹅王国号码
# 第一个数字为8，总长11位
for test in tel:
    if test[0] >= 11 and test[1][0] == '8' and (1 <= test[0] <= 100):  # 首位为8，大于等于11，那么肯定可以操作得到满足条件的的号码
        print("YES")
    elif test[0] < 11:  # 小于11位，没法操作
        print("NO")
    else:  # 大于11位，判断能否操作得到，即找第一个8出现的位置到最后的长度是否大于等于11
        index = test[1].find('8')
        if index != -1 and test[0] - index >= 11 and (1 <= test[0] <= 100):  # 存在数字8，且8往后的数字长度>=11
            print("YES")
        else:
            print("NO")

'''
1
15
98999999998
'''
