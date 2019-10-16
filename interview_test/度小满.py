n = int(input())
blood = list(map(int, input().split()))
blood.insert(0, 0)  # 控制index为1-n
# 第一次遍历，优先处理x,2x,2x+1
count = 0
i = 1
while i <= n and (i*2+1) <= n:
    while blood[i] != 0 :
        count += 1
        blood[i] -= 1
        if blood[i*2] != 0:
            blood[i*2] -= 1
        if blood[i*2+1] != 0:
            blood[i*2+1] -= 1
    i += 1

# 第二次遍历，优先处理2x,2x+1
i = 1
while i <= n and (i*2+1) <= n:
    while blood[i*2] != 0:
        count += 1
        blood[i*2] -= 1
        if blood[i*2+1] != 0:
            blood[i*2+1] -= 1
    i += 1
# 第三次遍历，遍历所有不为零的
i = 1
while i <= n:
    if blood[i] != 0:
        count += blood[i]
    i += 1
print(count)


'''

5
1 2 3 4 5
'''