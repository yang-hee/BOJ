import sys
sys.stdin = open('input.txt')

N = int(input())
lst = list(map(int, input().split()))
lst2 = [-1001] * N
# print(lst, lst2)


lst2[0] = lst[0]                        # 이전 값과 비교하기 위해 for문 1부터 시작. 0번째 값 채워놓기!
for i in range(1, N):
    if lst2[i-1] > 0:
        lst2[i] = lst[i] + lst2[i-1]
    else:
        lst2[i] = lst[i]

# print(lst, lst2)
print(max(lst2))

# for i in range(len(lst)):
#     if lst[i] > 0:
#         sum_p += lst[i]
#     else:
#         if sum_p:
#             sum_lst.append(sum_p)
#             sum_p = 0
#         sum_lst.append(lst[i])
# if sum_p:
#     sum_lst.append(sum_p)
#
# for j in range()
# print(sum_lst)
# print(max(sum_lst))