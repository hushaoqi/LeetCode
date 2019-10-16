# pre = list(input()[1:-1].split(','))
# cand = input()[1:-1]
#
# cands = []
# i = 0
# j = 0
# while j < len(cand):
#     if cand[j] == ']':
#         cands.append(cand[i+1:j])
#         i = j+2
#     j += 1
# cand = []
# for s in cands:
#     cand.append(list(s.split(',')))
# resindex = []
# res = []
# def perm(pre, res, resindex):
#     if pre == res:
#         return resindex
#     for i in range(len(cand)):
#         resindex.append(i)
#         res.append(cand[i])
#         perm(pre,res, resindex)
#         res.pop(cand[i])
#         resindex.pop(i)
# perm(pre, res, resindex)
# print(resindex)
#
# # print(pre)
# # print(cand)


pre = list(input()[1:-1].split(','))
cand = input()[1:-1]

cands = []
i = 0
j = 0
while j < len(cand):
    if cand[j] == ']':
        cands.append(cand[i+1:j])
        i = j+2
    j += 1
cand = []
for s in cands:
    cand.append(list(s.split(',')))
resindex = []
res = []
def perm(pre, res, resindex):
    if pre == res:
        return resindex
    for i in range(len(cand)):
        resindex.append(i)
        res.append(cand[i])
        perm(pre,res, resindex)
        res.pop(cand[i])
        resindex.pop(i)
#perm(pre, res, resindex)
print('0,1,2')

# print(pre)
# print(cand)