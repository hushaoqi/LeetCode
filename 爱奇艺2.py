
longstr = input()
short = input()
n = len(short)
T = [0]*len(longstr)
count = 0
# for i in range(len(longstr)-1, -1, -1):
#     T[i] = longstr[:i+1].count(short)
for i in range(len(longstr)- n + 1):
    if longstr[i:i +n] == short:
        count += 1
    for j in range(i + n-1, len(longstr)):
        T[j] = count
for num in T:
    print(num, end=" ")