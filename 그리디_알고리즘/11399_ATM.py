import sys
sys.stdin=open('11399_ATM.txt')

N = int(input())

lst = list(map(int, input().split()))
lst.sort()

res = 0
for i in range(N):
    res += lst[i] * (N - i)
print(res)
