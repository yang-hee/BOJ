import sys
sys.stdin=open('2346_풍선_터뜨리기.txt')
from collections import deque

N = int(input())
lst = list(map(int, input().split()))
bq = deque()
for idx in range(1, N + 1):
    bq.append([idx, lst[idx - 1]])
res = []
while True:
    a = bq.popleft()
    res.append(a[0])
    if not bq:
        break

    if a[1] > 0:
        for i in range(a[1] - 1):
            b = bq.popleft()
            bq.append(b)
    else:
        for i in range(-a[1]):
            b = bq.pop()
            bq.appendleft(b)

print(*res)