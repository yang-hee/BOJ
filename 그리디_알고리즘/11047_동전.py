import sys
sys.stdin=open('11047_동전.txt')
N, K = map(int, input().split())
lst = list(int(input()) for _ in range(N))

res = 0

for i in range(N-1, -1, -1):
    if K >= lst[i]:
        coin = K // lst[i]
        res += coin
        K -= coin * lst[i]
        if K == 0:
            break
print(res)


