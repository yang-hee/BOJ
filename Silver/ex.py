import sys
sys.stdin = open('ex.txt')
# 7785번 dictionary로 다시 풀어보장
n = int(sys.stdin.readline())
lst = []
for i in range(n):
    name, a = sys.stdin.readline().split()
    if a == 'enter':
        lst.append(name)
    elif a == 'leave':
        lst.remove(name)
lst.sort(reverse=True)
for j in lst:
    print(j)