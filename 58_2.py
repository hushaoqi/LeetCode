loop = list("0123456789'!@#$%^&*(){}\<>?")
n = int(input())
a = []
while n != 0:
    a.append(loop[n%27])
    n = n//27
a.reverse()
print("".join(a))
