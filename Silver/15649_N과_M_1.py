import sys
sys.stdin=open('input.txt')

def a(n):
    if len(lst) == M:
        print(*lst)
        return

    for i in range(1, N + 1):
        if i not in lst:
            lst.append(i)
            a(n)
            lst.pop()


N, M = map(int, input().split())
lst = []
a(1)
