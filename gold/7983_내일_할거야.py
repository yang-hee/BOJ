import sys
sys.stdin = open('today.txt')

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort(key=lambda x : x[1])                                   # 과제를 끝내야하는 날짜 기준으로 정렬

end_day = lst[-1][1]                                            # 최대한 미룰 수 있는 날
for i in range(len(lst)-1, -1, -1):
    if end_day <= lst[i][1]:
        end_day -= lst[i][0]
    else:
        end_day = lst[i][1] - lst[i][0]                         # 이미 i번 마지막날에 과제를 했을 경우 end_day 보다 lst[i]의 날이 작을 때..
print(end_day)
