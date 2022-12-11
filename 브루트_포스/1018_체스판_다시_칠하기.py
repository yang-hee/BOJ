import sys
sys.stdin=open('1018_체스판_다시_칠하기.txt')
N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
print(lst)