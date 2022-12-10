import sys
sys.stdin=open('1931_회의실배정.txt')

# 첫값을 기준으로 정렬! lst 순회하면서 첫값이 time의 첫값보다 크고!
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()
time = lst[0]
res = 1
for i in range(1, N):
    if time[1] <= lst[i][0]:
        res += 1
        time = lst[i]

    elif time[0] < lst[i][0] and lst[i][1] <= time[1]:
        time = lst[i]

print(res)


    # if time[1] == lst[i][0]:
    #     res += 1
    #     time = lst[i]
    # elif time[1]
    # elif time[1] > lst[i][1]:
    #     time = lst[i]
    # elif:

    # elif time[1] <= lst[i][0]:
    #     res += 1
    #     time = lst[i]

