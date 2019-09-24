s = input()
mask = list("MASK")
add = ''
for i in range(len(s)):
    if s[i+1] == '@':
        s = s[i:]
        break
    add += (s[i] + mask[i%4])
add += s
print(add)
