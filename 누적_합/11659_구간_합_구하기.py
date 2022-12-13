import sys
sys.stdin = open('11659_구간_합_구하기.txt')
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
sum_lst = [0]

a = 0
for i in range(N):
    a += lst[i]
    sum_lst.append(a)
print(sum_lst)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    res = sum_lst[b] - sum_lst[a - 1]
    print(res)

