import sys
sys.stdin = open('2078_무한이진트리.txt')
root_L = root_R = 1
L, R = map(int, input().split())


if L > 1:
    res_L = L - root_L
    res_R = (R - 1) // L
print(res_L, res_R)
# while root_R != R:
#     res_R += 1
#     root_R = L + root_R

# res_L = res_R = 0
# while root_L != L:
#     res_L += 1
#     root_L = root_L + root_R
#
# while root_R != R:
#     res_R += 1
#     root_R = root_L + root_R
# print(res_L, res_R)