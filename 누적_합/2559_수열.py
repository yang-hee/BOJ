import sys
sys.stdin=open('2559_수열.txt')
N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
res = []
tem_sum = 0
for i in range(K):
    tem_sum += lst[i]
res.append(tem_sum)
for j in range(N - K):
    tem_sum = tem_sum - lst[j] + lst[j + K]
    res.append(tem_sum)
print(max(res))


#     for j in range(i, i + K):
#         tem_sum += lst[j]
#     res.append(tem_sum)
# print(max(res))
#
# # max_tem = 0
# # for i in range(N - K + 1):
# #     tem = sum(lst[i:i+K])
#     if max_tem < tem:
#         max_tem = tem
# print(max_tem)