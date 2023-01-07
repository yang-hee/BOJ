import sys
sys.stdin=open('25215_타이핑.txt')

diamond = False         # 활성화시 대문자, 처음은 비활성 상태

s = input()
res = 0
for i in range(len(s)):
    if s[i].isupper(): # 대문자인경우
        if diamond:    # 대문자 입력 활성화상태
            res += 1
        else:          # 소문자 입력 상태
            if i != len(s) -1 and s[i + 1].isupper():
                diamond = True
            res += 2


    else:              # 소문자인경우
        if not diamond:
            res += 1
        else:
            if i != len(s) -1 and s[i + 1].islower():
                diamond = False
            res += 2

print(res)
# ILoveYOu
# i*l*oveYOU*
# *il*ove