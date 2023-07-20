import sys
sys.stdin = open('input.txt')

N = int(input())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(lst)
lst.sort()
# print(lst)
for i in lst:
    print(*i)