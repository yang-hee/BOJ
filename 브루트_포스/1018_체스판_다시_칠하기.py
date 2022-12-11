import sys
sys.stdin=open('1018_체스판_다시_칠하기.txt')
N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
res_list = []

# 시작값 설정
for i in range(0, N - 7):
    for j in range(0, M - 7):

        # 칠해야 하는 정사각형 개수
        res = 0

        # for b1 in range(i, i + 8):
        #     for b2 in range(j, j + 8):
        #         if lst[b1][b2] == 'W'
#----------------------------------
        # 체스판 순회
        for b1 in range(i, i + 8):
            for b2 in range(j, j + 8):

                if (b1 + b2) % 2 == 0:
                    if lst[b1][b2] == 'B':
                        res += 1
                else:
                    if lst[b1][b2] == 'W':
                        res += 1
        res_list.append(res)
res_list.sort()
if res_list[0] > 64 - res_list[-1]:
    res = 64 - res_list[-1]
else:
    res = res_list[0]
print(res)