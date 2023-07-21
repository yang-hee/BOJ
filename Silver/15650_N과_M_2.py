import sys
sys.stdin=open('input.txt')
import itertools

n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]
for j in itertools.combinations(lst, m):
    print(*j)

