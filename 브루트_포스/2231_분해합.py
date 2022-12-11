import sys
sys.stdin = open('2231_분해합.txt')
N = int(input())
for i in range(1, N + 1):
    n = list(map(int, str(i)))
    res = sum(n) + i
    if res == N:
        res = i
        break
    else:
        res = 0
print(res)
