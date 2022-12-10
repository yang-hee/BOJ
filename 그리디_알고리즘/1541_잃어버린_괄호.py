import sys
sys.stdin=open('1541_잃어버린_괄호.txt')

lst = list(input().split('-'))
for i in range(len(lst)):
    lst[i] = sum(list(map(int, lst[i].split('+'))))

res = lst[0]
for j in range(1, len(lst)):
    res -= lst[j]

print(res)

# lst = list(input().split('-'))
# if len(lst) == 1:
#     sum_list = list(map(int, lst[0].split('+')))
#     print(sum(sum_list))
# else:
#     res = sum(list(map(int, lst[0].split('+'))))
#
#     for i in range(1, len(lst)):
#         sub_list = list(map(int, lst[i].split('+')))
#         res -= sum(sub_list)
#     print(res)

