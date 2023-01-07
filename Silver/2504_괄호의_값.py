import sys
sys.stdin=open('2504_괄호의_값.txt')

a = input()

lst = []
res_lst = []
cnt = 0
res = 1
for i in range(len(a)):

    if a[i] == '(':
        lst.append(a[i])
        res *= 2

    elif a[i] == '[':
        lst.append(a[i])
        res *= 3

    elif a[i] == ']' and lst:
        b = lst.pop()
        if b == '(':
            break
        else:
            res +=
    elif a[i] == ')' and lst:
        b = lst.pop()
        if a[i] == '[':
            break
        else:
            res.append()
    else:
        if a[i] == ']' or a[i] == ')':
            res = 0
            break
print(res)


