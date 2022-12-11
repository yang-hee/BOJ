import sys
sys.stdin = open('7568_덩치.txt')
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

res = []
for i in range(N):
    cnt = 1
    for j in range(N):
        # 나랑 나는 비교하면 안되니까 넘겨주자
        if i == j:
            continue
        # 덩치가 큰 사람이 있을경우 cnt +1 해주기!
        else:
            if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
                cnt += 1
    res.append(cnt)
print(*res)
