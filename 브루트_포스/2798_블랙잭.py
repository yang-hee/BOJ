import sys
sys.stdin=open('2798_블랙잭.txt')

N, M = map(int, input().split())                # N 카드의 개수 / M 목표숫자
card = list(map(int, input().split()))          # 카드에 쓰여있는 수

res = 0
ans = 0
# for i in range(0, N - 2):                         # 카드의 첫 숫자
#     res += card[i]
#     if res > M:
#         res -= card[i]
#         continue
#     else:
#         for j in range(i + 1, N - 1):                 # 카드 두번째 숫자
#             res += card[j]
#             if res > M:
#                 res -= card[j]
#                 continue
#             else:
#                 for k in range(j + 1, N):
#                     res += card[k]
#                     if res > M:
#                         res -= card[k]
#                         continue
#                     elif ans < res <= M:
#                         ans = res
#                     res -= card[k]
#             res -= card[j]
#     res -= card[i]
# print(ans)

for i in range(0, N - 2):                         # 카드의 첫 숫자
    for j in range(i + 1, N - 1):                 # 카드 두번째 숫자
        for k in range(j + 1, N):
            res = card[i] + card[j] + card[k]
            if ans < res <= M:
                ans = res
print(ans)