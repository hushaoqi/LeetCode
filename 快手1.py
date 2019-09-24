import copy
num_str = input()
num = []
for si in num_str:
    num.append(int(si))
def letter(num):
    if len(num) == 0:
        return []

    aa = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    re = [""]
    for x in num:
        aaa = []
        for y in re:
            for z in aa[x]:
                aaa.append(y+z)
        re = aaa
    return re
res = letter(num)
print(res)
result = ""
for s in str(res):
    if s != "'":
        result += "".join(s)

print(result)