import sys
sys.stdin = open('input.txt')

N = int(input())
lst = [0] * (N + 1)
day = 0
for _ in range(N):
    day += 1
    T, P = map(int, input().split())
    lst[day] = max(lst[day - 1], lst[day])
    print(T, P)
    if day + T - 1 > N:
        continue
    else:
        lst[day + T - 1] = max(lst[day - 1] + P, lst[day + T - 1])
print(lst[-1])