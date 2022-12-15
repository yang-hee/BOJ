import sys
sys.stdin = open('11660_구간_합_구하기5.txt')

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(1, N):
        arr[i][j] += arr[i][j - 1]

for i in range(N):
    for j in range(1, N):
        arr[j][i] += arr[j - 1][i]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if x1 == 1 and y1 == 1:
        print(arr[x2 - 1][y2 - 1])
    elif x1 == 1:
        print(arr[x2 - 1][y2 - 1] - arr[x2 - 1][y1 - 2])
    elif y1 == 1:
        print(arr[x2 - 1][y2 - 1] - arr[x1 - 2][y2 - 1])
    else:
        print(arr[x2 - 1][y2 - 1] - arr[x2 - 1][y1 - 2] - arr[x1 - 2][y2 - 1] + arr[x1 - 2][y1 - 2])

## 시간초과1
# for i in range(N):
#     for j in range(N):
#         if i == 0 and j == 0:
#             arr_sum[i][j] = arr[i][j]
#         elif i == 0:
#             arr_sum[i][j] = arr_sum[i][j - 1] + arr[i][j]
#         elif j == 0:
#             arr_sum[i][j] = arr_sum[i - 1][j] + arr[i][j]
#         else:
#             arr_sum[i][j] = arr_sum[i][j - 1] + arr_sum[i - 1][j] + arr[i][j] - arr_sum[i - 1][j - 1]
#
# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     if x1 == 1 and y1 == 1:
#         res = arr_sum[x2 - 1][y2 - 1]
#     elif x1 == 1:
#         res = arr_sum[x2 - 1][y2 - 1] - arr_sum[x2 - 1][y1 - 2]
#     elif y1 == 1:
#         res = arr_sum[x2 - 1][y2 - 1] - arr_sum[x1 - 2][y2 - 1]
#     else:
#         res = arr_sum[x2 - 1][y2 - 1] - arr_sum[x2 - 1][y1 - 2] - arr_sum[x1 - 2][y2 - 1] + arr_sum[x1 - 2][y1 - 2]
#     print(res)


## 시간초과2
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# for i in range(N):
#     for j in range(1, N):
#         arr[i][j] += arr[i][j - 1]
#
# for i in range(N):
#     for j in range(1, N):
#         arr[j][i] += arr[j - 1][i]
#
# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     if x1 == 1 and y1 == 1:
#         res = arr[x2 - 1][y2 - 1]
#     elif x1 == 1:
#         res = arr[x2 - 1][y2 - 1] - arr[x2 - 1][y1 - 2]
#     elif y1 == 1:
#         res = arr[x2 - 1][y2 - 1] - arr[x1 - 2][y2 - 1]
#     else:
#         res = arr[x2 - 1][y2 - 1] - arr[x2 - 1][y1 - 2] - arr[x1 - 2][y2 - 1] + arr[x1 - 2][y1 - 2]
#     print(res)
