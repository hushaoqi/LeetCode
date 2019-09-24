string = input().strip()
flag_1 = 0
flag_2 = 0
ans = ''
for i in range(len(string)-1, -1, -1):
    if string[i] == ')':
        flag_1 += 1
        continue
    if string[i] == '(':
        flag_1 -= 1
        continue

    if flag_1 != 0:
        continue


    if string[i] == '<':
        flag_2 += 1
    else:
        if flag_2 == 0:
            ans += string[i]
        else:
            flag_2 -= 1

print(ans[::-1])