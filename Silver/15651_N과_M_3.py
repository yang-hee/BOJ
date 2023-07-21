import sys
sys.stdin=open('input.txt')

def a():
    if len(num) == M:
        print(*num)
        num.clear
        return

    for i in range(1, N + 1):
        num.append(i)
        a()
        num.pop()

N, M = map(int, input().split())
num = []
a()

