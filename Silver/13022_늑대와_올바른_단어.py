import sys
sys.stdin=open('input.txt')

s = input()
a = 'w'
cnt = 0
cnt2 = 0
res = 0
# print(len(set(s)))
if len(set(s)) < 4:
    res = 0

else:
    for i in s:
        if i == 'w':
            if a == 'w':
                cnt += 1
            elif a == 'f':
                if cnt2 == cnt:
                    cnt = 1
                    a = 'w'
            else:
                res = 0
                break


        elif i == 'o':
            if a == 'o':
                cnt += 1
            elif a == 'w':
                cnt2 = cnt
                cnt = 1
                a = 'o'
            else:
                res = 0
                break

        elif i == 'l':
            if a == 'l':
                cnt += 1
            elif a == 'o':
                if cnt2 == cnt:
                    cnt = 1
                    a = 'l'
            else:
                res = 0
                break

        elif i == 'f':
            if a == 'f':
                cnt += 1
            elif a == 'l':
                if cnt2 == cnt:
                    cnt = 1
                    a = 'f'
            else:
                res = 0
                break
    else:
        if a != 'f':
            res = 0
        else:
            if cnt2 == cnt:
                res = 1
            else:
                res = 0
print(res)