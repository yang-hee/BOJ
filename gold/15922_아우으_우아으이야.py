import sys
sys.stdin = open('input.txt')

N = int(input())
low_num, high_num = map(int, input().split())
res = high_num - low_num

for i in range(N-1):
    low, high = map(int, input().split())
    if high_num >= high and low_num <= low:
        continue
    elif high_num > low:
        res = res - (high_num - low_num) + (high - low_num)

    else:
        res += high - low
    low_num = low
    high_num = high
print(res)

