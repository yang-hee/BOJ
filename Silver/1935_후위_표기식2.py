import sys
sys.stdin=open('1935.txt')
N = int(input())
s = input()
lst = []
lst2 = []
res = []
for i in s:
    if i.isalpha():
        a = int(input())
        lst.append([a, i])
    else:
        lst2.append(i)
print(lst)
print(lst2)
print(type(s))
for j in len(s):
    if s[j].isalpha():
        res.append(lst[j][0])
    else:
        b = res.pop()
        c = res.pop()
        res.append(f'{c} {j} {b}')
print(res)

