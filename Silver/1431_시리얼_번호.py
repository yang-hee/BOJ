import sys
sys.stdin = open('input.txt')

# 모든 자리수 합
def a(s):
    a = 0
    for i in s:
        if i.isdigit():
            a += int(i)
    return a


N = int(input())
lst = list(input() for _ in range(N))

                    # 길이, 모든 자리수 합, 사전순
lst.sort(key=lambda x : (len(x), a(x), x))

for j in lst:
    print(j)